from django.contrib import admin
from django.urls import include, path
from tutorial.quickstart import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    # path(
    #     'api-auth/',
    #     include('rest_framework.urls', namespace='rest_framework')
    # ),
    path('', include('snippets.urls')),
]
