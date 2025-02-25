from typing import List

from django.core.cache import cache
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.decorators.http import require_http_methods

from core.models import Blog


@require_http_methods(["GET"])
def index(request: HttpRequest) -> HttpResponse:
    """Render the index page with a translated greeting message.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered index page with greeting message.
    """
    message = _("Hello There!")
    return render(request, 'index.html', {'message': message})


def get_cached_posts() -> List[Blog]:
    """Get posts from cache or database with proper error handling.

    Returns:
        List[Blog]: List of blog posts.
    """
    try:
        # Try to get posts from cache
        cached_posts = cache.get('blog_posts')
        if cached_posts is not None:
            return cached_posts

        # If not in cache, get from database and cache them
        posts = list(Blog.objects.filter(status=Blog.Status.PUBLISHED).order_by('-created_at'))
        cache.set('blog_posts', posts, timeout=60 * 15)  # Cache for 15 minutes
        return posts
    except Exception as e:
        # Log the error and return empty list as fallback
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error fetching posts: {str(e)}")
        return []


@require_http_methods(["GET"])
def posts(request: HttpRequest) -> HttpResponse:
    """Render the posts page with cached blog posts.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered posts page with blog posts.
    """
    posts = get_cached_posts()
    return render(request, 'posts.html', {'posts': posts})
