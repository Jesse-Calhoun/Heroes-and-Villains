from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serliazers import SuperSerializer
from .models import Super


@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET':
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
