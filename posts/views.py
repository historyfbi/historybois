from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models

# CREATE "Post"
class PostCreate(LoginRequiredMixin, CreateView):
    model = models.HistoryPost
    fields = ('title', 'post')
    template_name = 'posts/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# READ "Post" - list
class PostList(ListView):
    model = models.HistoryPost
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ["-updated_at"]
    
# READ "Post" - detail
class PostDetail(DetailView):
    model = models.HistoryPost
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

# UPDATE "Post"
class PostUpdate(UserPassesTestMixin, UpdateView):
    model = models.HistoryPost

    fields = ('title', 'post')
    template_name = 'posts/post_update.html'
    context_object_name = 'post'

    def form_valid(self, form):
        form.instance.updated = True
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        return self.request.user == post.author

# DELETE "Post"
class PostDelete(UserPassesTestMixin, DeleteView):
    model = models.HistoryPost
    template_name = 'posts/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts:post_create')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
