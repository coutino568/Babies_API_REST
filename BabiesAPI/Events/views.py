from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EventSerializer, EventByIdSerializer
from Events.models import Event
from django.core import serializers

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
	queryset= Event.objects.all()
	serializer_class = EventSerializer

	def list (self, request):
		events= Event.objects.all()
		serializer_context = {'request': Request(request._request)}
		return Response(EventSerializer(events, many=True, context=serializer_context).data)


	def retrieve (self,request,pk):
		event = Event.objects.get(pk=pk)
		serializer_context={'request':Request(request._request)}
		return Response(EventByIdSerializer(event,context=serializer_context).data)