from django.shortcuts import render, redirect
from RestManage.models import Customer,Product,Order
from django.contrib import messages

def index(request):
	ord_data= Order.objects.all()
	return render(request, "index.html", {'ord_data':ord_data})

def create(request):
	cust_data= Customer.objects.all()
	prod_data= Product.objects.all()
	return render(request, "create.html", {'cust_data':cust_data, 'prod_data':prod_data})

def data_stored(request):
	customer_id=request.POST['customer_id'] 
	customer= Customer.objects.get(id=customer_id)
	product_id=request.POST['product_id']
	product= Product.objects.get(id=product_id)
	unit_price=request.POST['unit_price'] 
	qty=request.POST['qty']
	total_price= float(unit_price) * int(qty)
	data1= Order(customer_id=customer, product_id=product, unit_price=request.POST['unit_price'], qty=request.POST['qty'],total_price=total_price)
	data1.save()
	messages.success(request, 'Data Submitted')
	return redirect('/create')

def data_deleted(request, id):
	ord_data= Order.objects.filter(id=id)
	ord_data.delete()	
	return redirect('/index')

def edit_data(request,id):
	ord_dataa= Order.objects.filter(id=id)
	return render(request, 'index.html', {'ord_dataa':ord_dataa})

def data_updated(request, id):
	customer_id = request.POST['customer_id']
	print(customer_id)
	ord_data= Order.objects.filter(id=id)
	return redirect('/index')

	