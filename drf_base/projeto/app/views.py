# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import *
from serializers import *


@api_view(['GET'])
def sports_list(request):
    """
    List all sports
    """
    if request.method == 'GET':
        sports = Sport.objects.all()
        serializer = SportSerializer(sports, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def new_sport(request):
    """
    Create a new Sport
    """
    if request.method == 'POST':
        serializer = SportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_sport(request, pk):
    """
    Get a specific sport
    """
    if request.method == 'GET':
        try:
            sport = Sport.objects.get(pk=pk)
            serializer = SportSerializer(sport)
            return Response(serializer.data)
        except Sport.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def players_list(request):
    """
    List all players
    """
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def new_player(request):
    """
    Create a new Player
    """
    if request.method == 'POST':
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_player(request, pk):
    """
    Get a specific player
    """
    if request.method == 'GET':
        try:
            player = Player.objects.get(pk=pk)
            serializer = PlayerSerializer(player)
            return Response(serializer.data)
        except Player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def players_list_from_sport(request, fk):
    """
    List all players from specific sport
    """
    if request.method == 'GET':
        try:
            player = Player.objects.filter(sport=fk)
            serializer = PlayerSerializer(player, many=True)
            return Response(serializer.data)
        except Player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)