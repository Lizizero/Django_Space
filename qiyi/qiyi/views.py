from django.forms import ModelForm
from .models import Score
from django import forms
from django.shortcuts import render
from django.forms import ValidationError


def validate_score(value):
    if int(value) < 0:
        raise ValidationError('Score must be between 0 and',code='min_value')
    if int(value) > 100:
        raise ValidationError('Score must be greater than 100',code='max_value')


class ScoreForm(ModelForm):
    python = forms.IntegerField(validators=[validate_score], help_text='1-100!')
    json = forms.IntegerField(validators=[validate_score], help_text='1-100!')

    class Meta:
        model = Score
        fields = {'name', 'python', 'json'}
        labels = {'name': '姓名'}
        help_texts = {'name': '姓名为中文字符'}


def useScoreForm(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            ps = Score.objects.filter(name=request.POST['name'])
            if ps.count() == 0:
                form.save()
                msg = '录入成功'
            else:
                msg = '已存在'
        else:
            msg = '有误'
    else:
        form = ScoreForm()
        msg = '请输入数据'
    form.order_fields(['name', 'python', 'json'])
    return render(request, 'qiyiscore.html', {'form': form, 'msg': msg})
