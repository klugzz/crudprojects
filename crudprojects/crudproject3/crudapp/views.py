from django.shortcuts import render,redirect
from crudapp.models import Bank
from crudapp.forms import BankForm
def read(request):
	bank=Bank.objects.all()
	return render(request,'apps/result.html',{'b':bank})
def insert(request):
	form=BankForm()
	if request.method=="POST":
		form=BankForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'apps/insert.html',{'form',form})
def delete(request,id):
	b=Bank.objects.get(id=id)
	b.delete()
	return redirect('/result')
def update(request,id):
	bank=Bank.objects.get(id=id)
	if request.method=="POST":
		form=BankForm(request.POST, instance=bank)
		if form.is_valid():
			form.save()
		return redirect('/result')
	return render(request,'apps/update.html',{'b':bank})