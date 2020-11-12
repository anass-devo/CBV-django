from django.urls import path
from . import views

app_name ="post"

urlpatterns =[
    path('',views.PostList.as_view() , name='post_list'),
    path('<int:id>/',views.PostDetail.as_view() , name='post_detail')
]


