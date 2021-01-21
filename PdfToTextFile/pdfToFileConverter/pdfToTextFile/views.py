# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from PyPDF2 import PdfFileReader
from django.http import HttpResponse

# Create your views here.
def index(request):
    txt = ''
    showTextFile = 0
    file_data = request.session.get('extractedText')
    if request.method == 'POST':
        showTextFile = 1
        pdfFile = request.FILES['pdfFile']
        pdf = PdfFileReader(pdfFile) 
        for page_num in range(pdf.numPages):
            pageObj = pdf.getPage(page_num)
            txt = txt + pageObj.extractText()
        request.session['extractedText'] = txt 
    elif request.method == 'GET' and file_data:
        response = HttpResponse(file_data, content_type='application/text charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="content.txt"'
        request.session['extractedText'] = '' 
        return response  
    return render(request,'base.html',{"showTextFile":showTextFile})
    
def textFileConverter(request):
    text="" 
    return render(request,'base.html')


def export_text_file(request):
    return render(request,'base.html')