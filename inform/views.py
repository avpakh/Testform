# -*- coding: utf-8 -*-
from django.shortcuts import render

#from .forms import ExampleForm
#from .forms import ObjectsListFormHelper
from .forms import Page1Form
from django.shortcuts import get_object_or_404
from utils import PagedFilteredTableView


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render,render_to_response
from .models import TestItem
import json

from simple_rest import Resource

from .models import Part1,Page1
from .models import Part2,Part3,Part4
from .models import EntDbSpr
from table import Table_Ent
from filters import EntDbFilter
from forms import ObjectsListFormHelperFind


# Create your views here.

def get_ent_name(id):  # get name from database for Ent

        #obj_ent = EntDbSpr.objects.select_related().get(gup=id)

        obj_ent = EntDbSpr.objects.filter(id_entdbspr=id).first()

        name = obj_ent.npr

        return name

def get_ent_gup(id):  # get name from database for Ent

        #obj_ent = EntDbSpr.objects.select_related().first().get(gup=id)[:1]

        obj_ent = EntDbSpr.objects.filter(id_entdbspr=id).first()

        gup = obj_ent.gup

        return gup

def get_ent_oku(id):  # get name from database for Ent

        #obj_ent = EntDbSpr.objects.select_related().first().get(gup=id)[:1]

        obj_ent = EntDbSpr.objects.filter(id_entdbspr=id).first()

        oku = obj_ent.oku

        return oku

def get_ent_okp(id):  # get name from database for Ent

        #obj_ent = EntDbSpr.objects.select_related().first().get(gup=id)[:1]

        obj_ent = EntDbSpr.objects.filter(id_entdbspr=id).first()

        okp = obj_ent.okp

        return okp

def get_ent_adr(id):  # get name from database for Ent

        #obj_ent = EntDbSpr.objects.select_related().first().get(gup=id)[:1]

        obj_ent = EntDbSpr.objects.filter(id_entdbspr=id).first()

        adr = obj_ent.adr

        return adr

def get_ent_tel(id):  # get name from database for Ent

        #obj_ent = EntDbSpr.objects.select_related().first().get(gup=id)[:1]

        obj_ent = EntDbSpr.objects.filter(id_entdbspr=id).first()

        tel = obj_ent.tel

        return tel

def  get_id_from(_part1_id1):

        tt = 0

        myrow = Part1.objects.filter(id_part1 = _part1_id1)

        for z in myrow:
            tt = z.id_page1

        #print tt.id_page1

        value1 = tt.id_page1

        return value1

def  get_id_from2(_part1_id2):

        tt2 = 0

        myrow = Part2.objects.filter(id_part2 =_part1_id2)

        for z in myrow:
            tt2 = z.id_page1

        #print tt.id_page1

        value2 = tt2.id_page1

        return value2

def  get_id_from3(_part1_id3):

        tt3 = 0

        myrow = Part3.objects.filter(id_part3 = _part1_id3)

        for z in myrow:
            tt3 = z.id_page1

        value3 = tt3.id_page1

        return value3

def  get_id_from4(_part1_id4):

        tt4 = 0

        myrow = Part4.objects.filter(id_part4=_part1_id4)

        for z in myrow:
            tt4 = z.id_page1

        #print tt.id_page1

        value4 = tt4.id_page1

        return value4


class ReportFindTable(PagedFilteredTableView):
    model = EntDbSpr
    table_class = Table_Ent
    template_name = 'test_find.html'
    paginate_by = 10
    filter_class = EntDbFilter
    formhelper_class =  ObjectsListFormHelperFind
    context_table_name = 'table'  # get error in not avaliable

class ReportFindResult(PagedFilteredTableView):
    model = EntDbSpr
    table_class = Table_Ent
    template_name = 'test_table.html'
    paginate_by = 10
    filter_class = EntDbFilter
    formhelper_class =  ObjectsListFormHelperFind
    context_table_name = 'table'  # get error in not avaliable

