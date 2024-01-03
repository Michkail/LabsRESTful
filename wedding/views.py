from django.shortcuts import render


# Create your views here.
def wedding_index(request):
    return render(request, 'wedding/index.html')
