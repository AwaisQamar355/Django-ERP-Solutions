from django.urls import path
from authenticate import views
urlpatterns = [

# Groups
#     path('insert_group/', views.insert_group , name='insert_group'),
#     path('list_group/', views.list_group, name='list_group' ),
#     path('delete_group/<int:id>/', views.delete_group, name="delete_group"),
#     path('edit_group/<int:id>/', views.edit_group, name="edit_group"),
#     path('update_group/<int:id>', views.update_group, name='update_group'),
    
# User Login 
    path('user_login',views.user_login,name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'), 
    
] 



