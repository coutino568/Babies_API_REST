from django.shortcuts import render
from django.core import serializers
from rest_framework import viewsets
from .serializers import ParentSerializer, ParentByIdSerializer

from Parents.models import Parent
# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
	queryset= Event.objects.all()
	serializer_class = EventSerializer

	def list (self, request):
		parents= Parent.objects.all()
		serializer_context = {'request': Request(request._request)}
		return Response(ParentSerializer(parents, many=True, context=serializer_context).data)


	def retrieve (self,request,pk):
		parent = Parent.objects.get(pk=pk)
		serializer_context={'request':Request(request._request)}
		return Response(ParentByIdSerializer(parent,context=serializer_context).data)