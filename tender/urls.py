from django.urls import path
from tender.views import (index, main, customers, contractors, success_login, tender_list, tender_detail,
    add_tender, create_offer, accept_offer, send_offer)


urlpatterns = [
    path('', index, name='index'),

    path('main/', main, name='main'),

    path('customers/add_tender/', add_tender, name='add_tender'),
    path('customers/<int:offer_id>/accept/', accept_offer, name='accept_offer'),
    # path('customers/add_tender', customers, name='customers'),
    # path('customers/add_tender/', add_tender, name='add_tender'),
   

    path('contractors/', contractors, name='contractors'),
    path('contractors/tenders/', tender_list, name='tender_list'),
    path('contractors/<int:tender_id>/create_offer/', create_offer, name='create_offer'),

    path('tenders/<int:tender_id>/', tender_detail, name='tender_detail'),
    path('offers/<int:offer_id>/accept/', accept_offer, name='accept_offer'),


    path('contractors/send_offer/<int:tender_id>/', send_offer, name='send_offer'),
    

    path('profile/', success_login, name='success_login'),
]