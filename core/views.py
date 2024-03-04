from django.core.cache import cache
from django.core import serializers
from redis import Redis
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _

from core.models import Blog

redis_cache = Redis(host='localhost', port=6379, db=0, decode_responses=True)


# This function is responsible for rendering the index page.
# It also translates a greeting message using gettext.
def index(request):
    message = _("Hello There!.")  # This is the translation string
    return render(request, 'index.html', {'message': message})


# This function is responsible for rendering the posts page.
# It first tries to get the posts from Django's cache.
# If the posts are not in the cache, it fetches them from the database and stores them in the cache.
def posts_django_cache(request):
    cached_posts = cache.get('cached_posts')
    if not cached_posts:
        db_posts = list(Blog.objects.all())
        cache.set('cached_posts', db_posts, 60 * 15)
    return render(request, 'posts.html', {'posts': cached_posts})


# This function is responsible for rendering the posts page.
# It first tries to get the posts from Redis cache.
# If the posts are not in the cache, it fetches them from the database, serializes them and stores them in the cache.
# If the posts are in the cache, it deserializes them before rendering.
def posts(request):
    cached_posts = redis_cache.get('cached_posts')
    if not cached_posts:
        db_posts = list(Blog.objects.all())
        serialized_db_posts = serializers.serialize('json', db_posts)
        redis_cache.set('cached_posts', serialized_db_posts, 60 * 15)
    else:
        cached_posts = serializers.deserialize('json', cached_posts)
    return render(request, 'posts.html', {'posts': [post.object for post in cached_posts]})
