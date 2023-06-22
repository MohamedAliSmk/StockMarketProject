from django.urls import path, re_path
from . import views

urlpatterns = [
#path('', RedirectView.as_view(url='AiPred/', permanent=True)),
#path('Pred/',views.Company , name="ModelP" , permanent=True),
path('train_model/', views.train, name='train_model'),

path('predict/', views.pred, name='predict'),
#path('predict_api/', views.predict_api, name='predict_api'),
path('plot_predicrtions/', views.plot_data, name='plot_predicrtions'),


#path('Companys/<str:symbol>',views.prediction , name="prediction"),
#path('Companys/<str:symbol>',views.predict_next_day , name="predict_next_day"),

]
