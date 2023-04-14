from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import (filters, mixins, pagination, permissions,
                            serializers, viewsets)

from posts.models import Comment, Follow, Group, Post

from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        return Comment.objects.filter(post=self.get_post().id)

    def perform_create(self, serializer):
        serializer.save(post=self.get_post(), author=self.request.user)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise serializers.ValidationError('Такая подписка уже есть!')

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)
