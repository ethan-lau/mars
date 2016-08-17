from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from crawl.models import Crawl, PageReference
from crawl.serializers import CrawlSerializer, PageReferenceSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def crawl_list(request):
    if request.method == 'GET':
        crawl = Crawl.objects.all()
        serializer = CrawlSerializer(crawl, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CrawlSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def crawl_detail(request, pk):
    try:
        crawl = Crawl.objects.get(pk=pk)
    except Crawl.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CrawlSerializer(crawl)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CrawlSerializer(crawl, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=404)
    elif request.method == 'DELETE':
        crawl.delete()
        return HttpResponse(status=204)


@csrf_exempt
def page_reference(request):
    if request.method == 'GET':
        page = PageReference.objects.all()
        p = Paginator(page, 10)
        serializer = PageReferenceSerializer(p.page(1), many=True)
        return JSONResponse(serializer.data)
