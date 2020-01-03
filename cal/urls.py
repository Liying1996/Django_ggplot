from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'cal'

urlpatterns = [
    # path('', views.draw_plot, name='draw_plot')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)