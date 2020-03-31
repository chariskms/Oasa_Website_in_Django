from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, auth
from django.contrib import messages
from .models import *

# Create your views here.


def searchStations(request):
    query = request.GET.get("searchArea")
    queryset_list =[]
    if query:
        queryset_list = Station.objects.filter(area=query)
    print(queryset_list)
    print(query)

    return render(request,'itineraries.html', {'results': queryset_list, 'requested': query, 'len': len(queryset_list)})

def searchAStation(request):
    name = request.GET.get("Station.Name")
    area = request.GET.get("Station.Area")
    queryset_list1 = []
    queryset_list2 = []
    queryset_list3 = []
    if name and area:
        if Station.objects.filter(name=name,area=area):
            queryset_list1 = Station.objects.get(name=name,area=area).busline_set.all()
            queryset_list2 = Station.objects.get(name=name,area=area).metroline_set.all()
            queryset_list3 = Station.objects.get(name=name,area=area).tramline_set.all()
        print(queryset_list1, queryset_list2, queryset_list3)


    return render(request,'itineraries.html', {'results1': queryset_list1, 'results2': queryset_list2, 'results3': queryset_list3,'requested2': name and area, 'len': len(queryset_list1) + len(queryset_list2) + len(queryset_list3)})

def busStations(request):
    line = request.GET.get("busline")
    id = 0
    if line:
        id = line
    queryset_list = []
    if id:
        """queryset_list = MetroLine.objects.filter(id=id).stations"""
        if BusLine.objects.filter(name=id):
            line = BusLine.objects.get(name=id)
            queryset_list = line.stations.all().order_by('name')
    print(queryset_list)
    print(id)

    return render(request, 'itineraries.html',{'results': queryset_list, 'requested5': id, 'len': len(queryset_list)})

def metroStations(request):
    line = request.GET.get("line")
    id = 0
    if line:
        id = line
    queryset_list = []
    if id:
        """queryset_list = MetroLine.objects.filter(id=id).stations"""
        line = MetroLine.objects.get(id=id)
        queryset_list = line.stations.all().order_by('id')
    print(queryset_list)
    print(id)

    return render(request, 'itineraries.html',{'results': queryset_list, 'requested3': id, 'len': len(queryset_list)})

def tramStations(request):
    line = request.GET.get("tramline")
    id = 0
    if line:
        id = line
    queryset_list = []
    if id:
        line = TramLine.objects.get(id=id)
        queryset_list = line.stations.all().order_by('id')
    print(queryset_list)
    print(id)

    return render(request, 'itineraries.html',{'results': queryset_list, 'requested4': id, 'len': len(queryset_list)})

def ticketCart(request):
    sum = 0
    if request.method == 'GET':
        quantity = request.GET.get("quantity")
        ticketType = request.GET.get("ticketType")
        if not quantity:
            quantity = '0'
        if ticketType == 'oneRoute':
            sum = 1.4*int(quantity)
        elif ticketType == 'dayTicket':
            sum = 4.5*int(quantity)
        elif ticketType == 'doubleRoute':
            sum = 2.7*int(quantity)
        elif ticketType == 'fiveDays':
            sum = 9*int(quantity)
        elif ticketType == 'airport':
            sum = 10*int(quantity)
        return render(request, 'ticketCart.html', {'price': sum})
    else:

        return render(request, 'ticketCart.html')


def loadCard(request):
    sum = 0
    if request.method == 'GET':
        quantity = request.GET.get("quantity")
        ticketType = request.GET.get("ticketType")
        wallet = request.GET.get("wallet")
        if not quantity:
            quantity = '0'
        if request.user.is_authenticated:
            user = request.user
            print("sindedemenos")
            elder = Elder.objects.filter(user=user)
            student = Student.objects.filter(user=user)
            normal = Normal.objects.filter(user=user)
            resellers = Resellers.objects.filter(user=user)
            unemployed = Unemployed.objects.filter(user=user)
            if elder:
                if ticketType == 'oneRoute':
                    sum = 0.6 * int(quantity)
                elif ticketType == 'dayTicket':
                    sum = 2.25 * int(quantity)
                elif ticketType == 'doubleRoute':
                    sum = 1.2 * int(quantity)
                elif ticketType == 'fiveDays':
                    sum = 4.5 * int(quantity)
                elif ticketType == 'airport':
                    sum = 5 * int(quantity)
            elif student:
                if ticketType == 'oneRoute':
                    sum = 0.6 * int(quantity)
                elif ticketType == 'dayTicket':
                    sum = 2.25 * int(quantity)
                elif ticketType == 'doubleRoute':
                    sum = 1.2 * int(quantity)
                elif ticketType == 'fiveDays':
                    sum = 4.5 * int(quantity)
                elif ticketType == 'airport':
                    sum = 5 * int(quantity)
            elif normal:
                 if ticketType == 'oneRoute':
                     sum = 1.4 * int(quantity)
                 elif ticketType == 'dayTicket':
                     sum = 4.5 * int(quantity)
                 elif ticketType == 'doubleRoute':
                     sum = 2.7 * int(quantity)
                 elif ticketType == 'fiveDays':
                     sum = 9 * int(quantity)
                 elif ticketType == 'airport':
                     sum = 10 * int(quantity)
            elif resellers:
                if ticketType == 'oneRoute':
                    sum = 1.4 * int(quantity)
                elif ticketType == 'dayTicket':
                    sum = 4.5 * int(quantity)
                elif ticketType == 'doubleRoute':
                    sum = 2.7 * int(quantity)
                elif ticketType == 'fiveDays':
                    sum = 9 * int(quantity)
                elif ticketType == 'airport':
                    sum = 10 * int(quantity)
            elif unemployed:
                    sum = 0
            print(wallet)
            if wallet:
                sum = sum + int(wallet)

            return render(request, 'ticketCart.html', {'price': sum})

        else:
            if ticketType == 'oneRoute':
                sum = 1.4*int(quantity)
            elif ticketType == 'dayTicket':
                sum = 4.5*int(quantity)
            elif ticketType == 'doubleRoute':
                sum = 2.7*int(quantity)
            elif ticketType == 'fiveDays':
                sum = 9*int(quantity)
            elif ticketType == 'airport':
                sum = 10*int(quantity)
            if wallet:
                sum = sum + int(wallet)
            return render(request, 'ticketCart.html', {'price': sum})
    else:

        return render(request, 'ticketCart.html')


