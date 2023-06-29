from django.urls import path, include
from apps.home import views
from django.conf.urls.i18n import urlpatterns as i18n_urlpatterns



app_name = 'home'
urlpatterns = [

    # The home page
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('setting/',views.setting , name="setting"),
    path('profile/',views.profile , name="profile"),
    path('profile/<str:username>/', views.profile, name='user_profile'),
    path('Companys/',views.Companys , name="Companys"),
    path('Companys/<str:Ticker>',views.Companys , name="Companys"),
    #path('Companys/<str:Ticker>/<int:next_days>',views.Companys , name="Companys"),
    path('LastNews/',views.LastNews , name="LastNews"),
    path('aboutus/',views.aboutus , name="aboutus"),
    path('chart/',views.chart , name="chart"),
    path('chart/<str:Ticker>',views.chart , name="chart"),
    path('Community/',views.Community , name="Community"),
    path('StocksScreener/', views.StocksScreener , name="StocksScreener"),
    path('i18n/', include(i18n_urlpatterns)),#for translation

]
