from django.shortcuts import render
import random


# Create your views here.
def password(request):
    symbols = 'abcdefghijklmnopqrstuvwxyz'

    if request.GET.get('uppercase'):
        symbols += symbols.upper()
    if request.GET.get('number'):
        symbols += '1234567890'
    if request.GET.get('special'):
        symbols += '!@#$%^&*()_+?][~'

    length = int(request.GET.get('length'))

    created_password = ''
    for i in range(length):
        created_password += random.choice(symbols)

    return render(request, 'password/password.html', {'created_password': created_password})
