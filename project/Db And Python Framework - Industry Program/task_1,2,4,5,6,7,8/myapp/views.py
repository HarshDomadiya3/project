from django.shortcuts import render

# Create your viede
 
def indexview(request):
    return render(request,'myapp/index.html')