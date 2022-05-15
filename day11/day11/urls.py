from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

#Creating Router object

router = DefaultRouter()


# Register class_name_"StudentViewSet" with router
router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]