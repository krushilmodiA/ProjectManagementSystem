
from django.contrib import admin
from django.urls import path,include

# for image
from django.conf import settings # this line is for image.
from django.conf.urls.static import static # this line is for image.
# for image

urlpatterns = [
        #this is core app path  
    path('', include('core.urls')),

    #this is feedback app path  
    path('feedback/', include('feedback.urls')),

        #this is account app path  
    path('', include('account.urls')),

        #this is project app path.
    path('projects/', include('project.urls')),
    
    #this is todolist app path and it is inside in the project app.
    path('projects/<uuid:project_id>/', include('todolist.urls')),
    
    #this is task app path and it is inside in the todolist app.
    path('projects/<uuid:project_id>/<uuid:todolist_id>/', include('task.urls')),
    
    path('admin/', admin.site.urls),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # this line is for image.
