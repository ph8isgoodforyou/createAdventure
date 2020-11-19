from rest_framework import serializers

#PointOfInterestSerializer  CitySerializer  TripSerializer  CountrySerializer
from api.models import Country, Trip, City, PointOfInterest


class PointOfInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfInterest
        fields = [
            'id',
            'title',
            'price',
            'work_hours',
            'city'
        ]
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.work_hours = validated_data.get('work_hours', instance.work_hours)

        instance.city_id = validated_data['city'].id

        instance.save()
        return instance

class CitySerializer(serializers.ModelSerializer):
    pointsOfInterest = PointOfInterestSerializer(required=False, many=True)
    class Meta:
        model = City
        fields = [
            'id',
            'title',
            'population',
            'country',
            'pointsOfInterest',
        ]
    def create(self, validated_data):
        pointsOfInterest_data = validated_data.pop('pointsOfInterest', None)
        city = City.objects.create(**validated_data)

        if pointsOfInterest_data is not None:
            for pointOfInterest_data in pointsOfInterest_data:
                PointOfInterest.objects.create(city=city, **pointOfInterest_data)

        return city

    def update(self, instance, validated_data):
        pointsOfInterest_data = validated_data.pop('pointsOfInterest')
        pointsOfInterest_list = (instance.pointsOfInterest).all()
        pointsOfInterest_list = list(pointsOfInterest_list)
        instance.title = validated_data.get('title', instance.title)
        instance.population = validated_data.get('population', instance.population)

        instance.country_id = validated_data['country'].id

        instance.save()

        for pointOfInterest_data in pointsOfInterest_data:
            pointOfInterest = pointsOfInterest_list.pop(0)
            pointOfInterest.title = pointOfInterest_data.get('title', pointOfInterest.title)
            pointOfInterest.price = pointOfInterest_data.get('price', pointOfInterest.price)
            pointOfInterest.work_hours = pointOfInterest_data.get('work_hours', pointOfInterest.work_hours)
            pointOfInterest.save()
        return instance

class CountrySerializer(serializers.ModelSerializer):
    cities = CitySerializer(required=False, many=True)
    class Meta:
        model = Country
        fields = [
            'id',
            'title',
            'population',
            'religion',
            'currency',
            'time_zone',
            'cities',
            'trip'
        ]

    def create(self, validated_data):
        cities_data = validated_data.pop('cities', None)
        country = Country.objects.create(**validated_data)

        if cities_data is not None:
            for city_data in cities_data:
                City.objects.create(country=country, **city_data)

        return country

    def update(self, instance, validated_data):
        cities_data = validated_data.pop('cities')
        cities_list = (instance.cities).all()
        cities_list = list(cities_list)
        instance.title = validated_data.get('title', instance.title)
        instance.population = validated_data.get('population', instance.population)
        instance.religion = validated_data.get('religion', instance.religion)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.time_zone = validated_data.get('time_zone', instance.time_zone)

        instance.trip_id = validated_data['trip'].id

        instance.save()

        for city_data in cities_data:
            city = cities_list.pop(0)
            city.title = city_data.get('title', city.title)
            city.population = city_data.get('population', city.population)
            city.save()
        return instance

class TripSerializer(serializers.ModelSerializer):
    countries = CountrySerializer(required=False, many=True)
    time_published = serializers.TimeField(format='%H:%M', read_only=True)
    time_updated = serializers.TimeField(format='%H:%M', read_only=True)
    class Meta:
        model = Trip
        fields = [
            'id',
            'title',
            'description',
            'trip_type',
            'date_published',
            'time_published',
            'date_updated',
            'time_updated',
            'trip_overall_price',
            'countries',
        ]

    def create(self, validated_data):
        countries_data = validated_data.pop('countries', None)
        trip = Trip.objects.create(**validated_data)

        if countries_data is not None:
            for country_data in countries_data:
                Country.objects.create(trip=trip, **country_data)

        return trip

    def update(self, instance, validated_data):
        countries_data = validated_data.pop('countries')
        country_list = (instance.countries).all()
        country_list = list(country_list)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.trip_type = validated_data.get('trip_type', instance.trip_type)
        instance.trip_overall_price = validated_data.get('trip_overall_price', instance.trip_overall_price)
        instance.save()

        for country_data in countries_data:
            country = country_list.pop(0)
            country.title = country_data.get('title', country.title)
            country.population = country_data.get('population', country.population)
            country.religion = country_data.get('religion', country.religion)
            country.currency = country_data.get('currency', country.currency)
            country.time_zone = country_data.get('time_zone', country.time_zone)
            country.save()
        return instance
