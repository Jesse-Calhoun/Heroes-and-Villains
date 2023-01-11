from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serliazers import SuperSerializer
from .models import Super


@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET':
        super_type = request.query_params.get('type')
        supers = Super.objects.all()
        if super_type:
            supers = supers.filter(super_type__type=super_type)
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            heroes = supers.filter(super_type__type='hero')
            heroes_serializer = SuperSerializer(heroes, many=True)
            villains = supers.filter(super_type__type='villain')
            villains_serializer = SuperSerializer(villains, many=True)
            custom_response = {'heroes' : heroes_serializer.data,'villains' : villains_serializer.data}
            return Response(custom_response)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)