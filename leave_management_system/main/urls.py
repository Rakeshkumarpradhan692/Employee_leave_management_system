from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('employee-login/', views.employee_login, name='employee_login'),
    path('employee-signup/', views.employee_sign_up, name='employee_signup'),
     path('employee-dashboard/', views.employee_dashboard, name='employee_dashboard'),
     path('logout/', views.logout_view, name='logout'),  # Add logout URL
     path('apply-for-leave/', views.apply_for_leave, name='apply_for_leave'),
     path('employee-dashboard/', views.employee_dashboard, name='employee_dashboard'),
      path('holidays-taken/', views.holidays_taken, name='holidays_taken'),
       path('admin/leave-requests/', views.all_leave_requests, name='all_leave_requests'),  # Admin leave requests page
       path('admin/leave-requests/', views.all_leave_requests, name='all_leave_requests'),
    #    path('admin-login/', views.custom_admin_login, name='admin_login'),
      path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
      
      path('admin-login/', views.admin_login, name='admin_login'),  # Admin login page
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('approve-leave/<int:leave_id>/', views.approve_leave, name='approve_leave'),
    path('cancel-leave/<int:leave_id>/', views.cancel_leave, name='cancel_leave'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
     path('leave-success/', views.leave_success, name='leave_success'),
     
     
    # path('leave-success/', views.leave_success, name='leave_success'),
    
    
    
       

]
