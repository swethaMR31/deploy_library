from django.urls import path, include
from . import views

#urlpatterns = [path("",views.index),]
from . views import *

urlpatterns = [
    path('', Myview.as_view(),),
    path('create/',Employee_create.as_view() ),
    path('list/', Employee_list.as_view() ),
    path('<pk>/',Employee_Detail.as_view()),
   path('<pk>/update',Employee_Update.as_view()),
   path('<pk>/delete/',Employee_Delete.as_view())
    ]