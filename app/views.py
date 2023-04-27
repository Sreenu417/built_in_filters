from django.shortcuts import render

# Create your views here.
def built_in_filter(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'Hai hWo ArE yOu','dt':dt,'c':7,'m':0,'p':1}
    return render(request,'built_in_filter.html',d)