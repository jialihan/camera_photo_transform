
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import re, io
import base64
import os
import errno

from django.core.files import File

# from django.views.generic import TemplateView


# Create your views here.


# class HomePageView(TemplateView):


def indexPage(request):
        return render(request, 'index.html', context=None)
    # def index(request):
    #     return render(request, 'index.html', [])

#  class AboutPageView(TemplateView):
#         template_name = "about.html"


def uploadPhoto(request):
    if request.method == 'POST' and request.is_ajax():

        dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
        image_data = request.POST['img']
        image_data = dataUrlPattern.match(image_data).group(2)
        image_data = image_data.encode()
        image_data = base64.b64decode(image_data)
        filename = "screen/input/screenshot.jpeg"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:      # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(filename, 'wb') as f:
            f.write(image_data)
        #####
        #  transformation algorithm calls();
        #####
        result_img = "screen/output/result.jpeg"
        try:
            with open(result_img, "rb") as imageFile:
                str = base64.b64encode(imageFile.read())
            # with open(result_img, "rb") as imageFile:
            #     f = imageFile.read()
            #     b = bytearray(f)
        except IOError as exc:
            raise IOError("%s: %s" % (result_img, exc.strerror))
        return HttpResponse(str)
    else:
        return HttpResponse("BAD request")

    # to Send Back processed pic
    # with open("t.png", "rb") as imageFile:
    #     str = base64.b64encode(imageFile.read())
    # print str


def testAjax(request):
    return render(request, 'about.html', context=None)

# def comments_upload(request):
#     if request.method == 'POST':
#         print("it's a test");
#         print(request.POST['name']);
#         print(request.POST['password']);
#         return HttpResponse("test ajax success")
#     else:
#         return HttpResponse("<h1>test</h1>")


def comments_upload(request):
    if request.method == 'POST':
        responseData = {
            'status': 200,
            'name': 'test Response'
        }
        # return HttpResponse(json.dumps(responseData), content_type="application/json")
        return HttpResponse("test ajax success")
    else:
         return HttpResponse("<h1>test</h1>")


