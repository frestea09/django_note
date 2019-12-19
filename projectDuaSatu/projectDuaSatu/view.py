from django.shortcuts import render

def index(request):
    content = {
        'kata':'hello'
    }
    return render(request,'index.html',content)
def angka(request,**input):
    content = {
        'kata':'hello',
        'tahun':input['tahun'],
        'bulan':input['bulan'],
        'tanggal':input['tanggal'],
    }
    return render(request,'index.html',content)
def page(request,page):
    content = {
        'kata':'hello',
        'page':page,
    }
    return render(request,'index.html',content)