class ReportTableViewDetail(PagedFilteredTableView):
    model = EntDbSpr
    table_class = Table_Ent
    template_name = 'test_table.html'
    paginate_by = 10
    filter_class = EntDbFilter
    formhelper_class = ObjectsListFormHelperFind


    def get(self, request, id):

        var_sel=''

        req_name = get_ent_name(id)
        req_gup = get_ent_gup(id)
        req_oku = get_ent_oku(id)
        req_okp = get_ent_okp(id)
        req_adr = get_ent_adr(id)
        req_tel = get_ent_tel(id)

        myobj = Page1.objects.filter(kod_gvk=req_gup).filter(kod_okpo=req_okp).filter(wateruser_name=req_name).count()

        if myobj == 0:
            var_sel = 'selection2'


        if myobj != 0:

            var_sel = 'error'

        return render(request, 'startform.html',
                      {'val_sel': var_sel, 'ent_name': req_name, 'ent_gup': req_gup, 'ent_oku': req_oku,
                       'ent_okp': req_okp, 'ent_adr': req_adr, 'ent_tel': req_tel})


def index_view(request):
    template_name= 'index.html'

    return render(request,template_name)

def get_ecommdata(request):

    list_square = [
        {"square": 0, "key": 0},
        {"square": 1, "key": 1},
        {"square": 4, "key": 2}
    ]
    data = json.dumps(list_square)
    return HttpResponse(data, content_type='application/json')

def part2_view(request,_id_main,_id_razdel):
    template_name = 'page2.html'
    code = []

    return render(request, template_name, {'id_main': _id_main,'id_razdel':_id_razdel})


def part3_view(request,_id_main,_id_razdel):
    template_name = 'page3.html'
    code = []

    return render(request, template_name, {'id_main': _id_main,'id_razdel':_id_razdel})

def part4_view(request,_id_main,_id_razdel):
    template_name = 'page4.html'
    code = []

    return render(request, template_name, {'id_main': _id_main,'id_razdel':_id_razdel})

def part1_view(request,_id_main,_id_razdel):
    template_name = 'page1.html'
    list_square = [
        {"Name": "введите", "Id": 0},
        {"Name": "11", "Id": 1},
        {"Name": "12", "Id": 2},
        {"Name": "13", "Id": 3}
    ]

    code = json.dumps(list_square)
    return render(request, template_name, {'id_main':_id_main,'id_razdel':_id_razdel})

