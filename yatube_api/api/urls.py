from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import (CommentModelViewSet, GroupReadOnlyModelViewSet,
                       PostModelViewSet)


router = DefaultRouter()
router.register('posts', PostModelViewSet)
router.register('groups', GroupReadOnlyModelViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentModelViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
