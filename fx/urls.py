from django.urls import path
from . import views

app_name = 'fx'

urlpatterns = [
    path('convert/<str:base>/', views.convert, name='convert'),

]