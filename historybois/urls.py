from django.contrib import admin
from django.urls import path, include
from posts import urls as posts
from accounts import urls as accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts)),
    path('', include(posts)),
    path('markdownx/', include('markdownx.urls')),
]
