from django.shortcuts import render
from .models import Branch, Broker
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
# Create your views here.
def mainpage(request):
    branch = Branch.objects.all()
    broker = Broker.objects.all()

    context = {'BranchEntries' : branch, 'BrokerEntries' : broker}
    return render(request,'datamanage/mainpage.html', context=context)

def updateActiveFlag_branch(request):

    if request.method == 'POST':
        if 'branchoption' in request.POST:
            branchId = request.POST.get('branchoption')
            update = Branch.objects.get(BranchID=branchId)
            update.ActiveFlag = 0
            update.InactiveDate = datetime.now()
            update.save()
            return HttpResponseRedirect(reverse('data_manage'))
        else:
            return HttpResponseRedirect(reverse('data_manage'))


def updateActiveFlag_broker(request):

    if request.method == 'POST':
        if 'brokeroption' in request.POST:
            brokerId = request.POST.get('brokeroption')
            update = Broker.objects.get(BrokerID=brokerId)
            update.ActiveFlag = 0
            update.InactiveDate = datetime.now()
            update.save()
            return HttpResponseRedirect(reverse('data_manage'))
        else:
            return HttpResponseRedirect(reverse('data_manage'))

