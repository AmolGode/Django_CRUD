from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_form,name='employee_insert'),
    path('<int:id>/',views.employee_form,name='employee_update'),
    path('list/',views.employee_list),
    path('employee_delete/<int:id>/',views.employee_delete,name='employee_delete')
]