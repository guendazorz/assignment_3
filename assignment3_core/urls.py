from django.contrib import admin
from django.urls import path
from math_operations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.math_form, name='math_form'),
    path('result/', views.math_result, name='math_result'),
]

