from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    print(request.POST.get('text','default'))
    return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps= request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc=="on":
         analyzed=""
         for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char
         params={'purpose':"Remove Punctuations",'analyzed_text':analyzed}
         djtext=analyzed
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params = {'purpose': "Changed to upper case", 'analyzed_text': analyzed}
        djtext=analyzed
    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': "New line removed", 'analyzed_text': analyzed}
        djtext=analyzed
    if charcount=="on":
        count=0
        for char in djtext:
            count+=1
        params = {'purpose': "count of characters", 'analyzed_text': count}
        djtext=analyzed

    return render(request, 'analyze.html', params)

