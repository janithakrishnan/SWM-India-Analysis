from django.urls import path
from . import views
urlpatterns=[path("",views.home,name='home'),
             path("chart/average/", views.chart_average, name="chart_average"),
             path("chart/total/", views.chart_total, name="chart_total"),
             path("chart/processed/", views.chart_processed, name="chart_processed"),
             path("download-excel/", views.download_excel, name="download_excel")]