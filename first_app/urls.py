from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views


app_name = 'first_app'

router = SimpleRouter()
router.register('books', views.BookViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('<str:name>/<int:num>/', views.hello),
    # path('', views.index),
    # path('redirect/', views.redirect),
    # path('books/', views.BookList.as_view(), name='book-list'),
    # path('books/<str:pk>/', views.BookList.as_view(), name='book-detail'),
    path('publisher/', views.PublisherList.as_view(), name='publisher-list'),
    path('publisher/<int:pk>/', views.PublisherDetails.as_view(), name='publisher-details'),
]