from django.shortcuts import render,redirect
from crudapp.models import Product
from crudapp.forms import ProductForm
def read(request):
	product=Product.objects.all()
	return render(request,'apps/result.html',{'p':product})
def insert(request):
	form=ProductForm()
	if request.method=="POST":
		form=ProductForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'apps/insert.html',{'form':form})
def delete(request,id):
	p=Product.objects.get(id=id)
	p.delete()
	return redirect('/result')
def update(request,id):
	product=Product.objects.get(id=id)
	if request.method=="POST":
		form=ProductForm(request.POST,instance=product)
		if form.is_valid():
			form.save()
		return redirect('/result')
	return render(request,'apps/update.html',{'p':product})

# Create your views here.
