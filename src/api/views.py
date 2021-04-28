from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Enter_Url


@api_view(['GET'])
def apioverview(request):

	api_urls = {

		'List':'/Url/',
		'Details View':'/Url-detal/<str:pk>/',
	}

	return Response(api_urls)
	
	
	
@api_view(['GET'])
def url_view(request):
	url = Enter_Url.objects.all()
	serializer = TaskSerializer(url,many = True)
	return Response(serializer.data)



@api_view(['GET'])
def url_post(request,inputdata):
	print(inputdata)
	serializer = TaskSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)




@api_view(['POST'])
def url_update(request,Inputdata):
	url = Enter_Url.objects.get()
	print(Inputdata)
	serializer = TaskSerializer(instance = url,data = request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)






@api_view(['DELETE'])
def url_delete(request,pk):
	url = Enter_Url.objects.get(id = pk)
	URL.delete()

	return Response("Item Deleted!!")