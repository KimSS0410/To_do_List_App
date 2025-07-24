from django.contrib import admin
from django.urls import path
from todo.views import todo_list, todo_info


urlpatterns = [
    path('todo/', todo_list, name='todo_list'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
    path('admin/', admin.site.urls),
]

#기본 URL에 페이지 띄우기
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("404 뜨는거 보기 싫어서 기본 페이지 만듬")),
    path('todo/', include('todo.urls')),
    path('admin/', admin.site.urls),
]