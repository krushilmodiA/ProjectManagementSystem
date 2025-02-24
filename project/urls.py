from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('add/', views.add, name='add'),
    path('<uuid:pk>/', views.project, name='project'),
    path('<uuid:pk>/edit/', views.edit, name='edit'),
    path('<uuid:pk>/delete/', views.delete, name='delete'),
    # files upload url
    path('<uuid:project_id>/files/upload_file/', views.upload_file, name='upload_file'), # for add file or image in project app.
    path('<uuid:project_id>/files/<uuid:pk>/delete/', views.delete_file, name='delete_file'), # for delete file or image in project app.
    # note add url
    path('<uuid:project_id>/notes/add/', views.create_note, name='create_note'), # for add or create note in project app.
    path('<uuid:project_id>/notes/<uuid:pk>/', views.note_detail, name='note_detail'), # for open note in another app.
    path('<uuid:project_id>/notes/<uuid:pk>/edit/', views.note_edit, name='note_edit'), # for edit note in project app.
    path('<uuid:project_id>/notes/<uuid:pk>/delete/', views.note_delete, name='note_delete'), # for edit note in project app.

    

    

    
    


]