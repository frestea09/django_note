from django.shortcuts import render

# Create your views here.
def index(request):
    content = {
        'judul':'blog',
        'article':'ini adalah section blog',
        'nav':[
            ['/','Home']
        ]
    }
    if request.method == 'POST':
        content['nameMahasiswa'] = request.POST['nameMahasiswa']
    else:
        print('false')
    return render(request,'index.html',content)