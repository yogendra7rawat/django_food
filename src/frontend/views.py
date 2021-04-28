from django.shortcuts import render,redirect

from .models import Enter_Url
from .form import UrlForm

# Create your views here.
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_pb2, status_code_pb2

channel = ClarifaiChannel.get_grpc_channel()

# Note: You can also use a secure (encrypted) ClarifaiChannel.get_grpc_channel() however
# it is currently not possible to use it with the latest gRPC version

stub = service_pb2_grpc.V2Stub(channel)

# This will be used by every Clarifai endpoint call.
metadata = (('authorization', 'Key 32067f835e484ea6afc8926b47131b09'),)


l = []

image = []

def List(request):
	if request.method == 'POST':
		l[:] = []
		image[:] = []
		
		url = request.POST.get('your_url')
		image.append(url)
		Request = service_pb2.PostModelOutputsRequest(
		model_id='bd367be194cf45149e75f01d59f77ba7',
		inputs=[
		  resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(url='{}'.format(url))))
		])
		response = stub.PostModelOutputs(Request, metadata=metadata)

		if response.status.code != status_code_pb2.SUCCESS:
			raise Exception("Request failed, status code: " + str(response.status.code))

		for concept in response.outputs[0].data.concepts:
			print(concept.name,concept.value)
			l.append([concept.name, concept.value])
	return render(request,'list.html',{})

def Results(request):
	context = {"data":l,"image":image}
	return render(request,'home.html',context)



