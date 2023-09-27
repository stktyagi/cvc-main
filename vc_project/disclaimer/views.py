from django.shortcuts import render

from django.http import HttpResponse


def disclaimer (request):
    return render(request, 'disclaimer.html')
