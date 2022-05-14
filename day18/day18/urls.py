from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


#for auth token ... user request...
# from rest_framework.authtoken.views import obtain_auth_token

#custom authtoken...
# from api.auth import CustomAuthToken


#using signals authtoken...



#Creating Router object

router = DefaultRouter()


# Register class_name_"StudentViewSet" with router
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    #for session authentication username and password prompted on webbrowser 
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

    #for authtoken user request
    # path('gettoken/', obtain_auth_token),

    #for customauthtoken...
    # path('gettoken/', CustomAuthToken.as_view()),

]