class Clients(Resource):

    def get(self, request,id_razdel,part1_id):

        zz = Page1.objects.get(pk=part1_id)

        print '-id radel',id_razdel

        if zz.razdel1_fill==False:
            clients = Part1.objects.all().filter(id_page1_id=zz).order_by('kod_str')
        if zz.razdel1_fill==True and zz.razdel2_fill==False:
             clients = Part2.objects.all().filter(id_page1_id=zz).order_by('kod_str2')
        if zz.razdel1_fill == True and zz.razdel2_fill == True and zz.razdel3_fill == False:
            clients = Part3.objects.all().filter(id_page1_id=zz).order_by('kod_str3')

        if zz.razdel1_fill == True and zz.razdel2_fill == True and zz.razdel3_fill == True and zz.razdel4_fill == False:
            clients = Part4.objects.all().filter(id_page1_id=zz).order_by('kod_str4')

        return HttpResponse(self.to_json(clients), content_type = 'application/json', status = 200)


    def post(self, request,id_razdel,part1_id):

        zz = Page1.objects.get(pk=part1_id)


        #zz = Page1.objects.latest('id_page1')


        if zz.razdel1_fill == False and  zz.razdel2_fill == False:
            # add record to Part1 database where id_page1=zz and latest
            num_strs = Part1.objects.filter(id_page1=zz)
            nn = num_strs.latest('kod_str')

            Part1.objects.create(
                naim = request.POST.get("naim"),
                location = request.POST.get("location"),
                kod_str = nn.kod_str+1,
                source_kod = request.POST.get("source_kod"),
                kod_basin= request.POST.get("kod_basin"),
                kod_category=request.POST.get("kod_category"),
                param_1= request.POST.get("param_1"),
                param_2= request.POST.get("param_2"),
                param_3= request.POST.get("param_3"),
                kod_wateruser_gvk= request.POST.get("kod_wateruser_gvk"),
                use_total= request.POST.get("use_total"),
                use_tag1= request.POST.get("use_tag1"),
                vol_tag1= request.POST.get("vol_tag1"),
                use_tag2= request.POST.get("use_tag2"),
                vol_tag2 = request.POST.get("vol_tag2"),
                use_tag3 = request.POST.get("use_tag3"),
                vol_tag3 = request.POST.get("vol_tag3"),
                use_tag4 =request.POST.get("use_tag4"),
                vol_tag4 =request.POST.get("vol_tag4"),
                rash_oborot = request.POST.get("rash_oborot"),
                vol_oborot=request.POST.get("vol_oborot"),
                trf_cod_wu1=request.POST.get("trf_cod_wu1"),
                vol_wu1=request.POST.get("vol_wu1"),
                trf_cod_wu2=request.POST.get("trf_cod_wu2"),
                vol_wu2=request.POST.get("vol_wu2"),
                trf_cod_wu3=request.POST.get("trf_cod_wu3"),
                vol_wu3=request.POST.get("vol_wu3"),
                trf_cod_au=request.POST.get("trf_cod_au"),
                vol_au=request.POST.get("vol_au"),
                code_gvk_au=request.POST.get("code_gvk_au"),
                lost_total=request.POST.get("lost_total"),
                lost_transport=request.POST.get("lost_transport"),
                use_bez=request.POST.get("use_bez"),
                id_page1=zz,
             )
            return HttpResponse(status=201)

        if zz.razdel1_fill == True and zz.razdel2_fill == False:

            num_strs = Part2.objects.filter(id_page1=zz)
            nn = num_strs.latest('kod_str2')

            Part2.objects.create(id_page2=zz, kod_str2=nn.kod_str2+1, naim='', location='', outlet_kod=0,
                                 kod_basin2=0, kod_category2=0,
                                 sbros=0, pribor_sbros=0, sbros_without=0, sbros_nogood=0,
                                 sbros_norm=0, kod_wwtp=0, wwtp_project=0, filtration_fields=0, )

            return HttpResponse(status = 201)

        if zz.razdel1_fill == True and zz.razdel2_fill == True  and zz.razdel3_fill == False:
            num_strs = Part3.objects.filter(id_page1=zz)
            nn = num_strs.latest('kod_str3')

            Part3.objects.create(id_page3=zz, kod_str3=nn.kod_str3+1, location_outlet=0,
                                 bod5=0, cod=0,  ssolids=0, mineral=0, sulphate=0,
                                 chloride=0,  phosp_ion=0, totalp=0, nh4=0,no2=0,no3=0, detergents=0,
                                 oil_p=0,fe_tot=0,cr_tot=0,ni=0,cu=0, lead=0, mercury = 0, zink=0, )

            return HttpResponse(status=201)



    def put(self, request,id_razdel,part1_id):

        # zz = get_id_from(part1_id)

        #zz = Page1.objects.latest('id_page1')

        print 'Part-1', part1_id,id_razdel

        if int(id_razdel) == 1:

            zz_id = get_id_from(part1_id)

            zz = Page1.objects.get(pk=zz_id)

            print zz_id,zz

            if zz.razdel1_fill == False:

                print 'update'

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

        if int(id_razdel) == 2:

            print request

            print 'part1_id',part1_id

            zz_id = get_id_from2(part1_id)

            zz = Page1.objects.get(pk=zz_id)

            if zz.razdel1_fill == True and zz.razdel2_fill == False:

                client = Part2.objects.get( pk = part1_id)
                client.naim = request.PUT.get("naim")
                client.location = request.PUT.get("location")
                client.outlet_kod = request.PUT.get("outlet_kod")
                client.kod_basin2 = request.PUT.get("kod_basin2")
                client.kod_category2 = request.PUT.get("kod_category2")
                client.sbros = request.PUT.get("sbros")
                client.pribor_sbros = request.PUT.get("pribor_sbros")
                client.sbros_without = request.PUT.get("sbros_without")
                client.sbros_nogood = request.PUT.get("sbros_nogood")
                client.sbros_norm = request.PUT.get("sbros_norm")
                client.kod_wwtp = request.PUT.get("kod_wwtp")
                client.wwtp_project = request.PUT.get("wwtp_project")
                client.filtration_fields = request.PUT.get("filtration_fields")
                client.save()

                return HttpResponse(status=200)

        if int(id_razdel) == 3:

            zz_id = get_id_from3(part1_id)

            zz = Page1.objects.get(pk=zz_id)

            if zz.razdel1_fill == True and zz.razdel2_fill == True and zz.razdel3_fill == False:



                client = Part3.objects.get(pk = int(part1_id))

                client.location_outlet = request.PUT.get("location_outlet")
                client.bod5 = request.PUT.get("bod5")
                client.cod = request.PUT.get("cod")
                client.ssolids = request.PUT.get("ssolids")
                client.mineral = request.PUT.get("mineral")
                client.sulphate = request.PUT.get("sulphate")
                client.chloride = request.PUT.get("chloride")
                client.phosp_ion = request.PUT.get("phosp_ion")
                client.totalp = request.PUT.get("totalp")
                client.nh4 = request.PUT.get("nh4")
                client.no2 = request.PUT.get("no2")
                client.no3 = request.PUT.get("no2")
                client.detergents = request.PUT.get("detergents")
                client.oil_p = request.PUT.get("oil_p")
                client.fe_tot= request.PUT.get("fe_tot")
                client.cr_tot = request.PUT.get("cr_tot")
                client.ni = request.PUT.get("ni")
                client.cu = request.PUT.get("cu")
                client.lead = request.PUT.get("lead")
                client.mercury = request.PUT.get("mercury")
                client.zink = request.PUT.get("zink")
                client.save()

                return HttpResponse(status=200)


        if int(id_razdel) == 4:

            zz_id = get_id_from4(part1_id)

            zz = Page1.objects.get(pk=zz_id)

            if zz.razdel1_fill == True and zz.razdel2_fill == True and zz.razdel3_fill == True and zz.razdel4_fill == False:
                client = Part4.objects.get(pk=part1_id)
                client.value = request.PUT.get("value")
                client.value_str = request.PUT.get("value_str")
                client.kod_str4 = request.PUT.get("kod_str4")
                client.save()

                return HttpResponse(status=200)

        return HttpResponse(status=200)

    def delete(self, request,id_razdel,part1_id):
        try:
            client = Part1.objects.get(pk = part1_id)
            client.delete()
        except Part1.DoesNotExist:
            try:
                client = Part2.objects.get(pk = part1_id)
                client.delete()
            except Part2.DoesNotExist:
                try:
                    client = Part3.objects.get(pk=part1_id)
                    client.delete()

                finally:
                    return HttpResponse(status = 200)

    def to_json(self, objects):
        return serializers.serialize('json', objects)

