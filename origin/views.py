from django.shortcuts import render

def index(request):
    return render(request, template_name="index.html", context={
        'name': "Mai tri Tue"
    })



# Create your views here.
