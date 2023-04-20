from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from .models import ReviewModel,Category,FileModel
from django.views.generic import CreateView,DeleteView,ListView,TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from . import forms
import csv
import io
import mimetypes
import shutil
# Create your views here.
def signview(request):
    if request.method =='POST':
     print('POST.method')
     password_data=request.POST['password_data']
     username_data=request.POST['username_data']
     try:
      user =User.objects.create_user(username_data,'',password_data)
     except IntegrityError:
      return render(request,'signup.html',{'error':'このユーザーは既に登録されています。'})
    else:
     print(User.objects.all())
     print()
     return render(request,'signup.html',{})
    return render(request,'signup.html',{})
def loginview(request):
    if request.method=='POST':
     username_data=request.POST['username_data']
     password_data=request.POST['password_data']
     user=authenticate(request,username=username_data,password=password_data)
     if user is not None:
      login(request,user)
      return redirect('list')
     else:
      return redirect('login')
    return render(request,'login.html',{'error':'IDとパスワードが間違っています。'})
def sampleview(request):
    if request.method=='POST':
     return redirect('login')
    else:
     return render(request,'login.html',{})
def listview(request):
    object_list = ReviewModel.objects.all()
    category_list=Category.objects.all()
    print(object_list)
    return render(request ,'list.html',{'object_list':object_list})
def categoryview(request):
 category =Category.objects.all()
 return render(request ,'category.html',({'category':category}))
def categorydetailview(request,pk):
    category_list=ReviewModel.objects.filter(category=pk).all()
    object_list=ReviewModel.objects.all()
    print(category_list)
    return render(request ,'categorydetail.html',({'category_list':category_list}))
def indexview(request):
    if request.method=="POST":
     index_data=request.POST["index_value"]
     print(index_data)
     print("POST")
    search_list=ReviewModel.objects.filter(title__contains=index_data).all()
    print(search_list)
    return render(request ,'search.html',({'search_list':search_list}))


def detailview(request,pk):
 object =ReviewModel.objects.get(pk=pk)
 return render(request,'detail.html',{'object':object})
class CreateClass(CreateView):
 template_name="create.html"
 model=ReviewModel
 fields=('title','content','images','evaluation','category','useful_review')
 success_url=reverse_lazy("list")
class Delete(DeleteView):
 template_name="delete.html"
 model=ReviewModel
 success_url=reverse_lazy("list")
class searchresultview(ListView):
 template_name="searchresult.html"

def logoutview(request):
    logout(request)
    return redirect('login')

def evaluationview(request,pk):
 post =ReviewModel.objects.get(pk=pk)
 author_name=request.user.get_username()+str(request.user.id)
 if author_name in post.useful_review_record:
  return redirect('list')
 else:
  post.useful_review = post.useful_review+1
  post.useful_review_record = post.useful_review_record+author_name
  post.save()
  return redirect('list')
class Formview(TemplateView):



    # 初期変数定義
    def __init__(self):
        self.params = {"Message":"情報を入力してください。",
                       "form":forms.IndexForm(),
                       }


    # GET時の処理を記載
    def get(self,request):
        return render(request, "formpage.html",context=self.params)

    # POST時の処理を記載
    def post(self,request):
        if request.method == "POST":
            self.params["form"] = forms.IndexForm(request.POST)
            
            # フォーム入力が有効な場合
            if self.params["form"].is_valid():
                self.params["Message"] = "入力情報が送信されました。"

        return render(request, "formpage.html",context=self.params)

def form_upload(request):
 if request.method == 'POST':
  form = forms.UploadForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
  return redirect('uploadlist')
 else:
  form = forms.UploadForm()
  return render(request, 'upload.html', {'form': form})
def form_upload_list(request):
    form_upload_list= FileModel.objects.all()
    return render(request ,'uploadlist.html',{'form_upload_list':form_upload_list})
def form_upload_detailview(request,pk):
 object =FileModel.objects.get(pk=pk)
 return render(request,'uploaddetail.html',{'object':object})

def download(request, pk):
    upload_file = get_object_or_404(FileModel, pk=pk)
    file = upload_file.uploadplace  # ファイル本体
    name = upload_file.title # ファイル名
    object =FileModel.objects.get(pk=pk)
    # ファイル名からmimetypeを推測。拡張子がないファイル等は、application/octet-stream
    response = HttpResponse()
    response = HttpResponse(content_type=mimetypes.guess_type(name)[0] or 'application/octet-stream')
    # Content-Dispositionでダウンロードの強制
    response['Content-Disposition'] = f'attachment; filename={name}'

    # HttpResponseに、ファイルの内容を書き込む
    shutil.copyfileobj(file, response)
    return response

 
