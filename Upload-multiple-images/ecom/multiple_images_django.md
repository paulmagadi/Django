# How to upload multiple images - Django

### Settings.py

```
STATICFILES_DIRS = [
    BASE_DIR / 'static/'
]

MEDIA_URL = 'media/'

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
```

### models.py

```
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='products/')
```


### Settings.py

```
STATICFILES_DIRS = [
    BASE_DIR / 'static/'
]

MEDIA_URL = '/media/'

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
```


### forms.py

```
from django import forms

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class UploadFileForm(forms.Form):
    files = MultipleFileField()
```

### views.py
```
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
            return redirect('home')
    else:
        form = UploadFileForm()

    return render(request, 'home.html', {'form': form, 'files': files})
```


### index.html
```
<!DOCTYPE html>
<html>
<head>
    <title>Upload and Display Files</title>
</head>
<body>
    <h2>Upload and Display Files</h2>

    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Upload</button>
    </form>

    <h3>Uploaded Files:</h3>
    <ul>
        {% for file in files %}
            <li><a href="{{ file.file.url }}">{{ file.file.name }}</a></li>
        {% empty %}
            <li>No files uploaded yet.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### urls.py (app)
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home")
]
```

### urls.py (project)
```
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from ecom import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```