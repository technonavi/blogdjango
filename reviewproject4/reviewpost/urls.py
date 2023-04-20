from django.contrib import admin
from django.urls import path
from .views import signview,loginview,sampleview,listview,detailview,CreateClass,logoutview,evaluationview,Delete,download
from .views import categoryview,indexview,categorydetailview,Formview,form_upload,form_upload_list,form_upload_detailview
urlpatterns =[
    path("admin/",admin.site.urls),
    path("signup/",signview,name="signup"),
    path("login/",loginview,name='login'),
    path("sample/",sampleview),
    path("list/",listview,name='list'),
    path("detail/<int:pk>/",detailview,name='detail'),
    path("create/",CreateClass.as_view(),name='create'),
    path("logout/",logoutview,name='logout'),
    path("evaluation/<int:pk>",evaluationview,name='evaluation'),
    path("delete/<int:pk>",Delete.as_view(),name="delete"),
    path("category/<int:pk>",categorydetailview,name="categorydetail"),
    path("category/",categoryview,name="category"),
    path("index",indexview,name="index"),
    path('form/', Formview.as_view(),name="formpage"),
    path('uploadcreate/',form_upload,name="upload"),
    path('uploadlist/',form_upload_list,name="uploadlist"),
    path('uploaddetail/<int:pk>',form_upload_detailview,name="uploaddetail"),
    path('download/<int:pk>',download,name="download"),

    ]
