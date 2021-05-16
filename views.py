from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import student
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
     return render(request, 'index.html')

def insert(request):
    if request.method == 'POST':
        fname= request.POST['fname']
        lname= request.POST['lname']
        rollnumber1= request.POST['rollnumber']
        usn= request.POST['usn']
        address= request.POST['address']
        city= request.POST['city']
        gender= request.POST['gender']
        department= request.POST['dep']
        img= request.POST['img']

        student_obj = student.objects.create(fname=fname, lname=lname, rollnumber=rollnumber1, usn=usn, address= address, city= city, gender= gender, dep=department, img=img)
        student_obj.save()
        print('Data inserted')

        return redirect('/')
    else:
        return render(request, 'insert.html')
def view1(request):
    obj= student.objects.all()
    return render(request, 'view1.html', {'obj': obj})

def delete(request):
    if request.method == 'POST':
        rno= request.POST['rollnumber']
        student.objects.filter(rollnumber=rno).delete()
        print('Record Deleted')
        return redirect('/')

    else:
        return render(request, 'delete.html')
    
def update(request):
    if request.method=='POST':
        fname= request.POST['fname']
        lname= request.POST['lname']
        rollnumber1= request.POST['rollnumber']
        usn= request.POST['usn']
        address= request.POST['address']
        city= request.POST['city']
        gender= request.POST['gender']
        department= request.POST['dep']
        img= request.POST['img']

        student_obj =student.objects.filter(rollnumber=rollnumber1).update(fname=fname, lname=lname, rollnumber=rollnumber1, usn=usn, address= address, city= city, gender= gender, dep=department, img=img)
        #student_obj.save()
        print('Data Updated')

        return redirect('/')

    else:
        return render(request, 'update.html')
    
def view1(request):
    obj = student.objects.all()
    return render(request, 'view1.html', {'obj': obj})

def search(request):

    query = request.GET['query']
    #student_obj = student.objects.filter(rollnumber=search)
    #return HttpResponse("Hello sakshi")
    #obj1=student.objects.all().order_by(rollnumber)
    query = int(query)
    
    obj1 = student.objects.filter(rollnumber__contains=query)
    if obj1:
        
        return render(request, 'search.html', {'obj1': obj1})
    else:
        #return HttpResponse("No result found")
        return render(request, 'alert.html')

def sort(request):
    obj2 = student.objects.order_by('rollnumber')
    return render(request, 'sort.html', {'obj2': obj2})

def register(request):
	if request.method == 'POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		uname=request.POST['uname']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']
		
		if password1==password2:
			if User.objects.filter(username=uname).exists():
				print('Username Taken')
			elif User.objects.filter(email=email).exists():
				print('Email Taken')
			else:
				user=User.objects.create_user(username=uname,password=password1,email=email,first_name=fname,last_name=lname)
				user.save()
				print('user created')
				return redirect('/')
		else:
			print("Password not matching")
		return redirect('/')
	else:
		return render(request,'userreg.html')