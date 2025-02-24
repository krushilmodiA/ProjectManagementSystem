from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# project model
from project.models import Project

from core.views import *
from core.templates import *
# <----- START-EMAIL ----->
from django.core.mail import send_mail  #EmailMessage
from django.conf import settings
# <----- END-EMAIL ----->

# feedback model or own model
from .models import Feedback
# Create your views here.

@login_required
def feedbacks(request):
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        desc = request.POST.get('desc', '')
        email = request.POST.get('email', '')

        if name and email:
           Feedback.objects.create(name=name, email=email, desc= desc, created_by=request.user)
           print("feedback Done")

           subject = name
           message = desc
           from_email = settings.EMAIL_HOST_USER
           recipient_list = [email]
           send_mail(subject, message, from_email, recipient_list)
           return redirect('/')
           
        else:
            print("not send data..")

    return render(request, 'feedback/feedback.html')

# @login_required
# def add(request, project_id):
#     project = Project.objects.filter(created_by = request.user).get(pk = project_id)

#     if request.method == "POST":
#         name = request.POST.get('name', '')
#         description = request.POST.get('description', '')

#         if name:
#             Feedback.objects.create(project = project, name = name, description = description, created_by = request.user)    

#             return redirect('/projects/')

#     return render(request, 'feedback/add.html')