def initial_page(request):

    var_sel='no selection'

    if request.method == 'POST':

        if 'radioGroup' in request.POST:

            sel_form =  request.POST['radioGroup']  #get selection

            if sel_form == 'option1':

                var_sel = 'selection1'

                return redirect('/inform/find/')


            if sel_form == 'option2':

                var_sel = 'selection2'

                return render(request, 'startform.html', {'val_sel': var_sel})


    # get from database initial paramaters for filling form


    return render (request, 'startform.html',{'val_sel':var_sel})

def get_from_Part(_r_gup,_r_okp,_r_npr):

    # vobj = get_object_or_404(Page1,kod_gvk=_r_gup,kod_okpo=_r_okp,wateruser_name=_r_npr)

    vv = 0

    gobj = Page1.objects.filter(kod_gvk=_r_gup).filter(kod_okpo=_r_okp).filter(wateruser_name=_r_npr)

    gobj_count = Page1.objects.filter(kod_gvk=_r_gup).filter(kod_okpo=_r_okp).filter(wateruser_name=_r_npr).count()

    if gobj_count == 1:

        for z in gobj:
            vv =z.id_page1

        return vv

    if gobj_count != 1:

        vv = 0

        return vv


def input_page(request):

    num_r1 = 8
    num_r2 = 8
    num_r3 = 8

    r_oku=0
    r_gup=0

    id_main = 0


    if request.method == 'GET':

        num_r1 = request.GET['numRazdel1']

        num_r2 = request.GET['numRazdel2']

        num_r3 = request.GET['numRazdel3']

        r_npr = request.GET['npr']
        r_adr = request.GET['adr']
        r_gup = request.GET['gup']
        r_tel = request.GET['tel']
        r_oku = request.GET['oku']
        r_okp = request.GET['okp']


    if request.method == 'POST':
        #form = ExampleForm(request.POST)

        form = Page1Form(request.POST)


        if 'Razdel1' in request.POST:

            # Checked Razdel 1

            print request.POST

            txt_obj = request.POST['Razdel1']

            tstr_index = txt_obj.find('-',0,len(txt_obj))

            main_str=''

            for k in range(tstr_index+1,len(txt_obj)):
                main_str=main_str+txt_obj[k]


            zz = Page1.objects.get(id_page1=main_str)
            zz.razdel1_fill=True
            zz.razdel2_fill = False
            zz.razdel3_fill = False
            zz.razdel4_fill = False
            zz.save()

            return part2_view(request,int(main_str),2)
        if 'Razdel2' in request.POST:

            txt_obj = request.POST['Razdel2']

            tstr_index = txt_obj.find('-', 0, len(txt_obj))

            main_str = ''

            for k in range(tstr_index + 1, len(txt_obj)):
                main_str = main_str + txt_obj[k]

            # Checked Razdel 2

            zz = Page1.objects.get(id_page1=main_str)
            zz.razdel1_fill = True
            zz.razdel2_fill = True
            zz.razdel3_fill = False
            zz.razdel4_fill = False
            zz.save()

            return part3_view(request, int(main_str),3)

        if 'Razdel3' in request.POST:

            # Checked Razdel 3

            txt_obj = request.POST['Razdel3']

            tstr_index = txt_obj.find('-', 0, len(txt_obj))

            main_str = ''

            for k in range(tstr_index + 1, len(txt_obj)):
                main_str = main_str + txt_obj[k]

            zz = Page1.objects.get(id_page1=main_str)
            zz.razdel1_fill = True
            zz.razdel2_fill = True
            zz.razdel3_fill = True
            zz.razdel4_fill = False
            zz.save()

            return part4_view(request,int(main_str),4)

        if 'Razdel4' in request.POST:


            # Checked Razdel 4

            txt_obj = request.POST['Razdel4']

            tstr_index = txt_obj.find('-', 0, len(txt_obj))

            main_str = ''

            for k in range(tstr_index + 1, len(txt_obj)):
                main_str = main_str + txt_obj[k]

            zz = Page1.objects.get(id_page1=main_str)
            zz.razdel1_fill = True
            zz.razdel2_fill = True
            zz.razdel3_fill = True
            zz.razdel4_fill = True
            zz.save()

            return  index_view(request)

        # Все поля формы были заполнены правильно?
        if form.is_valid():
            # Сохранить новую форму образ в базу данных.


            r_gup = request.GET['gup']
            r_okp = request.GET['okp']
            r_npr = request.GET['npr']


            # check if form in database existing - can be error second attempt


            form.save(commit=True)

            id_main = get_from_Part(r_gup, r_okp, r_npr)

            if id_main !=0:

                zz = Page1.objects.get(pk=id_main) # get id where connected to Page1 (id_page1)

                zz.razdel1_fill = False
                zz.razdel2_fill = False
                zz.razdel3_fill = False
                zz.razdel4_fill = False
                zz.save()



                # create Part1 - fields

                num_r1 = request.GET['numRazdel1']

                num_r2 = request.GET['numRazdel2']

                num_r3 = request.GET['numRazdel3']

                for ind1 in range(int(num_r1)):
                    mstr1 = str(101 + ind1)
                    Part1.objects.create(id_page1=zz,kod_str=mstr1,naim='',location='',source_kod=0, param_1=0,param_2=0,param_3=0,kod_basin=0,kod_category=0,
                                 kod_wateruser_gvk='', use_total=0, use_tag1=0, vol_tag1=0, use_tag2=0,vol_tag2=0,use_tag3=0, vol_tag3=0, use_tag4=0, vol_tag4=0, rash_oborot = 0, vol_oborot = 0,
                                 trf_cod_wu1 =0, vol_wu1= 0, trf_cod_wu2=0, vol_wu2=0,  trf_cod_wu3=0, vol_wu3=0,trf_cod_au=0, vol_au=0, code_gvk_au='', lost_total=0, lost_transport=0,use_bez=0)

                for ind2 in range(int(num_r2)):
                # Create Part2 - fields
                    mstr2 = str(201 + ind2)

                    Part2.objects.create(id_page1=zz, kod_str2=mstr2, naim='', location='', outlet_kod=0,
                                 kod_basin2=0, kod_category2=0,
                                 sbros=0, pribor_sbros=0, sbros_without=0, sbros_nogood=0,
                                 sbros_norm=0, kod_wwtp=0, wwtp_project=0, filtration_fields=0, )
                for ind3 in range(int(num_r3)):
                    # Create Part2 - fields
                    mstr3 = str(301 + ind3)

                    Part3.objects.create(id_page1=zz, kod_str3=mstr3, location_outlet=' ',
                                 bod5=0, cod=0,  ssolids=0, mineral=0, sulphate=0,
                                 chloride=0, phosp_ion=0, totalp=0, nh4=0, no2=0, no3=0, detergents=0,
                                 oil_p=0, fe_tot=0, cr_tot=0, ni=0, cu=0, lead=0, mercury=0, zink=0, )

                Part4.objects.create(id_page1=zz,
                                 kod_str4=401,
                                 value_str='Численность жителей населенных пунктов, подключенных к централизованной системе водоснабжения, человек: ',
                                 value = 0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=402,
                                 value_str='Численность жителей населенных пунктов, подключенных к централизованной системе водоотведения(канализации), человек: ',
                                 value = 0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=403,
                                 value_str='Количество дней работы водопользователя: ',
                                 value = 0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=404,
                                 value_str='Разрешенные объемы добычи подземной воды, тыс. куб. м/год: ',
                                 value=0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=405,
                                 value_str='Разрешенные объемы изъятия поверхностной воды, тыс. куб. м/год: ',
                                 value=0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=406,
                                 value_str='Разрешенные объемы сброса воды в окружающую среду, тыс. куб. м/год: ',
                                 value=0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=407,
                                 value_str='Разрешенные объемы сброса воды в поверхностные водные объекты, тыс. куб. м/год:',
                                 value=0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=408,
                                 value_str='Суммарная проектная мощность водозаборных сооружений для изъятия поверхностной воды, куб.м/сутки: ',
                                 value=0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=409,
                                 value_str=' Суммарная проектная мощность водозаборных сооружений для добычи подземной воды, куб.м/сутки:',
                                 value=0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=410,
                                 value_str=' Количество водозаборных сооружений, предназначенных для изъятия поверхностной воды, единиц',
                                 value=0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=411,
                                 value_str=' Количество приборов учета, установленных на водозаборных сооружениях, предназначенных для изъятия поверхностной воды, единиц',
                                 value=0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=412,
                                 value_str=' Количество водозаборных сооружений (скважин), предназначенных для добычи подземной воды - всего, единиц',
                                 value=0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=413,
                                 value_str=' Количество водозаборных сооружений (скважин), предназначенных для добычи подземной воды - ликвдировано, единиц:',
                                 value=0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=414,
                                 value_str=' Количество водозаборных сооружений (скважин), предназначенных для добычи подземной воды - законсервировано, единиц:',
                                 value=0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=415,
                                 value_str=' Количество приборов учета, установленных на водозаборных сооружениях, предназначенных для добычи подземной воды, единиц',
                                 value=0,
                                 )
                Part4.objects.create(id_page1=zz,
                                 kod_str4=416,
                                 value_str=' Количество приборов учета, установленных на очистных сооружениях, единиц',
                                 value=0,
                                 )

                # Теперь вызвать предсталвение index().
                # Пользователю будет показана следующая страница
                return part1_view(request,id_main,1)
        else:
            # Обрабатываемая форма содержит ошибки - вывести их в терминал.
            print form.errors
    else:
        # Если запрос был не POST, вывести форму, чтобы можно было ввести в неё данные.

        form = Page1Form(initial={'kod_okpo': r_okp, 'kod_unn': r_oku, 'kod_gvk': r_gup, 'wateruser_name': r_npr,
                                  'postal_address': r_adr, 'territory_level': ' н.д. ',
                                  'wateruser_level_name': ' н.д. ', 'email_address': '1@1.by'})


    # Форма с ошибкой (или ошибка с данных), форма не была получена...
    # Вывести форму с сообщениями об ошибках (если они были).

    return render (request, 'inputform.html', {'form': form})