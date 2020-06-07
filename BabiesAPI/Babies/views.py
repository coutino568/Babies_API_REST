from django.shortcuts import render
from .serializers import BabySerializer, BabyByIdSerializer

# Create your views here.
from Babies.models import Baby
from Babies.serializers import BabySerializer


class BabiesViewSet(viewsets.ModelViewSet):
	queryset= Baby.objects.all()
	serializer_class = BabySerializer

	def list (self, request):
		babies= Baby.objects.all()
		serializer_context = {'request': Request(request._request)}
		return Response(BabySerializer(babies, many=True, context=serializer_context).data)


	def retrieve (self,request,pk):
		baby = Baby.objects.get(pk=pk)
		serializer_context={'request':Request(request._request)}
		return Response(BabyByIdSerializer(baby,context=serializer_context).data)