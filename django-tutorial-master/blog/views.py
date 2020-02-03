from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
from .models import Post
from django.views.generic import View
from part2.utils import render_to_pdf
from django.conf import settings
from django.http import Http404
def view_post(request):
    posts = Post.objects.all() 
    context = {'posts': posts}
    return render(request, 'frontend/post.html', context)

def index(request):
    return render(request,'blog/index.html')
def python(request):
    return render(request,'blog/python.html')
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
 