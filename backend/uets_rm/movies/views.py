# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie
from movies.serializer import MovieSerializer

import joblib
import pandas as pd
import numpy as np

class MovieAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class MovieAPITitleView(APIView):

    def get(self, request, title):
        movie = Movie.objects.get(title=title)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

class MovieAPIViewById(APIView):

    def get(self, request, movie_id):
        movie = Movie.objects.get(movie_id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

class MovieAPIRecommenderView(APIView):

    def get(self, request, title):
        #cargo el modelo de ml
        model = joblib.load('/Users/bvegam/Documents/proyectos/movie_recommender_system/backend/uets_rm/model/knn_model.pkl')

        #obtengo la pelicula a recomendar
        movie = Movie.objects.get(title=title)
        serializer = MovieSerializer(movie)

        #cargar el conjunto de datos compilado
        df = pd.read_csv('/Users/bvegam/Documents/proyectos/movie_recommender_system/backend/uets_rm/data/movies_to_user.csv')
        df = df.set_index('title')


        #realizar la recomendación
        movies_list = list(df.index)
        movie_dict = {movie: index for index, movie in enumerate(movies_list)}

        index = movie_dict[serializer.data['title']]
        knn_input = np.asarray([df.values[index]])
        n = min(len(movies_list) - 1, 10)
        distances, indices = model.kneighbors(knn_input, n_neighbors=n + 1)

        response = []
        for i in range(1, n + 1):
            movie = Movie.objects.get(title=movies_list[indices[0][i]])
            serializer = MovieSerializer(movie)
            response.append(serializer.data)

        return Response(response)

