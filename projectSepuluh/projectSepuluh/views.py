from django.shortcuts import render

def index(request):
    content = {
        'judul':'Home',
        'article':'Ini adalah home',
        'menu':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
        ]
    }
    return render(request,'index.html',content)

def kirim(request):
    content = {
        'judul':'Kirim',
        'article':'ini article',
    }
    if request.method == 'POST':
        content['post'] = request.POST.get('post')
    else:
        print('ini metode get')
    return  render(request,'index.html',content)