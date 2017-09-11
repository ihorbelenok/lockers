# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Locker
from .serializers import LockerSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# Create your views here.

@login_required
def lockers_display(request):
    returnData = {}
    returnData["lockers"] = Locker.objects.all()
    return render(request, "lockers.html", returnData)

@login_required
def lockers_list(request):
    if request.method == 'GET':
        lockers = Locker.objects.all()
        serializer = LockerSerializer(lockers, many=True)
        return JsonResponse({"data":serializer.data}, safe=False)

@login_required
def lockers_add(request):
    if request.method == "POST":
        # for i in request.POST:
        #     print i, request.POST.get(i)

        if Locker.objects.filter(number=request.POST.get('number')).exists():
            return JsonResponse({"success": False, "error_message": "Шафа з таким номером вже існує"})
        else:
            try:
                new_locker = Locker()
                new_locker.number = request.POST.get('number')
                new_locker.code = request.POST.get('code')
                new_locker.kid = request.POST.get('kid')
                new_locker.kid_class = request.POST.get('kid_class')
                new_locker.address = request.POST.get('address')
                new_locker.phone = request.POST.get('phone')
                new_locker.save()
            except Exception:
                return JsonResponse({"success": False, "error_message": "Помилка при збереженні #001. Будь-ласка, перезагрузіть сторінку і спробуйте ще раз"})
            else:
                return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False, "error_message": "Помилка доступу до сервісу #002. Зверніться до адміністратора для вирішення проблеми"})


@login_required
def lockers_edit(request):
    if request.method == "POST":
        # for i in request.POST:
        #     print i, request.POST.get(i)

        if Locker.objects.filter(pk = request.POST.get('pk')).count() == 1:
            if Locker.objects.filter(number=request.POST.get('number')).exists():
                if (Locker.objects.get(number=request.POST.get('number')) == Locker.objects.get(pk = request.POST.get('pk'))):
                    try:
                        new_locker = Locker.objects.get(pk=request.POST.get('pk'))
                        new_locker.number = request.POST.get('number')
                        new_locker.code = request.POST.get('code')
                        new_locker.kid = request.POST.get('kid')
                        new_locker.kid_class = request.POST.get('kid_class')
                        new_locker.address = request.POST.get('address')
                        new_locker.phone = request.POST.get('phone')
                        new_locker.save()
                    except Exception:
                        return JsonResponse({"success": False,
                                             "error_message": "Помилка при збереженні #003. Будь-ласка, перезагрузіть сторінку і спробуйте ще раз"})
                    else:
                        return JsonResponse({"success": True})
                else:
                    return JsonResponse({"success": False, "error_message": "Шафа з таким номером вже існує"})
            else:
                try:
                    new_locker = Locker.objects.get(pk = request.POST.get('pk'))
                    new_locker.number = request.POST.get('number')
                    new_locker.code = request.POST.get('code')
                    new_locker.kid = request.POST.get('kid')
                    new_locker.kid_class = request.POST.get('kid_class')
                    new_locker.address = request.POST.get('address')
                    new_locker.phone = request.POST.get('phone')
                    new_locker.save()
                except Exception:
                    return JsonResponse({"success": False,
                                         "error_message": "Помилка при збереженні #004. Будь-ласка, перезагрузіть сторінку і спробуйте ще раз"})
                else:
                    return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error_message": "Помилка при збереженні #005. Будь-ласка, перезагрузіть сторінку і спробуйте ще раз"})
    else:
        return JsonResponse({"success": False, "error_message": "Помилка доступу до сервісу #006. Зверніться до адміністратора для вирішення проблеми"})

@login_required
def lockers_remove(request):
    if request.method == "POST":
        # for i in request.POST:
        #     print i, request.POST.get(i)

        if Locker.objects.filter(pk = request.POST.get('pk')).count() == 1:
            try:
                locker = Locker.objects.get(pk=request.POST.get('pk'))
                locker.delete()
            except Exception:
                return JsonResponse({"success": False, "error_message": "Помилка при збереженні #007. Будь-ласка, перезагрузіть сторінку і спробуйте ще раз"})
            else:
                return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error_message": "Помилка при збереженні #008. Будь-ласка, перезагрузіть сторінку і спробуйте ще раз"})
    else:
        return JsonResponse({"success": False, "error_message": "Помилка доступу до сервісу #009. Зверніться до адміністратора для вирішення проблеми"})