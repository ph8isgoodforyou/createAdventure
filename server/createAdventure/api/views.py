from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from api.models import (
    Trip as TripModel,
    Country as CountryModel,
    City as CityModel,
    PointOfInterest as PointOfInterestModel
)
from api.serializer import (
    TripSerializer,
    CountrySerializer,
    CitySerializer,
    PointOfInterestSerializer,
)

# ----------------------------------------------------------------------------------------------Trips
class listOfTrips(APIView):
    """
    List all trips, or create a new trip.
    """

    # authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_staff:
            trips = TripModel.objects.all()
        else:
            trips = TripModel.objects.filter(author=user)

        if trips.count() > 0:
            serializer = TripSerializer(trips, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)


    def post(self, request):
        user = request.user
        trip = TripModel(author=user)
        serializer = TripSerializer(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Trip(APIView):
    """
    Retrieve, update or delete a trip instance.
    """

    # @authentication_classes([TokenAuthentication])
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = request.user
        try:
            trip = TripModel.objects.get(pk=pk)

            if user.is_staff or user == trip.author:
                serializer = TripSerializer(trip)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            else:
                return JsonResponse([], status=status.HTTP_401_UNAUTHORIZED)
            if trip.author != user:
                return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)
        except TripModel.DoesNotExist:
            return JsonResponse([], status=status.HTTP_404_NOT_FOUND, safe=False)

    def put(self, request, pk):
        user = request.user
        try:
            trip = TripModel.objects.get(pk=pk)

            if user.is_staff or trip.author == user:
                serializer = TripSerializer(trip, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            elif trip.author != user:
                return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

        except TripModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def delete(self, request, pk):
        user = request.user
        try:
            trip = TripModel.objects.get(pk=pk)

            if user.is_staff or trip.author == user:
                trip.delete()
                return JsonResponse(204, status=status.HTTP_204_NO_CONTENT, safe=False)
            elif trip.author != user:
                return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

        except TripModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

# ----------------------------------------------------------------------------------------------Countries in a trip
#
# class Trip_Countries(APIView):
#     """
#     List all countries, or create a new country.
#     """
#
#     # queryset = CountryModel.objects.all()
#     # serializer_class = CountrySerializer
#
#     # permission_classes = [IsAuthenticated]
#
#     def get_trip_object(self, request, trip_pk):
#         try:
#             trip = TripModel.objects.get(pk=trip_pk)
#             return trip
#         except TripModel.DoesNotExist:
#             return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
#
#     def get(self, request, trip_pk):
#         # trip = self.get_trip_object(request, trip_pk)
#         countries = CountryModel.objects.filter(trip=trip_pk)
#         if countries.count() > 0:
#             serializer = CountrySerializer(countries, many=True)
#             return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
#         else:
#             return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
#
#     def post(self, request, trip_pk):
#         serializer = CountrySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class Trip_Country(APIView):
#     """
#     Retrieve, update or delete a country instance.
#     """
#
#     # permission_classes = [IsAuthenticated]
#
#     def get(self, request, trip_pk, country_pk):
#         try:
#             country = CountryModel.objects.get(pk=country_pk)
#             serializer = CountrySerializer(country)
#             return JsonResponse(serializer.data, status=status.HTTP_200_OK)
#         except CountryModel.DoesNotExist:
#             return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
#
#     def put(self, request, trip_pk, country_pk):
#         try:
#             country = CountryModel.objects.get(pk=country_pk)
#             serializer = CountrySerializer(country, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, status=status.HTTP_200_OK)
#             else:
#                 return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except CountryModel.DoesNotExist:
#             return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
#
#
#     def delete(self, request, trip_pk, country_pk):
#         try:
#             country = CountryModel.objects.get(pk=country_pk)
#             country.delete()
#             return JsonResponse(204, status=status.HTTP_204_NO_CONTENT, safe=False)
#         except CountryModel.DoesNotExist:
#             return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

# ----------------------------------------------------------------------------------------------Countries
class listOfCountries(APIView):
    """
    List all countries, or create a new country.
    """


    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_staff:
            countries = CountryModel.objects.all()
        else:
            countries = CountryModel.objects.filter(author=user)

        if countries.count() > 0:
            serializer = CountrySerializer(countries, many=True)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        else:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)


    def post(self, request):
        user = request.user
        print(request.data['trip'])
        country = CountryModel(author=user)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Country(APIView):
    """
    Retrieve, update or delete a country instance.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = request.user
        try:
            country = CountryModel.objects.get(pk=pk)

            if user.is_staff or user == country.author:
                serializer = CountrySerializer(country)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            else:
                return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)
        except CountryModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def put(self, request, pk):
        user = request.user
        try:
            country = CountryModel.objects.get(pk=pk)

            if user.is_staff or country.author == user:
                serializer = CountrySerializer(country, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            if country.author != user:
                return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)
        except CountryModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def delete(self, request, pk):
        user = request.user
        try:
            country = CountryModel.objects.get(pk=pk)

            if user.is_staff or user == country.author:
                country.delete()
                return JsonResponse(204, status=status.HTTP_204_NO_CONTENT, safe=False)
            if country.author != user:
                return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

        except CountryModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)


# ----------------------------------------------------------------------------------------------Cities
class listOfCities(APIView):
    """
    List all cities or Create a new city
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_staff:
            cities = CityModel.objects.all()
        else:
            cities = CityModel.objects.filter(author=user)

        if cities.count() > 0:
            serializer = CitySerializer(cities, many=True)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        else:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def post(self, request):
        user = request.user
        city = CityModel(author=user)
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class City(APIView):
    """
        Retrieve, update or delete a city instance.
    """

    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = request.user
        try:
            city = CityModel.objects.get(pk=pk)

            if user.is_staff or user == city.author:
                serializer = CitySerializer(city)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)

            if user == city.author:
                return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

        except CityModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def put(self, request, pk):
        user = request.user
        try:
            city = CityModel.objects.get(pk=pk)

            if user.is_staff or user == city.author:
                serializer = CitySerializer(city, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            if user != city.author:
                return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)
        except CityModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def delete(self, request, pk):
        user = request.user
        try:
            city = CityModel.objects.get(pk=pk)

            if user.is_staff or user == city.author:
                city.delete()
                return JsonResponse(204, status=status.HTTP_204_NO_CONTENT, safe=False)
            if user != city.author:
                return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)
        except CityModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)


