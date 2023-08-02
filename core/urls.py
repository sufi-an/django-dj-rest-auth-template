from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from rest_framework.routers import DefaultRouter
from . import views

from .views import *
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()
from django.views.decorators.csrf import csrf_exempt

# create a router and register our viewsets with it
# router.register(r'v1/subject-category-list', views.SubjectCategoryViewSet)

router.register(r'v1/user', user_list_view)

urlpatterns = [

    path('', include(router.urls)),
    #re_path(r'^get-user/$', getUserViewSet.as_view(),name='get_user'),  path('v1/task/<str:username>/', TaskList, name='task-list')
     #path('v1/save-new-task/', saveNewTask, name='save_new_task'),
    # path('v1/task-assign/', TaskAssignsListView, name='TaskAssignsListView')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path, include,re_path
from rest_framework.routers import DefaultRouter




