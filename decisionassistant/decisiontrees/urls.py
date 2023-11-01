from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DecisionTreeViewSet

router = DefaultRouter()
router.register(r'trees', DecisionTreeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
