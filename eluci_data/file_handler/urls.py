"""eluci_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import file_upload_handler, get_main_df, get_pc_df, get_lpc_df, get_plasmalogen_df, get_retention_rf_df, get_mean_agg_rf_df

urlpatterns = [
    path('upload/',file_upload_handler,name="file_upload_handler"),
    path('get_main_df/',get_main_df,name="get_main_df"),
    path('get_pc_df/',get_pc_df,name="get_pc_df"),
    path('get_lpc_df/',get_lpc_df,name="get_lpc_df"),
    path('get_plasmalogen_df/',get_plasmalogen_df,name="get_plasmalogen_df"),
    path('get_retention_rf_df/',get_retention_rf_df,name="get_retention_rf_df"),
    path('get_mean_agg_rf_df/',get_mean_agg_rf_df,name="get_mean_agg_rf_df"),
]
