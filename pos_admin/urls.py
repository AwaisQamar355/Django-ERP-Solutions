from django.urls import path
from pos_admin import views

urlpatterns = [
     path('admin_dashboard/',views.admin_dashboard, name='dashboard'),
# User
    path('user_list/', views.user_list, name='user_list'),
    path('add_user/', views.add_user, name='add_user'),
    path('user_update/<int:user_id>/', views.user_update, name='user_update'),
     path('activate_user/', views.activate_user, name='activate_user'),
    path('deactivate_user/', views.deactivate_user, name='deactivate_user'),
    # communication  
    path('send_email/<int:user_id>/', views.send_email, name='send_email'),
    # path('user_detail/<int:user_id>/', views.user_detail, name='user_detail'),
    path('success/', views.email_success, name='email_success'),
    path('email_log_list/', views.email_log_list, name='email_log_list'),
    path('email_log_detail/<int:user_id>/', views.email_log_detail, name='email_log_detail'),
# company
    path('company_list/', views.company_list, name='company_list'),
    path('<int:pk>/', views.company_detail, name='company_detail'),
    path('add/', views.company_create, name='add_company'),
    path('update_company/<int:company_id>/', views.update_company, name='update_company'),
     path('activate_company/', views.activate_company, name='activate_company'),
    path('deactivate_company/', views.deactivate_company, name='deactivate_company'),
    # path('<int:pk>/delete/', views.company_delete, name='company_delete'),
# Payment
    path('payment_list/', views.payment_list, name='payment_list'),
    path('add_payment/', views.add_payment, name='add_payment'),
    path('update_payment/<int:payment_id>/', views.update_payment, name='update_payment'),
    path('generate_invoice/<int:payment_id>/', views.generate_invoice, name='generate_invoice'),
    path('financial_report/', views.financial_report, name='financial_report'),
]
