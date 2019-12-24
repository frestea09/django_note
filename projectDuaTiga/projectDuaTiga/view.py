from django.shortcuts import render

def index(request):
    content = {
        'title':'Home',
    }
    if request.method == 'POST':
        content['nama'] = request.POST['nameMahasiswa']
    print(content)
    return render(request,'index.html',content)