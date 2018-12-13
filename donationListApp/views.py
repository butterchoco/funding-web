from django.shortcuts import render
from ProgramApp.models import program_registration

# Create your views here.
response = {}

def donation(request):
    if request.user.is_authenticated:
        strNama = request.user.first_name + " " + request.user.last_name
        strNama = strNama.strip()
        request.session['name'] = strNama
        request.session['email'] = request.user.email
        response['nama'] = request.session['name']
    else:
        response['nama'] = ''
    donasi = program_registration.objects.filter(email=request.session['email'])
    jumlahDonasi = 0;
    for data in donasi:
        jumlahDonasi += data.jumlah_uang
    response['jumlahDonasi'] = jumlahDonasi
    response['donationlist'] = donasi
    return render(request, 'donationlist.html', response)
