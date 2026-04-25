from types import new_class
from django.shortcuts import render
from .models import News

# Create your views here.

# don't make same function name and veriable nane its give erro
def news(request):
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss':newss})
