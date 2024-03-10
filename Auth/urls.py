from django.urls import path
from . import views
urlpatterns = [
    path('Sign_Up/',views.SignupView,name="signup"),
    path('Login/',views.login_user,name="login"),
    path('Logout/',views.logout_view,name="Logout"),
    ##admin##
    path('Admin_Dash/',views.AdminDash,name="AdminDash"),
    path('Admin_Dash/<str:status>/',views.AdminDash,name="AdminDash"),
    path('Admin_Dash/Clients',views.get_all_clients,name="Clients"),
    path('Admin_Dash/Accept/<int:pk>/',views.Accepte_Demande,name="Accept"),
    path('Packages/',views.Admin_Packages,name="Admin_Packages"),
    path('Add_Package/',views.Add_Packages,name="Add_pack"),
    ##admin##
    path('Client_Profile/',views.ClientProfile,name="Client_Profile"),
    path('Update_Profile/',views.ClientSetting,name="ClientSetting"),
    path('Cliene_Packages/',views.Client_Packages,name="client_pack")
]
