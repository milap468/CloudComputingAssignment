from django.urls import path
from .import views

urlpatterns = [
    path("",views.index,name="index"),
    path("file-upload/",views.file_upload,name="file-upload"),
    path('download/<uuid:file_id>/', views.download_file, name='download_video'),
    path('delete/<uuid:file_id>/', views.delete_file, name='delete-file'),

]
