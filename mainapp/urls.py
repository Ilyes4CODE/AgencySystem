from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="main"),
    path('Our_Packages/',views.packages,name="packages"),
    path('about_us/',views.About,name="About"),
    path('Contact/',views.Contact,name="Contact"),
]
