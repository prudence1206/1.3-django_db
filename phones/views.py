from django.shortcuts import render, redirect
from phones.models import Phone
from django.http import HttpResponse


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    all_phones = Phone.objects.all()
    context = {'phones':all_phones}
    print(context['phones'])
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter()
    context = {'phones':Phone.objects.filter()}
    return render(request, template, context)


def s1(request):
    car_objects = Phone.objects.all()
    print(car_objects)
    cars = [f'{c.id}: {c.name}, {c.image}: {c.price}: {c.slug}' for c in car_objects]
    return HttpResponse(cars)
def s2(request):
    context = {"query_results":Phone.objects.all()}
    template = 's2t.html'
    return render(request, template, context=context)