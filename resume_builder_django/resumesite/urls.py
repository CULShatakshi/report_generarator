from django.urls import path
from . import views


urlpatterns = [
    
    path('report_informal/', views.report_informal, name="report_informal"),
    path('informal/',views.info,name="info"),
    path('', views.homepage, name="homepage"),
    path('formal/', views.formal, name="formal"),
    path('report_formal/', views.report_formal, name="report_formal"),
    path('new/', views.new, name="new"),
   
]
