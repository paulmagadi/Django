from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import UploadFileForm


def home(request):
    files = UploadedFile.objects.all()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for uploaded_file in request.FILES.getlist('files'):
                UploadedFile.objects.create(file=uploaded_file)
            return redirect('product')
    else:
        form = UploadFileForm()

    return render(request, 'home.html', {'form': form, 'files': files})
