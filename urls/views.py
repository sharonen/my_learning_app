from django.shortcuts import render, get_object_or_404

from . import models


def urls_list(request):
    urls = models.Url.objects.all()
    return render(request, 'urls/urls_list.html', {'urls': urls})


def urls_detail(request, pk):
    url = get_object_or_404(models.Url, pk=pk)
    return render(request, 'urls/url_detail.html', {'urls': urls})
