from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


#Creating Router object

router = DefaultRouter()


# Register class_name_"StudentViewSet" with router
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    #for session authentication username and password prompted on webbrowser 
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

]
