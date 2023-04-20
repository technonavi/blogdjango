from django import forms
from .models import FileModel
class IndexForm(forms.Form):
    Name = forms.CharField(label="名前")                    
    Tell = forms.IntegerField(label="電話番号")
    Mail = forms.EmailField(label="メールアドレス")
    Birthday = forms.DateField(label="生年月日")
    Website = forms.URLField(label="Webサイト")
    FreeText = forms.CharField(widget=forms.Textarea,label="備考")

class UploadForm(forms.ModelForm):
 class Meta:
  model = FileModel
  fields = ('title', 'uploadplace')