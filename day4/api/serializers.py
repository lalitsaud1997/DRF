from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student

# Validators....
def start_with_l(value):
    if value[0].lower() != 'l':
        raise serializers.ValidationError('Name should be start with L')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_l])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    #Validation are manly three types:
    #1. field level validations ,
    #2. object level validations and 
    #3. validators
    ## Priority::::: validators > field level validations > object level validations


    #Field level validation
    def validate_roll(self, value):
        if value >200:
            raise serializers.ValidationError('Admission seat is full!!!')
        return value

    #object level validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'lalit' and city.lower() != 'delhi':
            raise serializers.ValidationError('city must be delhi....')
        return data
        


