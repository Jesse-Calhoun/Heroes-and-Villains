from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serliazers import SuperSerializer
from .models import Super


@api_view(['GET'])
def supers_list(request):
    supers = Super.objects.all()
    serializer = SuperSerializer(supers, many=True)
    return Response(serializer.data)