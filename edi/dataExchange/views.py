from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader


import requests
import json, xmltodict

api_url = "https://wlzsqbocgbjocri.weclapp.com/webapp/api/v1/user"
headers = {
            "Content-Type": "application/json",
            "AuthenticationToken":"ed81f7c4-309d-46dc-916f-d366fe922c30",
        }

def index(request):
    template = loader.get_template('./index.html') 
    return HttpResponse(template.render())

def handle_xml_upload(request):
    xmlfile = request.FILES['xmlfile'] if 'xmlfile' in request.FILES else None
    print(xmlfile)
    with open(xmlfile) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        json_data = json.dumps(data_dict['root'])
        x = requests.post(api_url, json = json_data, headers=headers)
        print(x)
    return render(request, 'index.html')
    

