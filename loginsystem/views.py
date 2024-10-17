from django.shortcuts import render
from django.template import loader
# Create your views here.
from .models import Pasien, Dokter, Obat, Laporan
from .forms import PasienForm
from django.http import HttpResponse

from .login_logic import  auth_user

def dashboard_view(request):
    return render(request, "dashboard.html")

def pasien_view(request):
    if request.method == 'POST':
            # Handle the button click event here
        # data_nama=Pasien.objects.values_list('nama')
        data_nama=Pasien.objects.all()
        # print(data_nama)
        # print('aku diklik')
        return render(request, "pasien.html",{'persons': data_nama})
    
    data_nama=Pasien.objects.all()
    # print(data_nama)
    # print('aku diklik')

    return render(request, "pasien.html",{'persons': data_nama})
    # return HttpResponse('jkljlj')

def dokter_view(request):
    if request.method == 'POST':
            # Handle the button click event here
        # data_nama=Pasien.objects.values_list('nama')
        data_nama=Dokter.objects.all()
        print(data_nama)
        # print('aku diklik')
        return render(request, "dokter.html",{'persons': data_nama})
    
    data_nama=Dokter.objects.all()
    print(data_nama)
    # print('aku diklik')
    return render(request, "dokter.html",{'persons': data_nama})

def obat_view(request):
    if request.method == 'POST':
    #         # Handle the button click event here
    #     # data_nama=Pasien.objects.values_list('nama')
        data_nama=Obat.objects.all()
        print(data_nama)
    #     print('aku diklik')
        return render(request, "obat.html",{'persons': data_nama})
    
    data_nama=Obat.objects.all()
    print(data_nama)
    # print('aku diklik')
    return render(request, "obat.html",{'persons': data_nama})

def laporan_view(request):
    if request.method == 'POST':
    #         # Handle the button click event here
    #     # data_nama=Pasien.objects.values_list('nama')
        data_nama=Laporan.objects.all()
        print(data_nama)
    #     print('aku diklik')
        return render(request, "laporan.html",{'persons': data_nama})
    
    data_nama=Laporan.objects.all()
    print(data_nama)
    # print('aku diklik')
    return render(request, "laporan.html",{'persons': data_nama})

def settings_view(request):
    # if request.method == 'POST':
    #         # Handle the button click event here
    #     # data_nama=Pasien.objects.values_list('nama')
    #     data_nama=Pasien.objects.all()
    #     print(data_nama)
    #     print('aku diklik')
    #     return render(request, "settings.html",{'persons': data_nama})
    
    # data_nama=Pasien.objects.all()
    # print(data_nama)
    # print('aku diklik')
    return render(request,"settings.html")

def login_view(request):
    test = auth_user('joko','dfdsafdf')
    print(test)
    
    return render(request, "login.html")
    

def loginsystems(request):
    print('Hello')
    
    return render(request, 'login.html')

def index(request):
    context = {}
    form = Pasien()
    scores = Pasien.object.all()
    context['pasien'] = Pasien
    context['title'] = Pasien
    context['form'] = form
    print('hhhh')
    return render(request, 'dashboard.html', context)

def about(request):
    context = {}
    context['title'] = 'about'
    return render(request, 'about.html', context)

# def dashboard(request):
   # return render(request, 'dashboard.html' )

def loginsystems(request):
    template = loader.get_template('dashboard.html')
    data_nama=Pasien.objects.values_list('nama')
    print(data_nama)
    print('hhhh')

    context = {
        'titleklinik' : 'Dashboard Klinik',
        }
    return HttpResponse(template.render(context, request))