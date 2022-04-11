from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.detail import DetailView
from blog.models import  Post, Comment, Category
from blog.forms import PostForm, CommentForm, CategoryForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime

def create_category(request):
    form = CategoryForm(request.POST or None) 
    if form.is_valid(): 
        form.save()  
    categories = Category.objects.all()
    messages.success(request, "Category created successfully.")
    context = {
        'category_form': form,
        'categories': categories,
    }
    return render(request, "blog/create_category.html", context)      


def create_post(request):
    posts=Post.objects.all()

    # create post
    form = PostForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        instance = form.save(commit=False)
        instance.author = request.user
        instance.slug=slugify(instance.title)
        instance.status = 0
        instance.save() 
        messages.success(request, "Blog post created successfully.")
        return redirect('post_list')
    context = {
        'post_form': form,
        'posts': posts,
    }
    return render(request, "blog/create_post.html", context)  


def post_list(request):
    context = {}
    if request.user.is_staff:
        post_list = Post.objects.all()  
    else:
        post_list = Post.objects.filter(status=1)

    categories = Category.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {
        # 'popular_posts': popular_posts,
        'categories':categories,
        'posts': posts,
    }
    return render(request, "blog/post_list.html", context)


        

def post_detail(request, pk):
    blog_post = get_object_or_404(Post, pk=pk)
   
    # comments 
    comment_form  = CommentForm(request.POST or None, request.FILES or None, initial={"post": blog_post}) 
    if comment_form.is_valid(): 
        instance = comment_form.save(commit=False)
        instance.post = blog_post
        instance.time = datetime.now()
        instance.status = 1
        instance.author = request.user
        instance.save() 
        messages.success(request, "Comment registered.")
        return redirect('post_detail', pk=blog_post.id )

    comments = Comment.objects.filter(post=blog_post)
  
    context = {
        'post': blog_post,
        'comment_form': comment_form,
        'comments': comments,
        'comment_count': comments.count()
    }
    return render(request, 'blog/post_detail.html', context)


def post_update(request, pk):
    blog_post = get_object_or_404(Post, pk=pk)
    update_post = CommentForm(request.POST or None, request.FILES or None, instance=blog_post) 
    if update_post.is_valid(): 
        instance = update_post.save(commit=False)
        instance.time = datetime.now()
        instance.save() 
        messages.success(request, "Blog post updated.")
        return redirect('post_detail', pk=blog_post.id ) 
    context = {
        'post': blog_post,
        'update_post': update_post,
    }
    return render(request, 'blog/post_update.html', context)


def post_search(request):
    context = {}
    posts = Post.objects.filter(status=1)
    if request.user.is_staff:
        posts = Post.objects.all()  
    else:
        posts = Post.objects.filter(status=1)

    if request.method == "GET":
        query = request.GET.get("search")
        queryset = posts.filter(Q(title__icontains=query))

        page = request.GET.get("page")
        paginator = Paginator(queryset, 5)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        qs_results = queryset.count()
        context.update({
            "page":page,
            "qs_results":qs_results,
            "query":query,
            "posts":posts,

        })
        return render(request, "blog/post_search.html", context)



@user_passes_test(lambda u: u.is_staff)
def post_visibility(request, pk):
    blog = get_object_or_404(Post, pk=pk) 
    if blog.status == 1:
        blog.status = 0
        messages.success(request, "The blog has been moved to drafts.")
        blog.save()
        return redirect('post_list')
    else:
        blog.status = 1
        blog.save()
        messages.success(request, "The blog has been published.")
        return redirect('post_list')

  


# class PostDetailView(HitCountDetailView):
#     model = Post
#     template_name = "blog/post.html"
#     slug_field = "slug"
#     count_hit = True

#     form = CommentForm

#     def post(self, request, *args, **kwargs):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             post = self.get_object()
#             form.instance.user = request.user
#             form.instance.post = post
#             form.save()

#             return redirect(reverse("post", kwargs={
#                 'slug': post.slug
#             }))


#     def get_context_data(self, **kwargs):
#         similar_posts = self.object.tags.similar_objects()[:3]
#         tags = self.object.tags.all()
#         post_comments = Comment.objects.all().filter(post=self.object.id).filter(status=1)
#         post_comments_count = post_comments.count()
#         context = super().get_context_data(**kwargs)
#         context.update({
#             "similar_posts":similar_posts,
#             'form': self.form,
#             'post_comments': post_comments,
#             'post_comments_count': post_comments_count,
#             'tags': tags,
#         })
#         return context
