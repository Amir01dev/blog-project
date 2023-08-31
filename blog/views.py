from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse, Http404
from .models import *
from .form import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST
# from django.db.models import Q
# from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def post_list(request, category=None):
    if category is not None:
        posts = Post.published.filter(category=category)
    else:
        posts = Post.published.all()
    paginator = Paginator(posts, 6)
    page_num = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_num)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, "blog/list.html", context)
    # return HttpResponse('Post List')
# class PostListView(ListView):
#     # model = Post
#     queryset = Post.published.all()
#     template_name = 'blog/list.html'
#     paginate_by = 3
#     context_object_name = "posts"


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    # try:
    #     post = Post.published.get(id=pk)
    # except:
    #     raise Http404("Not Found :((")
    comments = post.comments.filter(active=True)
    form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, "blog/detail.html", context)
    # return HttpResponse(f"post: {pk}")


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/detail.html'


def ticket(request):
    # روش اول برای ایجاد آبجکت تیکت 👇🏻
    # if request.method == "POST":
    #     form = TicketForm(request.POST)
    #     if form.is_valid():
    #         ticket_obj = Ticket.objects.create()
    #         cd = form.cleaned_data
    #         ticket_obj.message = cd['message']
    #         ticket_obj.name = cd['name']
    #         ticket_obj.phone = cd['phone']
    #         ticket_obj.email = cd['email']
    #         ticket_obj.subject = cd['subject']
    #         ticket_obj.save()
    #         return redirect('blog:index')
    # else:
    #     form = TicketForm()
    # روش دوم برای ایجاد آبجکت تیکت 👇🏻
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Ticket.objects.create(message=cd['message'], name=cd['name'], email=cd['email'],
                                  phone=cd['phone'], subject=cd['subject'])
            return redirect("blog:index")
    else:
        form = TicketForm()
    return render(request, 'form/ticket.html', {"form": form})


@require_POST
def post_comment(request, pk):
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    context = {
        'post': post,
        'form': form,
        'comment': comment
    }
    return render(request, "form/comment.html", context)


def post_search(request):
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(data=request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results1 = Post.published.annotate(similarity=TrigramSimilarity('title', query)) \
                .filter(similarity__gt=0.1)
            results2 = Post.published.annotate(similarity=TrigramSimilarity('description', query)) \
                .filter(similarity__gt=0.1)
            results = (results1 | results2).order_by('-similarity')
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'blog/search.html', context)


@login_required
def profile(request):
    user = request.user
    posts = Post.published.filter(author=user)
    return render(request, "blog/profile.html", {'posts': posts})


@login_required
def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            Image.objects.create(image_file=form.cleaned_data['img1'], post=post)
            Image.objects.create(image_file=form.cleaned_data['img2'], post=post)
            return redirect("blog:profile")
    else:
        form = CreatePostForm()
    return render(request, "form/create_post.html", {'form': form})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:profile')
    return render(request, 'form/delete-post.html', {'post': post})


@login_required
def delete_image(request, pk):
    image = get_object_or_404(Image, id=pk)
    image.delete()
    return redirect('blog:profile')


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            Image.objects.create(image_file=form.cleaned_data['img1'], post=post)
            Image.objects.create(image_file=form.cleaned_data['img2'], post=post)
            return redirect("blog:profile")
    else:
        form = CreatePostForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, "form/create_post.html", context)


# function to login user👇🏻
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('blog:profile')
#                 else:
#                     return HttpResponse('شما در سایت غیرفعال شده اید.')
#             else:
#                 return HttpResponse('همچین کاربری در سایت وجود ندارد.')
#     else:
#         form = LoginForm()
#     return render(request, 'form/login.html', {'form': form})

# function to logout user
def log_out(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Account.objects.create(user=user)
            return render(request, 'registration/register_done.html', {'user': user})
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def edit_account(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        account_form = AccountEditForm(request.POST, files=request.FILES, instance=request.user.account)
        if account_form.is_valid() and user_form.is_valid():
            account_form.save()
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        account_form = AccountEditForm(instance=request.user.account)
    context = {
        'user_form': user_form,
        'account_form': account_form
    }
    return render(request, 'registration/edit_account.html', context)
