import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

#for csrf_token by pass for post methods
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# for by pass csrf_token
@csrf_exempt
def student_api(request):
    #for data read.....
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)

        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    #For create data.....
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()

            #for response message to client / 3rd party app....
            res = {'msg':'Data Created Successfully!!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        # if condition validation is false... then to return error message
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    #For update data.......
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        #for partial update use partial=True....
        #for complete update remove partial=True
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Data Updated !!!!'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
            #return JsonResponse(response, safe=False)

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
        

    #For delete data.........
    if request.method =='DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        response = {'msg':'Data Deleted !!!!'}
        # json_data = JSONRenderer().render(response)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(response, safe=False)
    