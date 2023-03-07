 
from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),
    path('setting/',views.setting , name="setting"),
    path('Profile/',views.profile , name="Profile"),
    path('Companys/',views.Companys , name="Companys"),
    path('LastNews/',views.LastNews , name="LastNews"),
    path('Trending/',views.Trending , name="Trending"),
    path('chart/',views.chart , name="chart"),
    path('Community/',views.Community , name="Community"),
   

]
