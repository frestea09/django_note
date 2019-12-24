from django.shortcuts import render,redirect
from . import form
# Create your views here.
def index(request):
    myForm = form.FormPost(request.POST or None)
    content = {}
    if(request.method == 'POST'):
        if(myForm.is_valid()):
            myForm.save()
            return redirect('blog:index')
    content['form'] = myForm
    return render(request,'blog/index.html',content)