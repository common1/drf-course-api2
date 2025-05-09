from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('products/', views.ProductListCreateAPIView.as_view()),
    path('products/info/', views.product_info),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view()),
]

router = DefaultRouter()
router.register(r'orders', views.OrderViewSet)
urlpatterns += router.urls