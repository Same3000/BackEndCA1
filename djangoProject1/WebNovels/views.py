from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views import generic
from .models import *


class NovelFrom(ModelForm):
    class Meta:
        model = WebNovels
        fields = ['name', 'price', 'author', 'status', 'length', 'tags', 'views']


def create_webnovels(request):
    context = {}
    form = NovelFrom(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("webnovels/")
    context['form'] = form
    return render(request, "WebNovels/form.html", context)


def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = WebNovels.objects.get(id=id)

    return render(request, "WebNovels/detail_view.html", context)


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(WebNovels, id=id)

    # pass the object as instance in form
    form = NovelFrom(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "WebNovels/update_detail.html", context)


def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(WebNovels, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "WebNovels/delete_view.html", context)


class Index(generic.ListView):
    model = WebNovels
    template_name = 'WebNovels/home.html'
    context_object_name = "books"

    def get_queryset(self):
        return WebNovels.objects.all()
