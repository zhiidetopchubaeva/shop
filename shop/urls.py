from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ProductViewSet, CategoryViewSet, CommentViewSet, add_rating, toggle_like

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('toggle_like/<int:p_id>/', toggle_like),
    path('add_rating/<int:p_id>/',add_rating),
]
