from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie
from movies.serializer import MovieSerializer
from ratings.models import Rating
from ratings.serializer import RatingSerializer

import numpy as np


class RatingAPIViewByUserId(APIView):

    def get(self,request,user_id):
        ratings = Rating.objects.filter(user_id=user_id).order_by('-rating')
        serializer = RatingSerializer(ratings,many=True)
        return Response(serializer.data[:2])


class RatingAPIViewByMovieId(APIView):

    def get(self,request,movie_id):
        movie = Movie.objects.get(movie_id=movie_id)
        serializer_movie = MovieSerializer(movie)
        ratings = Rating.objects.filter(movie_id=movie_id).order_by('-rating')
        serializer = RatingSerializer(ratings,many=True)
        mean = np.mean([r['rating'] for r in serializer.data])
        return Response({'rating':mean,'movie_id':serializer_movie.data['movie_id'],'movie':serializer_movie.data['title']})

class RatingAPIViewPost(APIView):

    def post(self,request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
