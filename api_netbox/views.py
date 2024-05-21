from django.http import JsonResponse
from .models import Netbox
from .serializers import NetboxSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET', 'POST'])
def netbox_list(request):

    #get all the netbox
    #serialize them
    #return json

    if request.method == 'GET':
        netbox = Netbox.objects.all()
        serializer = NetboxSerializer(netbox, many=True)
        return JsonResponse({'netbox': serializer.data})
    
    if request.method == 'POST':
        serializer = NetboxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
@api_view(['GET', 'PUT', 'DELETE'])
def netbox_details(request, id):


    try:
        netbox = Netbox.objects.get(pk=id)
    except Netbox.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NetboxSerializer(netbox)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = NetboxSerializer(netbox, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        netbox.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

