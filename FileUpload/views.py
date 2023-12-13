from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import FileResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import FileUpload
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm
from django.conf import settings
import os

@login_required
def index(request):

    all_files = FileUpload.objects.all().filter(user=request.user)

    items_per_page = 10

    paginator = Paginator(all_files, items_per_page)
    page = request.GET.get('page')

    try:
        files = paginator.page(page)

    except PageNotAnInteger:

        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    context = {
        'files': files,
    }

    return render(request,"FileUpload/index.html",context)



@login_required
def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_upload_instance = form.save(commit=False)
            file_upload_instance.user = request.user
            file_upload_instance.save()
            return HttpResponseRedirect('/')
    else:
        form = FileUploadForm()

    return render(request, 'FileUpload/file_upload.html', {'form': form})


def download_file(request, file_id):
    file = FileUpload.objects.get(fileId=file_id)
    response = FileResponse(open(file.file.path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{file.file.name}"'
    return response




def delete_file(request, file_id):

    if request.method == 'POST':
        file = FileUpload.objects.get(fileId=file_id)
        base_dir = settings.BASE_DIR
        relative_path = os.path.join('media', file.file.name)
        file_path = os.path.join(base_dir, relative_path)
        os.remove(file_path)
        file.delete()
        return redirect('index')

    