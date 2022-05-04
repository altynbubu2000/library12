from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

r = DefaultRouter()
r.register('book', views.BooksViewSet)
r.register('lib', views.LibuserViewSet)
r.register('rent', views.RentBookViewSet)


urlpatterns = [
    path('category-create/', views.BookcategoryCreateView.as_view()),
    path('category-list-create/', views.BookCategoryListCreateView.as_view()),
    path('category-retrieve/<int:pk>', views.BookCategoryRetrieveView.as_view()),
    path('category-update/<int:pk>', views.BookCategoryUpdateView.as_view()),
    path('category-retrieve-update/<int:pk>', views.BookCategoryUpdateRetrieveView.as_view()),
    path('category-destroy/<int:pk>', views.BookCategoryDestroyView.as_view())
]
urlpatterns += r.urls
