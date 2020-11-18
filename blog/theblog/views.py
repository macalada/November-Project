from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def LikeView(request, pk):
    post=get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else :
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args = [str(pk)]))


# def home(request):
#     return render (request, "home.html", {})

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-post_date']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context= super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context


def CategoryView(request, cats):
    category_post= Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_post':category_post})

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

    
    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context= super(PostDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"]=cat_menu
        context["total_likes"]=total_likes
        context["liked"]=  liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context= super(AddPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context
    # fields = '__all__'
    # fields = ('title','author', 'body')

class AddCategoryView(CreateView):
    model = Category
    template_name = "add_category.html"
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "update_post.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context= super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context
    # fields =['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url= reverse_lazy('home')