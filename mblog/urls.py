from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, lotto, showpost, mychart 
from mainsite import views

urlpatterns = [
    path('post/<str:slug>/', showpost),
    path('list/<int:id>/', views.showlist),
    path('admin/', admin.site.urls),
    path('playlist/', views.playlist),
    path('lotto/', lotto),
    path('mychart/', mychart),
    path('mychart/<int:bid>/', mychart),
    path('', homepage),
]
