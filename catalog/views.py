from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'catalog/homepage.html')

def contacts(request):
    if request.method == 'POST':
        username = request.POST.get("name")
        message = request.POST.get("message")
        phone = request.POST.get("phone")
        print( f'{username},{phone}:{message}')

    return render(request, 'catalog/contacts.html')
