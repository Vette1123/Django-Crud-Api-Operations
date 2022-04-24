from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('show/<std_id>', views.show, name='show'),
    path('delete/<std_id>', views.delete_student, name='delete'),
    path('add/', views.add_student, name='add'),
    path('edit/<std_id>', views.edit_student , name='edit'),

    #rest_framework api urls
    path('api-all/', views.api_all_student, name='api-all'),
    path('api-add/', views.api_add_student, name='api-add'),
    path('api-one/<std_id>', views.api_one_student, name='api-one'),
    path('api-edit/<std_id>', views.api_edit_student, name='api-edit'),
    path('api-delete/<std_id>', views.api_delete_student, name='api-delete'),
]
