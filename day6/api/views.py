from functools import partial
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request, pk=None):

    # try:
    #     stu = Student.objects.get(pk=pk)
    # except Student.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data , status=status.HTTP_302_FOUND )
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'PATCH':
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg':'Data Deleted Success...'}, status=status.HTTP_204_NO_CONTENT)
