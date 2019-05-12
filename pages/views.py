from django.shortcuts import render
from django.http import HttpResponse
from quote.models import Quote

# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    
    context = {
        'quotes': quotes,
        
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')