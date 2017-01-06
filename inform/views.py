# -*- coding: utf-8 -*-
from django.shortcuts import render

from .forms import ExampleForm
from .forms import ObjectsListFormHelper
from .forms import Page1Form


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from .models import TestItem
import json

from simple_rest import Resource

from .models import Part1,Page1


# Create your views here.
def index_view(request):
    template_name= 'index.html'

    return render(request,template_name)



def get_ecommdata(request):
    print "inside get_ecommdata"
    list_square = [
        {"square": 0, "key": 0},
        {"square": 1, "key": 1},
        {"square": 4, "key": 2}
    ]
    data = json.dumps(list_square)
    return HttpResponse(data, content_type='application/json')

def part1_view(request):
    template_name = 'page1.html'
    list_square = [
        {"Name": "введите", "Id": 0},
        {"Name": "11", "Id": 1},
        {"Name": "12", "Id": 2},
        {"Name": "13", "Id": 3}
    ]

    code = json.dumps(list_square)
    return render(request, template_name, {'source_code': code})

class Clients(Resource):

    def get(self, request):
        clients = Part1.objects.all().order_by('kod_str')
        return HttpResponse(self.to_json(clients), content_type = 'application/json', status = 200)

    def post(self, request):
        zz = Page1.objects.latest('id_page1')

        # add record to Part1 database where id_page1=zz and latest
        num_strs = Part1.objects.filter(id_page1=zz)
        nn = num_strs.latest('kod_str')

        Part1.objects.create(
            naim = '',
            location = '',
            kod_str = nn.kod_str+1,
            source_kod = 0,
            kod_basin=0,
            kod_category=0,
            param_1=0,
            param_2=0,
            param_3=0,
            kod_wateruser_gvk='', use_total=0, use_tag1=0, vol_tag1=0, use_tag2=0, vol_tag2=0, use_tag3=0,
            vol_tag3=0, use_tag4=0, vol_tag4=0, rash_oborot=0, vol_oborot=0, trf_cod_wu1=0, vol_wu1=0, trf_cod_wu2=0, vol_wu2=0, trf_cod_wu3=0, vol_wu3=0, trf_cod_au=0, vol_au=0,
            code_gvk_au='', lost_total=0, lost_transport=0, use_bez=0,
            id_page1=zz,
        )
        return HttpResponse(status = 201)

    def put(self, request, part1_id):
        client = Part1.objects.get(pk = part1_id)
        client.naim = request.PUT.get("naim")
        client.location = request.PUT.get("location")
        client.kod_str = request.PUT.get("kod_str")
        client.source_kod = request.POST.get("source_kod")
        client.kod_basin = request.POST.get("kod_basin")
        client.kod_category = request.POST.get("kod_category")
        client.param_1 = request.POST.get("param_1")
        client.param_2 = request.POST.get("param_2")
        client.param_3 = request.POST.get("param_3")
        client.kod_wateruser_gvk = request.POST.get("kod_wateruser_gvk")
        client.use_total = request.POST.get("use_total")
        client.use_tag1 = request.POST.get("use_tag1")
        client.use_tag2 = request.POST.get("use_tag2")
        client.use_tag3 = request.POST.get("use_tag3")
        client.use_tag4 = request.POST.get("use_tag4")
        client.vol_tag1 = request.POST.get("vol_tag1")
        client.vol_tag2 = request.POST.get("vol_tag2")
        client.vol_tag3 = request.POST.get("vol_tag3")
        client.vol_tag4 = request.POST.get("vol_tag4")
        client.rash_oborot = request.POST.get("rash_oborot")
        client.vol_oborot = request.POST.get("vol_oborot")
        client.trf_cod_wu1 = request.POST.get("trf_cod_wu1")
        client.trf_cod_wu2 = request.POST.get("trf_cod_wu2")
        client.trf_cod_wu3 = request.POST.get("trf_cod_wu3")
        client.vol_wu1 = request.POST.get("vol_wu1")
        client.vol_wu2 = request.POST.get("vol_wu2")
        client.vol_wu3 = request.POST.get("vol_wu3")
        client.trf_cod_au = request.POST.get("trf_cod_au")
        client.vol_au = request.POST.get("vol_au")
        client.code_gvk_au = request.POST.get("code_gvk_au")
        client.lost_total = request.POST.get("lost_total")
        client.lost_transport = request.POST.get("lost_transport")
        client.use_bez = request.POST.get("use_bez")

        client.save()
        return HttpResponse(status = 200)

    def delete(self, request, part1_id):
        print part1_id
        client = Part1.objects.get(pk = part1_id)
        client.delete()
        return HttpResponse(status = 200)

    def to_json(self, objects):
        return serializers.serialize('json', objects)


