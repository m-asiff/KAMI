from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK, \
    HTTP_204_NO_CONTENT

from airplane.models import Airplane
from airplane.serializers import AirplaneSerializer


class AirplaneController:

    @classmethod
    def get_airplane(cls, request, plane_id=None):
        if plane_id:
            try:
                airplane = Airplane.objects.get(plane_id=plane_id)
                serializer = AirplaneSerializer(airplane)
                return Response(data=serializer.data, status=HTTP_200_OK)
            except Airplane.DoesNotExist:
                return Response(data={'error': 'Airplane with the provided plane_id does not exist.'}, status=HTTP_404_NOT_FOUND)

        airplanes = Airplane.objects.all()
        serializer = AirplaneSerializer(airplanes, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

    @classmethod
    def add_airplane(cls, request):

        # As we have to allow 10 airplanes
        if Airplane.objects.count() >= 10:
            raise ValidationError("Cannot add more than 10 airplanes.")

        serialized_airplane = AirplaneSerializer(data=request.data)
        if serialized_airplane.is_valid(raise_exception=True):
            serialized_airplane.save()
            return Response(data=serialized_airplane.data, status=HTTP_201_CREATED)
        return Response(data=serialized_airplane.errors, status=HTTP_400_BAD_REQUEST)

    @classmethod
    def update_airplane(cls, request, plane_id=None):
        if plane_id is None:
            return Response({'error': 'plane_id is required.'}, status=HTTP_400_BAD_REQUEST)

        try:
            airplane = Airplane.objects.get(plane_id=plane_id)

        except Airplane.DoesNotExist:
            return Response(data={'error': 'Airplane with the provided plane_id does not exist.'}, status=HTTP_404_NOT_FOUND)

        serializer = AirplaneSerializer(airplane, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @classmethod
    def delete_airplane(cls, request, plane_id=None):
        if plane_id is None:
            return Response({'error': 'plane_id is required.'}, status=HTTP_400_BAD_REQUEST)
        try:
            airplane = Airplane.objects.get(plane_id=plane_id)
            airplane.delete()
            return Response(data={'message': 'Airplane deleted'}, status=HTTP_204_NO_CONTENT)
        except Airplane.DoesNotExist:
            return Response(data={'error': 'Airplane with the provided plane_id does not exist.'}, status=HTTP_404_NOT_FOUND)
