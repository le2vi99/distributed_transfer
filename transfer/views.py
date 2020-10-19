from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'transfer/index.html')

def form(request):
    fid = request.POST['fid']
    tid = request.POST['tid']
    amount = request.POST['amount']
    method = request.POST['method']
    print("{} {} {} {}".format(fid,tid,amount,method))
    return render(request, 'transfer/transfer.html')
