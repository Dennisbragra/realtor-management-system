from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Housetype, HouseUnit, Topic, Messages, Reviews, Maintenance, HouseRequest
from .forms import HouseForm, TopicForm, MaintenanceForm, HouseRequestForm
# Create your views here.


@login_required(login_url='login')
def homeView(request):
	houses = HouseUnit.objects.all()
	reviews = Reviews.objects.all()[0:3]
	topics = Topic.objects.all()[0:3]

	context = {'houses':houses, 'reviews':reviews, 'topics':topics}
	return render(request, 'index.html', context)



def mainView(request):
	topics = Topic.objects.all()
	houses = HouseUnit.objects.all()
	reviews = Reviews.objects.all()

	context = {'topics':topics, 'houses':houses, 'reviews':reviews}

	return render(request, 'main.html', context)

def requestUnit(request, pk):
	house = HouseUnit.objects.get(id=pk)
	houserequests = house.houserequest_set.all()
	
	if request.method == 'POST':
		
		houserequests = HouseRequest.objects.create(
			user = request.user,
			house = house,
			requested = True,
			)
		return redirect('houses')

	context = {'house':house}
	return render(request, 'requestunit.html', context)


def approveRequest(request, pk):
	house = HouseUnits.objects.get(id=pk)
	houserequest = HouseRequest.objects.get(id = pk)
	form = HouseRequestForm( instance = houserequest)

	if request.method == 'POST':
		
		houserequests = HouseRequest.objects.create(
	
			rented = True,
			)
		return redirect('houses')		

	context = {'houserequest':houserequest, 'form':form}
	return render(request, 'approverequest.html', context)


def unitRequested(request):
	houserequests = HouseRequest.objects.all()


	context = {'houserequests':houserequests}
	return render(request, 'requestedunits.html', context)



def addunitView(request):
	form = HouseForm()

	if request.method == 'POST':
		form = HouseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('houses')
	context = {'form':form}
	return render(request, 'add_updateunit.html', context)

def updateunitView(request, pk):
	house = HouseUnits.objects.get(id=pk)
	form = HouseForm(instance=house) 

	if request.method == 'POST':
		form = HouseForm(request.POST, instance=house)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {'form':form}
	return render(request, 'add_updateunit.html', context)

def viewUnit(request, pk):
	house = HouseUnit.objects.get(id = pk)
	rentdue = house.rent - house.rentpaid
	maintenances = house.maintenance_set.all()

	hserequests = house.houserequest_set.all()

    


	context = {'house':house, 'rentdue':rentdue, 'maintenances':maintenances, 'hserequests':hserequests}
	return render(request, 'viewunit.html', context)

def viewTopic(request, pk):
	topic = Topic.objects.get(id=pk)
	messages = topic.messages_set.all()

	if request.method == 'POST':
		messages = Messages.objects.create(
			tenant = request.user,
			topic=topic,
			message = request.POST.get('body')
			)
		return redirect('viewtopic', pk=topic.id)	


	context = {'topic':topic, 'messages':messages}

	return render(request, 'viewtopic.html', context)

def noticeBoard(request):
	topics = Topic.objects.all()
	messages = Messages.objects.all()

	context ={'messages':messages, 'topics':topics}
	return render(request, 'viewtopics.html', context)

def addNotice(request):
	form = TopicForm()

	if request.method =='POST':
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('noticeboard')
	

	context = {'form':form}

	return render(request, 'addnotice.html', context)
	

def rentArrears(request):
	houses = HouseUnit.objects.all()

	for house in houses:
		rentdue = house.rent - house.rentpaid


	context = {'houses':houses, 'rentdue':rentdue}
	return render(request, 'rentarrears.html', context)

def reviewsView(request):
	reviews = Reviews.objects.all()

	if request.method == 'POST':
		reviews = Reviews.objects.create(
			host = request.user,
			body = request.POST.get('body')
			)
		return redirect('reviews')
	context = {'reviews':reviews}	

	return render(request, 'reviews.html', context)

def maintenanceView(request, pk):
	house = HouseUnit.objects.get(id=pk)
	rentdue = house.rent - house.rentpaid
	maintenances = house.maintenance_set.all()

	if request.method == 'POST':
		maintenances = Maintenance.objects.create(
			house = house,
			repaired = False,
			natureofrepair = request.POST.get('body')
			)		
		return redirect('maintenance', pk = house.id)

	context = {'house':house, 'rentdue':rentdue, 'maintenances':maintenances}
	return render(request, 'maintenance.html', context)

def maintenanceRequestView(request):
	maintenances = Maintenance.objects.all()	



	context = {'maintenances':maintenances}
	return render(request, 'maintenancerequests.html', context)

def updateMaintenanceView(request, pk):
	maintenance = Maintenance.objects.get(id=pk)
	form = MaintenanceForm(instance=maintenance) 

	if request.method == 'POST':
		form = MaintenanceForm(request.POST, instance=maintenance)
		if form.is_valid():
			form.save()
			return redirect('maintenance-requests')	


	context = {'maintenance':maintenance, 'form':form}
	return render(request, 'updatemaintenance.html', context)
