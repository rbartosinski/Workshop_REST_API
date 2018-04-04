from rest_framework import serializers
from movies.models import Person, Movie, StarringPersons


class RoleSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(source='person.id')
    name = serializers.CharField(source='person.name')

    class Meta:
        model = StarringPersons
        fields = ['id', 'name', 'role']


class MovieSerializer(serializers.ModelSerializer):
    starring = RoleSerializer(many=True, source='starringpersons_set')

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'director', 'starring', 'year']

    def update(self, instance, validated_data):
        actors_data = validated_data.pop('starringpersons_set')
        movie = super().update(instance, validated_data)
        for actor_data in actors_data:
            StarringPersons.objects.update_or_create(
                person_id=actor_data['person']['id'],
                movie_id=movie.id,
                defaults={'role': actor_data['role']}
            )
        return movie

    def create(self, validated_data):
        pass
        # Under construction
        # actors_data = validated_data.pop('starringpersons_set')
        # movie = Movie.objects.create(**validated_data)
        # for actor_data in actors_data:
        #     StarringPersons.objects.create(
        #         person=actor_data['person']['id'],
        #         movie=movie.id,
        #         defaults={'role': actor_data['role']}
        #     )
        # return movie


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'