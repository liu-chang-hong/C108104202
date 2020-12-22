from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, taipei, showpost, mychart ,chart , newtaipei, kao ,tyu, taipeicar,newtaipeicar,kaocar,tyucar
from mainsite import views

urlpatterns = [
    path('post/<str:slug>/', showpost),
    path('list/<int:id>/', views.showlist),
    path('admin/', admin.site.urls),
    path('playlist/', views.playlist),
    path('taipeicar/', views.playlist),
    path('newtaipeicar/', views.playlist1),
    path('kaocar/', views.playlist2),
    path('tyucar/', views.playlist3),
    path('taipei/', taipei),
    path('newtaipei/', newtaipei),
    path('kao/', kao),
    path('tyu/', tyu),
    path('taipeicar/', taipeicar),
    path('newtaipeicar/', newtaipeicar),
    path('kaocar/', kaocar),
    path('tyucar/', tyucar),
    path('mychart/', mychart),
    path('mychart/<int:bid>/', mychart),
    path('income_month/<int:year>/<int:month>/', chart ),
    path('', homepage),
]
