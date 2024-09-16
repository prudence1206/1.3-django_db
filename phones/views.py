from django.shortcuts import render, redirect
from phones.models import Phone
from django.http import HttpResponse


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)


def s1(request):
    car_objects = Phone.objects.all()
    print(car_objects)
    cars = [f'{c.id}: {c.name}, {c.image}: {c.price}: {c.slug}' for c in car_objects]
    return HttpResponse(cars)

