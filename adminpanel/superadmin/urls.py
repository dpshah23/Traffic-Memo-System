from django.contrib import admin
from django.urls import path
from superadmin import views

urlpatterns = [
   path('home/',view=views.index,name='index'),
   path('password-change/',view=views.pswdChange,name='pswdChange'),
   path('memo/',view=views.memoView,name='memo'),
   path('user-details/',view=views.userDetails,name='userDet'),
   path('login',views.login,name="login"),
   path('staff/',views.staff,name="staff")
]
