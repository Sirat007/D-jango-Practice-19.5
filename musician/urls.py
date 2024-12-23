from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.Profile,name='profile'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.UserLogin.as_view(),name='login'),
    path('add/',views.AddMusician.as_view(),name='add_musician'),
    path('edit/<int:id>/',views.EditMusician.as_view(),name='edit_musician'),
    path('delete/<int:id>/',views.DeleteMusician.as_view(),name='delete_musician'),
    path('logout/',views.UserLogout,name='logout'),
]