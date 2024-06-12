# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from tender.views import success_login

class RegisterView(FormView):
    template_name = 'registration/registration_form.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('main')  

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())



# class CustomLoginView(LoginView):
#     form_class = LoginForm
#     template_name = 'registration/login_form.html'
#     success_url = reverse_lazy('success_login')


# class CustomLogoutView(LogoutView):
#     form_class = LogoutView
#     success_url = reverse_lazy('main')