def input_page(request):

    if request.method == 'POST':
        #form = ExampleForm(request.POST)
        form = Page1Form(request.POST)

        # Все поля формы были заполнены правильно?
        if form.is_valid():
            # Сохранить новую категорию в базе данных.
            form.save(commit=True)
            zz = Page1.objects.latest('id_page1')
            Part1.objects.create(id_page1=zz,kod_str=101,naim='',location='',source_kod=0, param_1=0,param_2=0,param_3=0,kod_basin=0,kod_category=0,
                                 kod_wateruser_gvk='', use_total=0, use_tag1=0, vol_tag1=0, use_tag2=0,vol_tag2=0,use_tag3=0, vol_tag3=0, use_tag4=0, vol_tag4=0, rash_oborot = 0, vol_oborot = 0,
                                 trf_cod_wu1 =0, vol_wu1= 0, trf_cod_wu2=0, vol_wu2=0,  trf_cod_wu3=0, vol_wu3=0,trf_cod_au=0, vol_au=0, code_gvk_au='', lost_total=0, lost_transport=0,use_bez=0)
            Part1.objects.create(id_page1=zz,kod_str=102,naim='',location='',source_kod=0, param_1=0,param_2=0,param_3=0,kod_basin=0,kod_category=0,
                                 kod_wateruser_gvk='', use_total=0, use_tag1=0, vol_tag1=0, use_tag2=0,vol_tag2=0,use_tag3=0, vol_tag3=0, use_tag4=0, vol_tag4=0, rash_oborot = 0, vol_oborot = 0,
                                 trf_cod_wu1 =0, vol_wu1= 0, trf_cod_wu2=0, vol_wu2=0,  trf_cod_wu3=0, vol_wu3=0,trf_cod_au=0, vol_au=0, code_gvk_au='', lost_total=0, lost_transport=0,use_bez=0)
            Part1.objects.create(id_page1=zz,kod_str=103,naim='',location='',source_kod=0, param_1=0,param_2=0,param_3=0,kod_basin=0,kod_category=0,
                                 kod_wateruser_gvk='', use_total=0, use_tag1=0, vol_tag1=0, use_tag2=0,vol_tag2=0,use_tag3=0, vol_tag3=0, use_tag4=0, vol_tag4=0, rash_oborot = 0, vol_oborot = 0,
                                 trf_cod_wu1 =0, vol_wu1= 0, trf_cod_wu2=0, vol_wu2=0,  trf_cod_wu3=0, vol_wu3=0,trf_cod_au=0, vol_au=0, code_gvk_au='', lost_total=0, lost_transport=0,use_bez=0)
            Part1.objects.create(id_page1=zz,kod_str=104,naim='',location='',source_kod=0, param_1=0,param_2=0,param_3=0,kod_basin=0,kod_category=0,
                                 kod_wateruser_gvk='', use_total=0, use_tag1=0, vol_tag1=0, use_tag2=0,vol_tag2=0,use_tag3=0, vol_tag3=0, use_tag4=0, vol_tag4=0, rash_oborot = 0, vol_oborot = 0,
                                 trf_cod_wu1 =0, vol_wu1= 0, trf_cod_wu2=0, vol_wu2=0,  trf_cod_wu3=0, vol_wu3=0,trf_cod_au=0, vol_au=0, code_gvk_au='', lost_total=0, lost_transport=0,use_bez=0)
            Part1.objects.create(id_page1=zz,kod_str=105,naim='',location='',source_kod=0, param_1=0,param_2=0,param_3=0,kod_basin=0,kod_category=0,
                                 kod_wateruser_gvk='', use_total=0, use_tag1=0, vol_tag1=0, use_tag2=0,vol_tag2=0,use_tag3=0, vol_tag3=0, use_tag4=0, vol_tag4=0, rash_oborot = 0, vol_oborot = 0,
                                 trf_cod_wu1 =0, vol_wu1= 0, trf_cod_wu2=0, vol_wu2=0,  trf_cod_wu3=0, vol_wu3=0,trf_cod_au=0, vol_au=0, code_gvk_au='', lost_total=0, lost_transport=0,use_bez=0)
            Part1.objects.create(id_page1=zz,kod_str=106,naim='',location='',source_kod=0, param_1=0,param_2=0,param_3=0,kod_basin=0,kod_category=0,
                                 kod_wateruser_gvk='', use_total=0, use_tag1=0, vol_tag1=0, use_tag2=0,vol_tag2=0,use_tag3=0, vol_tag3=0, use_tag4=0, vol_tag4=0, rash_oborot = 0, vol_oborot = 0,
                                 trf_cod_wu1=0, vol_wu1= 0, trf_cod_wu2=0, vol_wu2=0,  trf_cod_wu3=0, vol_wu3=0,trf_cod_au=0, vol_au=0, code_gvk_au='', lost_total=0, lost_transport=0,use_bez=0)
            Part1.objects.create(id_page1=zz,kod_str=107,naim='',location='',source_kod=0, param_1=0,param_2=0,param_3=0,kod_basin=0,kod_category=0,
                                 kod_wateruser_gvk='', use_total=0, use_tag1=0, vol_tag1=0, use_tag2=0,vol_tag2=0,use_tag3=0, vol_tag3=0, use_tag4=0, vol_tag4=0, rash_oborot = 0, vol_oborot = 0,
                                 trf_cod_wu1=0, vol_wu1= 0, trf_cod_wu2=0, vol_wu2=0,  trf_cod_wu3=0, vol_wu3=0,trf_cod_au=0, vol_au=0, code_gvk_au='', lost_total=0, lost_transport=0,use_bez=0)
            Part1.objects.create(id_page1=zz,kod_str=108,naim='',location='',source_kod=0, param_1=0,param_2=0,param_3=0,kod_basin=0,kod_category=0,
                                 kod_wateruser_gvk='', use_total=0, use_tag1=0, vol_tag1=0, use_tag2=0,vol_tag2=0,use_tag3=0, vol_tag3=0, use_tag4=0, vol_tag4=0, rash_oborot = 0, vol_oborot = 0,
                                 trf_cod_wu1=0, vol_wu1= 0, trf_cod_wu2=0, vol_wu2=0,  trf_cod_wu3=0, vol_wu3=0,trf_cod_au=0, vol_au=0, code_gvk_au='', lost_total=0, lost_transport=0,use_bez=0)

            # Теперь вызвать предсталвение index().
            # Пользователю будет показана следующая страница
            return part1_view(request)
        else:
            # Обрабатываемая форма содержит ошибки - вывести их в терминал.
            print form.errors
    else:
        # Если запрос был не POST, вывести форму, чтобы можно было ввести в неё данные.
        form = Page1Form()


    # Форма с ошибкой (или ошибка с данных), форма не была получена...
    # Вывести форму с сообщениями об ошибках (если они были).

    return render (request, 'inputform.html', {'form': form})