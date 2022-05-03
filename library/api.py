from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'books', views.BooksViewSet, basename='books')
router.register(r'lib-users', views.LibuserViewSet)
router.register(r'rented-books', views.RentBookViewSet)




for url in router.urls:
    print(url,'/n')