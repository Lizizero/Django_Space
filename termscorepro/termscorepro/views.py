from django.forms import ModelForm
from .models import score
from django import forms
from django.shortcuts import render
from django.forms import ValidationError


def validate_score(value):
    if int(value) < 0:
        raise ValidationError('成绩不能小于0分')
    if int(value) > 100:
        raise ValidationError('成绩不能大于100分')


class scoreForm(ModelForm):
    python = forms.IntegerField(validators=[validate_score], help_text='输入1-100整数')
    js = forms.IntegerField(validators=[validate_score], help_text='整数1-100，OK！')

    class Meta:
        model = score
        fields = {'name', 'python', 'js'}
        labels = {'name': '姓名'}
        help_texts = {'name': '姓名为中文字符'}


def usescoreForm(request):
    if request.method == 'POST':
        form = scoreForm(request.POST)
        if form.is_valid():
            ps = score.objects.filter(name=request.POST['name'])
            if ps.count() == 0:
                form.save()
                msg = '成绩录入成功'
            else:
                msg = '已存在相同name，请勿重复提交'
        else:
            msg = '输入的数据有误'
    else:
        form = scoreForm()
        msg = '请输入数据'
    form.order_fields(['name', 'python', 'js'])
    return render(request, 'temscore.html', {'form': form, 'msg': msg})
