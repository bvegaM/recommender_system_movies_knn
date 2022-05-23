from rest_framework import serializers

from ratings.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'user_id', 'movie_id', 'rating')