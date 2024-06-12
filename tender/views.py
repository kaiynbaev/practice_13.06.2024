from django.shortcuts import render
from .models import Tender, UserModel, TenderOffer
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TenderForm, OfferForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.


def index(request):
    return render(request, 'tender/index.html')


def main(request):
    return render(request, 'tender/main.html')


def customers(request):
    return render(request, 'tender/customers.html')


def contractors(request):
    return render(request, 'tender/contractors.html')


def success_login(request):
    return render(request, 'tender/success_login.html')


def tender_list(request):
    tenders = Tender.objects.order_by('-create_date')
    return render(request, 'tender/elements/contractors/tender_list.html', {'tenders': tenders})

UserModel

def add_tender(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TenderForm(request.POST)
            if form.is_valid():
                tender = form.save(commit=False)
                tender.customer = request.user  # Устанавливаем текущего пользователя как заказчика
                tender.save()
                return redirect('tender_list')
        else:
            form = TenderForm()
        return render(request, 'tender/elements/customers/add_tender.html', {'form': form})
    else:
        return redirect('login')  # Перенаправляем на страницу входа


@login_required
def create_offer(request, tender_id):
    tender = get_object_or_404(Tender, pk=tender_id)

    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.tender = tender
            offer.user = request.user
            offer.save()
            return redirect('tender_detail', tender_id=tender.id)
    else:
        form = OfferForm()

    return render(request, 'tender/elements/contractors/create_offer.html', {'form': form, 'tender': tender})

@login_required
def tender_detail(request, tender_id):
    tender = get_object_or_404(Tender, pk=tender_id)
    offers = TenderOffer.objects.filter(tender=tender)
    return render(request, 'tender/elements/contractors/tender_detail.html', {'tender': tender, 'offers': offers})


@login_required
def send_offer(request, tender_id):
    tender = get_object_or_404(Tender, id=tender_id)
    user_choices = [(user.id, user.username) for user in UserModel.objects.all()]

    if request.method == 'POST':
        form = OfferForm(request.POST, user_choices=user_choices)
        if form.is_valid():
            contractor_id = form.cleaned_data['contractor']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            
            contractor = UserModel.objects.get(id=contractor_id)
            tender.offer.add(contractor)
            tender.price = price
            tender.description = description
            tender.save()
            return redirect('tender_detail', tender_id=tender_id)
    else:
        form = OfferForm(user_choices=user_choices)
    return render(request, 'tender/elements/contractors/send_offer.html', {'form': form, 'tender': tender})


@login_required
def accept_offer(request, offer_id):
    offer = get_object_or_404(TenderOffer, id=offer_id)
    tender = offer.tender

    if request.user == tender.customer:
        tender.contractor = offer.user
        tender.is_active = False
        offer.is_accepted = True
        tender.save()
        offer.save()

    return redirect('tender_detail', tender_id=tender.id)