def home(request):
    return render(request, 'index.html')


def directions(request):
    origin =" "
    destination= " "
    if request.method == 'GET':
        origin = request.GET.get("origin")
        destination = request.GET.get("destination")
        str(origin).replace(" ", "+")
        str(destination).replace(" ", "+")
        print(origin)
    return render(request, 'directions.html', {'originRes': origin, 'destinationRes': destination, 'directRequest': origin})


def itineraries(request):
    return render(request, 'itineraries.html')


def maps(request):
    return render(request, 'maps.html')


def tickets(request):
    return render(request, 'tickets.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        userType = request.POST['userType']
        password1 = request.POST['password2']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=email).exists():
                messages.info(request, 'Email Taken')
                return
            else:
                user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, password=password1, email=email)
                user.save()
                if userType == 'Student':
                    model = Student(user=user)
                    model.save()
                elif userType == 'Unemployed':
                    model = Unemployed(user=user)
                    model.save()
                elif userType == 'Elder':
                    model = Elder(user=user)
                    model.save()
                elif userType == 'Normal':
                    model = Normal(user=user)
                    model.save()
                elif userType == 'Resellers':
                    model = Resellers(user=user)
                    model.save()
                group = Group.objects.get(name=userType)
                user.groups.add(group)
                if user.groups.filter(name=group).exists():
                    print('mpike sto group')
                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
            return redirect('login')
    else:
        return redirect('login')


def login(request):
    if request.method == 'POST':
        print('login')
        password = request.POST['password']
        email = request.POST['email']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
           auth.login(request,user)
           return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def editProfile(request):
    if request.method == 'POST':
        user = request.user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        userType = request.POST['userType']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        print("eimai o ",first_name)
        print("thelw na ginw",userType)
        if password1 == password2:
            if user.username != email:
                if User.objects.filter(username=email).exists():
                    messages.info(request, 'Email Taken')
                    return

            user.first_name = first_name
            user.last_name = last_name
            user.username = email
            user.email = email
            user.save()

            elder = Elder.objects.filter(user=user)
            student = Student.objects.filter(user=user)
            normal = Normal.objects.filter(user=user)
            resellers = Resellers.objects.filter(user=user)
            unemployed = Unemployed.objects.filter(user=user)

            if elder:
                print("imoun",elder)
                elder = Elder.objects.get(user=user)
                elder.delete()
                oldType = "Elder"
            elif student:
                print("imoun", student)
                student = Student.objects.get(user=user)
                student.delete()
                oldType = "Student"
            elif normal:
                print("imoun", normal)
                normal = Normal.objects.get(user=user)
                normal.delete()
                oldType = "Normal"
            elif resellers:
                print("imoun", resellers)
                resellers = Resellers.objects.get(user=user)
                resellers.delete()
                oldType = "Resellers"
            else:
                print("imoun", unemployed)
                unemployed = Unemployed.objects.get(user=user)
                unemployed.delete()
                oldType = "Unemployed"

            group = Group.objects.get(name=oldType)
            user.groups.remove(group)

            if userType == 'Student':
                model = Student(user=user)
                model.save()
            elif userType == 'Unemployed':
                model = Unemployed(user=user)
                model.save()
            elif userType == 'Elder':
                model = Elder(user=user)
                model.save()
            elif userType == 'Normal':
                model = Normal(user=user)
                model.save()
            elif userType == 'Resellers':
                model = Resellers(user=user)
                model.save()

            group = Group.objects.get(name=userType)
            user.groups.add(group)

            return redirect('/')
        else:
            return render(request, 'editProfile.html')
    else:
        """
        userName = User.get_short_name()
        userFullName = User.get_full_name()
        """
        user = request.user
        print("else")
        elder = Elder.objects.filter(user=user)
        student = Student.objects.filter(user=user)
        normal = Normal.objects.filter(user=user)
        reseller = Resellers.objects.filter(user=user)
        unemployed = Unemployed.objects.filter(user=user)
        return render(request, 'editProfile.html', {'student': student, 'elder': elder, 'normal':normal, 'reseller': reseller, 'unemployed': unemployed})


def org_oasa(request):
    return render(request, 'org_oasa.html')


def contact(request):
    return render(request, 'contact.html')


def amea(request):
    return render(request, 'amea.html')



