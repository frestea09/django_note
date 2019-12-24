from django.shortcuts import render

def index(request):
    content = {
        'sectionWeb':'Home',
        'sectionWebDesc':'Section ini mengenai Home Website',
        'sectionWebDescDetail':'Website ini mengenai pelatihan ilman menggunakan django. Data yangdipergunakan adalah data blog.'
    }
    return  render(request,'index.html',content)