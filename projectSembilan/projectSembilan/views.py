from django.shortcuts import render
from django.http import HttpResponseRedirect
def index(request):
    content = {
        'judul':'Home',
        'article':'Welcome in home',
        'nav':[
            ['','Home'],
            ['/blog','Blog']
        ]
    }
    if request.method == 'POST':
        content['nameMahasiswa'] = request.POST['nameMahasiswa']
    else:
        print('false')
    return render(request,'index.html',content)
