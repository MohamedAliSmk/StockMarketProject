 
from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),
    path('outh/',include('social_django.urls'), name='social'),
    path("Companys/", include("Model.urls")),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

