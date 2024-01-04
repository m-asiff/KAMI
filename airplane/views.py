from rest_framework.views import APIView
from airplane.airplane_controller import AirplaneController


# Create your views here.
class AirplaneView(APIView):
    airplane_controller = AirplaneController()

    @classmethod
    def get(cls, request, plane_id=None):
        return cls.airplane_controller.get_airplane(request, plane_id)

    @classmethod
    def post(cls, request):
        return cls.airplane_controller.add_airplane(request)

    @classmethod
    def patch(cls, request, plane_id=None):
        return cls.airplane_controller.update_airplane(request, plane_id)

    @classmethod
    def delete(cls, request, plane_id=None):
        return cls.airplane_controller.delete_airplane(request, plane_id)
