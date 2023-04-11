from django.urls import path, include
from apps.home import views
from django.conf.urls.i18n import urlpatterns as i18n_urlpatterns




urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('setting/',views.setting , name="setting"),
    path('profile/',views.profile , name="Profile"),
    path('Companys/<str:Ticker>',views.Companys , name="Companys"),
    path('LastNews/',views.LastNews , name="LastNews"),
    path('Trending/',views.Trending , name="Trending"),
    path('chart/',views.chart , name="chart"),
    path('Community/',views.Community , name="Community"),
   
    path('i18n/', include(i18n_urlpatterns)),#for translation

]
