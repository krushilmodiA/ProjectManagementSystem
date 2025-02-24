from django.shortcuts import render

from feedback.models import Feedback

# Create your views here.
def index(request):
    # feedback data print from database
    #   feedback = Feedback.objects.filter(created_by = request.user)

    #   return render(request, 'core/index.html',{
    #     'feedback': feedback,
    #   })
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')