from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')
def info1(request):
    return render(request, 'main/full_info1.html')
def info2(request):
    return render(request, 'main/full_info2.html')