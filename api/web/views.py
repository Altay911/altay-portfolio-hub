from django.shortcuts import render, redirect
from hub.models import Link 

def home_view(request):
    # Fetch all links from the database
    # Group them by category later in the HTML
    items = Link.objects.all() 
    
    context = {
        'items': items
    }
    return render(request, 'web/index.html', context)


def resume_view(request):
    return redirect('https://drive.google.com/file/d/1aDwx5j2SdcXPc4hGHjeZ9AFE79LZMyN7/view?usp=sharing')