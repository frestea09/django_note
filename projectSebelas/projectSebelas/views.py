from django.shortcuts import render

def index(request):
    content = {
        'section':'Home',
        'judul':'Home',
        'article':'Selamat Datang di website ini',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
        ],
        'banner':'img/banner.jpg',
    }
    return  render(request,'index.html',content)

def post(request):
    content = {
        'section': 'Home',
    }
    if request.method == 'POST':
        content['nimMahasiswa'] = request.POST.get('nimMahasiswa')
        content['nameMahasiswa'] = request.POST.get('nameMahasiswa')
    else:
        content['gagal'] = 'gagal'
    return  render(request,'index.html',content)