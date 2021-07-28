from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('',views.home, name='home'),
    path('futsal/<slug:slug>',views.detail, name='detail')
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)