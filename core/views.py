from django.shortcuts import render
from chips import models as chip_models


def homeRender(request):

    chipList = chip_models.Chips.objects.all()

    return render(request, "screens/home.html", context={"chipList": chipList})
