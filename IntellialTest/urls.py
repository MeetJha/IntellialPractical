from django.contrib import admin
from django.urls import path
from RestManage import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index),
    path('create', views.create),
    path('data_stored', views.data_stored),
    path('data_deleted/<int:id>', views.data_deleted),
    path('edit_data/<int:id>', views.edit_data),
    path('data_updated/<int:id>', views.data_updated),
]
