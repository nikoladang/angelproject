from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
import random, string, json
from .models import Urls
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings

def index(request):
    # c = {}
    # c.update(csrf(request))
    # return render_to_response('shortenersite/index.html', c)
    pass

def redirect_original(request, short_id):
    # https://docs.djangoproject.com/en/1.10/ref/request-response/
    user_ip = request.META.get('REMOTE_ADDR')
    print(user_ip)
    print(short_id)
    url = get_object_or_404(Urls, pk=short_id) # get object, if not        found return 404 error
    url.views_total += 1
    print(url.original_url)
    print(request.META)
    url.save()
    return HttpResponseRedirect(url.original_url)

# def redirect_original(request):
#     url = get_object_or_404(Urls, pk="aaaa") # get object, if not        found return 404 error
#     url.count += 1
#     print(url.httpurl)
#     url.save()
#     return HttpResponseRedirect(url.httpurl)

# def shorten_url(request):
#     url = request.POST.get("url", '')
#     if not (url == ''):
#         short_id = get_short_code()
#         b = Urls(httpurl=url, short_id=short_id)
#         b.save()
#
#         response_data = {}
#         response_data['url'] = settings.SITE_URL + "/" + short_id
#         return HttpResponse(json.dumps(response_data),  content_type="application/json")
#     return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")

def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Urls.objects.get(pk=short_id)
        except:
            return short_id