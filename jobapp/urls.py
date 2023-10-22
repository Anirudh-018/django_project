from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    # path('login/',views.login_users,name='login'),
    path('logout/',views.logout_users,name='logout'),
    path('register/',views.register_user,name='register'),
    path('job/<int:pk>',views.job_desc,name='job'),
    path('delete/<int:pk>',views.delete_job,name='delete')
]
