from django.shortcuts import render
from .forms import MyForm

def form_view(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data here
            return render(request, 'myapp/success.html')
    else:
        form = MyForm()

    return render(request, 'myapp/form.html', {'form': form})
