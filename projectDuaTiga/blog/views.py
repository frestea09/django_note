from django.shortcuts import render
from . import form
# Create your views here
def index(request):
    contanForm = form.formSaya()
    content = {
        'title':'Blog',
        'form':contanForm
    }
    if(request.method == 'POST'):
        content['nama'] = request.POST['nama']
        content['hobby'] = request.POST['hobby']
    return render(request,'blog/index.html',content)