from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework.decorators import api_view
from chairsapp.models import Product
from chairsapp.serializers import ProductsSerializer
from bot.bot import chair_agent

class AgentView(APIView):	
	def post(self, request):
		message = request.data.get('message')

		response = chair_agent().invoke({"question": message})
	
		items = response.items()

		# Convert dict_items to a list
		items_list = list(items)

		# Access the second item
		second_item = items_list[1]

		# Extract the value (if needed)
		second_item_value = second_item[1]

		response_json = json.loads(second_item_value)
		
		return Response(response_json)

@api_view(['GET'])
def lounge(request):
    lounge = Product.objects.filter(chair_type="Lounge Chair")
    serializer = ProductsSerializer(lounge, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def recliner(request):
    recliner = Product.objects.filter(chair_type="Recliner Chair")
    serializer = ProductsSerializer(recliner, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def patio(request):
    patio = Product.objects.filter(chair_type="Patio Chair")
    serializer = ProductsSerializer(patio, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def gaming(request):
    gaming = Product.objects.filter(chair_type="Gaming Chair")
    serializer = ProductsSerializer(gaming, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def office(request):
    office = Product.objects.filter(chair_type="Office Chair")
    serializer = ProductsSerializer(office, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def allprods(request):
    allprods = Product.objects.all()
    serializer = ProductsSerializer(allprods, many=True)
    return Response(serializer.data)