from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.html import strip_tags
import uuid

class HistoryPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    uid = models.CharField(
        primary_key=True,
        unique=True,
        max_length=4,
        editable=False
    )
    title = models.CharField(max_length=20)
    post = MarkdownxField()
    created_at = models.DateField(default=timezone.now, editable=False)
    updated_at = models.DateField(auto_now=True)

    @property
    def post_md(self):
        return markdownify(strip_tags(self.post))

    def save(self, *args, **kwargs):
        while True:
            unique_uid = str(uuid.uuid4())[:8]
            if not HistoryPost.objects.filter(uid=unique_uid).exists():
                break


        self.uid = unique_uid
        super(HistoryPost, self).save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        return reverse_lazy('posts:post_detail', kwargs={'pk': self.uid})

    def __str__(self):
        return f"\"{self.title}\" by {self.author}"

