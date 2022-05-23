from django.contrib import admin
from django.urls import path
from movies.views import (
    MovieAPIView,
    MovieAPITitleView,
    MovieAPIRecommenderView,
    MovieAPIViewById,
)
from ratings.views import (
    RatingAPIViewByUserId,
    RatingAPIViewByMovieId,
    RatingAPIViewPost,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', MovieAPIView.as_view()),
    path('movie/title/<str:title>/', MovieAPITitleView.as_view()),
    path('movie/id/<int:movie_id>/', MovieAPIViewById.as_view()),
    path('rating/<int:user_id>/', RatingAPIViewByUserId.as_view()),
    path('rating/post/', RatingAPIViewPost.as_view()),
    path('movie/details/<int:movie_id>/', RatingAPIViewByMovieId.as_view()),
    path('recommend/<str:title>/', MovieAPIRecommenderView.as_view()),
]