# ----------------------------------------------------------------------------------------------PointsOfInterest
class listOfPointsOfInterest(APIView):
    """
    List all pointOfInterest, or create a new pointOfInterest.
    """

    # permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_staff:
            pointsOfInterest = PointOfInterestModel.objects.all()
        else:
            pointsOfInterest = PointOfInterestModel.objects.filter(author=user)
        if pointsOfInterest.count() > 0:
            serializer = PointOfInterestSerializer(pointsOfInterest, many=True)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        else:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def post(self, request):
        user = request.user

        pointsOfInterest = PointOfInterestModel(author=user)

        serializer = PointOfInterestSerializer(pointsOfInterest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class pointOfInterest(APIView):
    """
    Retrieve, update or delete a pointOfInterest instance.
    """

    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = request.user
        try:
            pointOfInterest = PointOfInterestModel.objects.get(pk=pk)

            if user.is_staff or user == pointOfInterest.author:
                serializer = PointOfInterestSerializer(pointOfInterest)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            if pointOfInterest.author != user:
                return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)
        except PointOfInterestModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def put(self, request, pk):
        user = request.user
        try:
            pointOfInterest = PointOfInterestModel.objects.get(pk=pk)


            if user.is_staff or user == pointOfInterest.author:
                serializer = PointOfInterestSerializer(pointOfInterest, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            if pointOfInterest.author != user:
                return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

        except PointOfInterestModel.DoesNotExist:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def delete(self, request, pk):
        user = request.user
        try:
            pointOfInterest = PointOfInterestModel.objects.get(pk=pk)

            if user.is_staff or user == pointOfInterest.author:
                pointOfInterest.delete()
                return JsonResponse(204, status=status.HTTP_204_NO_CONTENT, safe=False)
            if pointOfInterest.author != user:
                return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)
        except PointOfInterestModel.DoesNotExist:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
