from django.urls import path
from . import views

app_name = 'cashflow'

urlpatterns = [
    # Main pages
    path('', views.cashflow_list, name='cashflow_list'),
    path('create/', views.cashflow_create, name='cashflow_create'),
    path('edit/<int:pk>/', views.cashflow_edit, name='cashflow_edit'),
    path('delete/<int:pk>/', views.cashflow_delete, name='cashflow_delete'),
    
    # Dictionary management
    path('dictionaries/', views.dictionaries, name='dictionaries'),
    path('dictionaries/status/', views.status_list, name='status_list'),
    path('dictionaries/status/create/', views.status_create, name='status_create'),
    path('dictionaries/status/edit/<int:pk>/', views.status_edit, name='status_edit'),
    path('dictionaries/status/delete/<int:pk>/', views.status_delete, name='status_delete'),
    
    path('dictionaries/type/', views.type_list, name='type_list'),
    path('dictionaries/type/create/', views.type_create, name='type_create'),
    path('dictionaries/type/edit/<int:pk>/', views.type_edit, name='type_edit'),
    path('dictionaries/type/delete/<int:pk>/', views.type_delete, name='type_delete'),
    
    path('dictionaries/category/', views.category_list, name='category_list'),
    path('dictionaries/category/create/', views.category_create, name='category_create'),
    path('dictionaries/category/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('dictionaries/category/delete/<int:pk>/', views.category_delete, name='category_delete'),
    
    path('dictionaries/subcategory/', views.subcategory_list, name='subcategory_list'),
    path('dictionaries/subcategory/create/', views.subcategory_create, name='subcategory_create'),
    path('dictionaries/subcategory/edit/<int:pk>/', views.subcategory_edit, name='subcategory_edit'),
    path('dictionaries/subcategory/delete/<int:pk>/', views.subcategory_delete, name='subcategory_delete'),
    
    # API endpoints for AJAX
    path('api/get_categories/<int:type_id>/', views.get_categories, name='get_categories'),
    path('api/get_subcategories/<int:category_id>/', views.get_subcategories, name='get_subcategories'),
]