from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name="data_manage"),
    path('branch_update/', views.updateActiveFlag_branch, name="branch_disable_active_flag"),
    path('broker_update/', views.updateActiveFlag_broker, name="broker_disable_active_flag"),
]
