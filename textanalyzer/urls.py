from django.urls import path
from . import views

urlpatterns = [
    # Note: We removed 'admin/' path because we disabled the admin app
    path('', views.home, name='home'),
    path('analyze', views.analyze, name='analyze'),
]