from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context=context)


# this replaces the function view approach above
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"  # Django default: <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ("-date_posted",)


class PostDetailView(DetailView):
    model = Post
    # below variable is not needed because default already used
    # template_name = "blog/post_detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ("title", "content")
    template_name = "blog/post_form_new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ("title", "content")
    template_name = "blog/post_form_update.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = "post"
    success_url = "/"  # redirects to URL after deletion. In this case the home page.

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, "blog/about.html", context={"title": "About"})
