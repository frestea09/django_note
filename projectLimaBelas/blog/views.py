from django.shortcuts import render,redirect

def hitung(bilanganPertama,bilanganKedua):
    hasil = bilanganPertama + bilanganKedua
    return hasil

def index(request):
    content = {
        'titleWeb':'Blog',
        'judulArticle':'Blog',
        'article':'Ini adalah Section Blog menggunakan django, dan menampilkan Implementasi Form ',
        'link':'/hitung'
    }
    if request.method == 'POST':
        nilaiPertama = int(request.POST.get('namaMahasiswa'))
        nilaiKedua = int(request.POST.get('nilaiMahasiswa'))
        hasil = hitung(nilaiPertama,nilaiKedua)
        content['hasil'] = hasil
    else:
        content['error'] = 'Terjadi Error'
    return render(request,'blog/index.html',content)
