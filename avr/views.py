import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from avr.models import AVRIndex


def index(request):
    return render(request, 'avr/index.html')


def results(request):
    return render(request, 'avr/results.html')


@require_POST
def getListBrands(request):
    save_info = json.loads(request.POST.get('saveInfo'))
    print(save_info)
    end_text_for_name = "для схем на контакторах"
    if save_info['powerUnit'] == "автоматические выключатели":
        end_text_for_name = "для схем на авт. выкл."
    list_brands = AVRIndex.objects.filter(avr_scheme=save_info['avrScheme'], name__endswith=end_text_for_name)\
        .values_list('power_devices_brand')
    list_brands = list(set([x for x, in list_brands]))
    list_brands.sort()
    print(list_brands)
    return JsonResponse(['ABB', 'Eaton', 'Delta', 'Relpol'], safe=False)


# function returnListBrands(enteredInfo) {
#   if (enteredInfo.avrScheme != '' && enteredInfo.powerUnit != '' && enteredInfo.plcSupplyVoltage != '') {
#     var end_text_for_name = "для схем на контакторах";
#
#     if (enteredInfo.powerUnit == "автоматические выключатели") {
#       end_text_for_name = "для схем на авт. выкл.";
#     }
#
#     var list_brands = [];
#     var data = ws_datafile.getDataRange().getValues();
#
#     for (let i = 1; i < data.length; i++) {
#       if (data[i][0] == enteredInfo.avrScheme && data[i][2].endsWith(end_text_for_name)) {
#         list_brands.push(data[i][3]);
#       }
#     }
#
#     list_brands = unique(list_brands).sort();
#     return list_brands;
#   }
# }


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
