from django.shortcuts import render
from rest_framework import viewsets,status,generics
from api import serializers
from rest_framework.response import Response
from api.models import Book, BookCategory,LibUser,RentBook
from api.pagination import CustomPagination
from api.serializers import BookCategorySerializer, BookSerializer,LibUserSerializer,RentBookSerializer
#viewsset:list,create,retrieve,update,partial_update,destroy

class BooksViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Book.objects.all()
        serializers = BookSerializer(queryset,many=True)
        return Response(serializers.data)
    
    
    def post(self,request):
        serializers = BookSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    





# class BooksViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    
    
    
class LibuserViewSet(viewsets.ModelViewSet):
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer 
    pagination_class = CustomPagination   
    
    
class RentBookViewSet(viewsets.ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer
    
#--------------------------------


#get
class BookcategoryListView(generics.ListAPIView):
    queryset = BookCategory.objects.all()
    serializers_class = BookCategorySerializer
    
#post
class BookcategoryCreateView(generics.CreateAPIView):
    queryset = BookCategory.objects.all()
    serializers_class = BookCategorySerializer

#get and post   
class BookCategoryListCreateView(generics.ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializers_class = BookCategorySerializer
    
#get
class BookCategoryRetrieveView(generics.RetrieveAPIView):
    queryset = BookCategory.objects.all()
    serializers_class= BookCategorySerializer
    
    
#Put
class BookCategoryUpdateView(generics.UpdateAPIView):
    queryset = BookCategory.objects.all()
    serializers_class= BookCategorySerializer
    
    
#get and put
class BookCategoryUpdateRetrieveView(generics.RetrieveUpdateAPIView):
    queryset = BookCategory.objects.all()
    serializers_class= BookCategorySerializer
    

#delete
class BookCategoryDestroyView(generics.DestroyAPIView):
    queryset = BookCategory.objects.all()
    serializers_class= BookCategorySerializer
    
    