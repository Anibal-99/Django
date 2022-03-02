from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import PostCreateForm
from .models import Post
# Create your views here.
# Vamos a crear la vista del indice del blog
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        contex={

        }
        return render(request, 'blog_list.html', contex)

class BlogCreateView(View):
    def get (self, request, *args, **kwargs):
        form=PostCreateForm()
        context={
            'form':form
        }
        return render(request, 'blog_create.html', context)

# CREAMOS EL POST
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form=PostCreateForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data.get('title')
                content=form.cleaned_data.get('content')
            # creamos el post
                p,created= Post.objects.get_or_create(title=title,content=content)
                p.save()
                return redirect('blog:home ')
        context={
        }
        return render(request, 'blog_create.html', context)
