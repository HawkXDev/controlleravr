import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from avr.models import AVRIndex

global_n = None


def index(request):
    global global_n
    global_n = [80, 125]
    if global_n:
        n = global_n
        global_n = None
        print(f'{n = }')
        article1, article2 = get_articles(n)
        return render(request, 'avr/results.html', {'article1': article1, 'article2': article2})
    else:
        return render(request, 'avr/index.html')


def get_articles(n):
    article1 = AVRIndex.objects.filter(id=n[0])[0]
    article2 = AVRIndex.objects.filter(id=n[1])[0]
    return article1, article2


@require_POST
def getListBrands(request):
    save_info = json.loads(request.POST.get('saveInfo'))
    list_brands = []
    if save_info['avrScheme'] and save_info['powerUnit'] and save_info['plcSupplyVoltage']:
        end_text_for_name = "для схем на авт. выкл." \
            if save_info['powerUnit'] == "автоматические выключатели" \
            else "для схем на контакторах"
        list_brands = AVRIndex.objects.filter(avr_scheme=save_info['avrScheme'], name__endswith=end_text_for_name)\
            .values_list('power_devices_brand', flat=True).distinct().order_by('power_devices_brand')
        list_brands = list(list_brands)
    return JsonResponse(list_brands, safe=False)


@require_POST
def getListTypes(request):
    save_info = json.loads(request.POST.get('saveInfo'))
    list_types = []
    if save_info['avrScheme'] and save_info['powerUnit'] and save_info['plcSupplyVoltage'] and save_info['manufacturer']:
        end_text_for_name = "для схем на авт. выкл." \
            if save_info['powerUnit'] == "автоматические выключатели" \
            else "для схем на контакторах"
        list_types = AVRIndex.objects.filter(avr_scheme=save_info['avrScheme'], name__endswith=end_text_for_name,
                                             power_devices_brand=save_info['manufacturer']) \
            .values_list('power_devices_type', flat=True).distinct().order_by('power_devices_type')
        list_types = list(list_types)
    return JsonResponse(list_types, safe=False)


@require_POST
def getChooseResult(request):
    save_info = json.loads(request.POST.get('saveInfo'))
    end_text_for_name = "для схем на авт. выкл." \
        if save_info['powerUnit'] == "автоматические выключатели" \
        else "для схем на контакторах"
    chooseIds = AVRIndex.objects.filter(avr_scheme=save_info['avrScheme'], name__endswith=end_text_for_name,
                                        power_devices_brand=save_info['manufacturer'],
                                        power_devices_type=save_info['typeDevice']) \
        .values_list('id', flat=True)
    chooseIds = list(chooseIds)
    global global_n
    global_n = chooseIds
    return JsonResponse(chooseIds, safe=False)


@require_POST
def logs(request):
    log_number = request.POST.get('log_number')
    v = request.POST.get('v')
    t = request.POST.get('t')
    print(log_number)
    print(v)
    print(t)
    return HttpResponse('')


@require_POST
@csrf_exempt
def avradmin(request):
    postdata = {k: v[0] if len(v) == 1 else v for k, v in request.POST.lists()}
    AVRIndex.objects.create(
        avr_scheme=postdata['Схема АВР'], article=postdata['Артикул'],
        name=postdata['Наименование'], power_devices_brand=postdata['Бренд силовых аппаратов'],
        power_devices_type=postdata['Тип аппарата (привода)'],
        spring_time=postdata['Время взвода пружины'] if postdata['Время взвода пружины'] != 'nan' else None,
        plc=postdata['Контроллер'],
        extension_module=postdata['Модуль расширения'] if postdata['Модуль расширения'] != 'nan' else None,
        specification=postdata['Спецификация'],
        documentation=postdata['Документация'] if postdata['Документация'] != 'nan' else None,
        specification_link=postdata['Спецификация.1'], xlsx_export_link=postdata['Xlsx export'],
        pdf_avr_link=postdata['Pdf avr'], pdf_scheme_link=postdata['Pdf schema'], zip_link=postdata['Zip'],
        xlsx_link=postdata['Xlsx'],
        status=postdata['STATUS'] if postdata['STATUS'].strip() != '' else None
    )
    return JsonResponse({'result': True})
