from .views import *
from django.urls import path
 
 
urlpatterns = [

    path('api/AnimauxlostList/', AnimauxlostList.as_view(),name='Animauxlost-list'),
    path('api/AnimauxlostDetail/<int:pk>/', AnimauxlostDetail.as_view(), name='Animauxlost-detail'),

    path('api/AnimauxfoundList/', AnimauxfoundList.as_view(),name='Animauxfound-list'),
    path('api/AnimauxfoundDetail/<int:pk>/', AnimauxfoundDetail.as_view(), name='Animauxfound-detail'),

    path('api/AnimauxList/', AnimauxList.as_view(),name='Animaux-list'),

    path('api/AnimauxListser/', AnimauxListser.as_view(),name='Animaux-lists'),
    path('api/AnimauxfoundListser/', AnimauxfoundListser.as_view(),name='Animauxfound-lists'),
    path('api/AnimauxlostListser/', AnimauxlostListser.as_view(),name='Animauxlost-lists'),

    path('api/AnimauxList/<int:pk>/', AnimauxDetail.as_view(), name='Animaux-detail'),



    path('api/FavoriteList/', FavoriteList.as_view(),name='Favorite-lists'),
    path('api/FavoriteByidUser/<str:userid>/', FavoriteByidUser.as_view(), name='favorites-api'),

    path('api/FavoriteByidUserAndAnimid/', FavoriteByidUserAndAnimid.as_view(), name='favorites-api'),





]

 
