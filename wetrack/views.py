from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from django.http import JsonResponse

import csv

def index(request):
    return HttpResponse("Hello, world. You're at the wetrack index.")

def report(request):
    report = loader.get_template('report.html')
    context = {}
    return HttpResponse(report.render(context, request))

def track(request):
    '''
    username = request.GET('user','')
    if username == '':
        return HttpResponse("please attach ?user=yourname")
    track = loader.get_template('track.html')
    gpsinfo = []
    with open(username+'.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=', ', quotechar='|')
        for row in reader:
            gpsinfo.append(row)
    context = {'user':username,'gpsinfo':gpsinfo}
    return HttpResponse(track.render(context, request))
    '''
def uploadgps(request):
    '''
    lat = request.GET.get('lat', '')
    lng = request.GET.get('lng', '')
    username = request.GET.get('username', '')
    timestamp = request.GET.get('time','')
    if lat != '' and lng !='' and username !='' and timestamp != '':
        with open(username+'.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([timestamp, lat, lng)
        return HttpResponse("{status:'success'}")
    else:
        return HttpResponse("{status:'failure'}")
    '''
    status = {"status":"success"}
    return JsonResponse(status)
# Create your views here.
