from django.urls import re_path 
from userCRUD import views 
 
urlpatterns = [ 
    re_path(r'^api/create-user$', views.user_create),
    re_path(r'^api/get-users$', views.user_read),
    re_path(r'^api/delete-user/(?P<username>[A-Za-z]+)$', views.user_delete),
    re_path(r'^api/update-user/(?P<username>[A-Za-z]+)$', views.user_update)
]