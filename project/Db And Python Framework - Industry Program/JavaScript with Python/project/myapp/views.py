from django.shortcuts import render, redirect
from .forms import UserForm

def show_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Process the form data (you can add your own logic here)
            # After form submission, redirect to the success page
            return redirect('success')  # Redirect to success view
    else:
        form = UserForm()  # Initialize an empty form
    return render(request, 'myapp/form.html', {'form': form})  # Render the form page

def success_page(request):
    return render(request, 'myapp/success.html')  # Render success page
