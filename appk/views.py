from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Animaux
from .serializers import *
from django.utils import timezone
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework import status
from PIL import Image

 

 # AnimauxlostList

class AnimauxlostList(ListAPIView):

    queryset = Animauxlost.objects.all()
    serializer_class = AnimauxlostSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'age']

    def get(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

 

    def post(self, request):
        serializer = AnimauxlostSerializer(data=request.data)
        if serializer.is_valid():
            animauxlost =serializer.save()
            # Perform image resizing or other operations
            image_file = request.data['image']
            image = Image.open(image_file)
            # Resize the image
            image.thumbnail((400, 400))
            # Save the resized image
            image.save(animauxlost.image.path)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    




 # Animauxfound
class AnimauxfoundList(ListAPIView):

    queryset = Animauxfound.objects.all()
    serializer_class = AnimauxfoundSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['couleur', 'age']

    def get(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        # if response.status_code == 404:
        #      print("Les données n'existent pas.")
        # else:

        #     # Gérez les autres codes d'erreur HTTP si nécessaire
        #     print(f"Erreur HTTP : {response.status_code}")     

        return Response(serializer.data)

 

    def post(self, request):
        serializer = AnimauxfoundSerializer(data=request.data)
        if serializer.is_valid():
            animauxfound =serializer.save()
            # Perform image resizing or other operations
            image_file = request.data['image']
            image = Image.open(image_file)
            # Resize the image
            image.thumbnail((400, 400))
            # Save the resized image
            image.save(animauxfound.image.path)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   



 
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class AnimauxListser(ListAPIView):

    queryset = Animaux.objects.all()
    serializer_class = AnimauxSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name','addrs','bred','size','age']
    search_fields = ['name','addrs','bred','size','age']


class AnimauxfoundListser(ListAPIView):

    queryset = Animauxfound.objects.all()
    serializer_class = AnimauxfoundSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['addrs','bred','size','age']
    search_fields = ['addrs','bred','size','age']    


class AnimauxlostListser(ListAPIView):

    queryset = Animauxlost.objects.all()
    serializer_class = AnimauxlostSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name','addrs','bred','size','age']
    search_fields = ['name','addrs','bred','size','age']




class AnimauxList(ListAPIView):

    queryset = Animaux.objects.all()
    serializer_class = AnimauxSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['addrs']
    search_fields = ['name', 'age']

    def get(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

 

    def post(self, request):
        serializer = AnimauxSerializer(data=request.data)
        if serializer.is_valid():
            animaux =serializer.save()
            # Perform image resizing or other operations
            image_file = request.data['image']
            image = Image.open(image_file)
            # Resize the image
            image.thumbnail((400, 400))
            # Save the resized image
            image.save(animaux.image.path)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    






class AnimauxlostDetail(APIView):
    def get(self, request, pk):
        animauxlost = get_object_or_404(Animauxlost, pk=pk)
        serializer = AnimauxlostSerializer(animauxlost)
        return Response(serializer.data)

    def put(self, request, pk):
        animauxlost = get_object_or_404(Animauxlost, pk=pk)
        serializer = AnimauxlostSerializer(animauxlost, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        animauxlost = get_object_or_404(Animauxlost, pk=pk)
        animauxlost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












class AnimauxfoundDetail(APIView):
    def get(self, request, pk):
        animauxfound = get_object_or_404(Animauxfound, pk=pk)
        serializer = AnimauxfoundSerializer(animauxfound)
        return Response(serializer.data)

    def put(self, request, pk):
        animauxfound = get_object_or_404(Animauxfound, pk=pk)
        serializer = AnimauxfoundSerializer(Animauxfound, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        animauxfound = get_object_or_404(Animauxfound, pk=pk)
        animauxfound.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



 
 

class AnimauxDetail(APIView):
    def get(self, request, pk):
        animaux = get_object_or_404(Animaux, pk=pk)
        serializer = AnimauxSerializer(animaux)
        return Response(serializer.data)

    def put(self, request, pk):
        animaux = get_object_or_404(Animaux, pk=pk)
        serializer = AnimauxSerializer(animaux, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        animaux = get_object_or_404(Animaux, pk=pk)
        animaux.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class FavoriteList(ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
     

    def get(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

 

    def post(self, request):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            favorite =serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   




from rest_framework import generics
class FavoriteByidUser(generics.ListAPIView):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        userid = self.kwargs['userid']
        return Favorite.objects.filter(userid=userid)



# class FavoriteByidUserAndAnimid(generics.ListAPIView):
#     serializer_class = FavoriteSerializer

#     def get_queryset(self):
#         animid = self.request.query_params.get('animid')
#         userid = self.request.query_params.get('userid')
        
#         queryset = Favorite.objects.all()
        
#         if animid:
#             queryset = queryset.filter(animid=animid)
        
#         if userid:
#             queryset = queryset.filter(userid=userid)
        
#         return queryset



class FavoriteByidUserAndAnimid(generics.ListAPIView):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        animid = self.request.query_params.get('animid')
        userid = self.request.query_params.get('userid')

        queryset = Favorite.objects.all()

        if animid:
            queryset = queryset.filter(animid=animid)

        if userid:
            queryset = queryset.filter(userid=userid)

        return queryset

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
