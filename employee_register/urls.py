from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employee_form,name='employee_insert'),  # get and post insert operations
    path('<int:id>/', views.employee_form,name='employee_update'), # get and post update operations
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('list/',views.employee_list,name='employee_list') #get request to retrieve and diaplay all records

]
