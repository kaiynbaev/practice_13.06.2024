from django.urls import path, include
# from .views import RegisterView, CustomLoginView
from .views import RegisterView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', CustomLogoutView.as_view(), name='logout'),
    # path('', include('django.contrib.auth.urls')),
]
