from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import MyFileForm
from .models import MyFile


def file_upload_view(request):
    if request.method == 'POST':
        form = MyFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_upload')  # Redirect to a new URL
    else:
        form = MyFileForm()
    data = MyFile.objects.all()
    return render(request, 'test.html', context={'form': form, 'data': data})
