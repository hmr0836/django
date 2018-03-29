from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    pall = Post.objects.all()
    return render(request,'posts/index.html', {
        'posts':pall,
    })

def new():
    pass

def show(request,pk):
   #pselect = Post.objects.get(pk=pk)
    pselect = get_object_or_404(Post,pk=pk)
    return render(request, 'posts/show.html' , {
        'posts':pselect,
    })
def edit():
    pass

def delete():
    pass
