from django.urls import path
from rest_framework import routers
from api import views


urlpatterns = [
    path('category-list/', views.BookcategoryListView.as_view()),
    path('category-create/', views.BookcategoryCreateView.as_view()),
    path('category-list-create/', views.BookCategoryListCreateView.as_view()),
    path('category-retrieve/<int:pk>', views.BookCategoryRetrieveView.as_view()),
    path('category-update/<int:pk>', views.BookCategoryUpdateView.as_view()),
    path('category-retrieve-update/<int:pk>', views.BookCategoryUpdateRetrieveView.as_view()),
    path('category-destroy/<int:pk>', views.BookCategoryDestroyView.as_view())
     
    
]
