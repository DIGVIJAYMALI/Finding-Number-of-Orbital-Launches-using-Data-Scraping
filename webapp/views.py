from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from . import NewScraper
from .forms import NameForm
import csv

import pandas as pd
# Create your views here.

s = ""

def index(request):
	return render(request, 'personal/home.html')

def GetOrbitalLaunchesCSV(request):
	#pd.set_option('display.width',1000)
	pd.options.display.max_colwidth = 300
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		name = NameForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
	else:
		name = NameForm()

	global s
	s = request.POST['launch_year']
	DataFrame=NewScraper.getlink(str(s))
	print("frame is :")
	print(DataFrame)
	#return render(request, 'personal/name.html', {'name': name})
	#ama3.getlink()
	#return render(request, 'personal/outputA.html', { 'content' : frame.to_html() })
	#def getCSV(request):
	response = HttpResponse(content_type='text/csv')
	response[
		'Content-Disposition'] = 'attachment; filename=OrbitalLaunchesOutput.csv'
	DataFrame.to_csv(response, index=False)
	return response


def GetOrbitalLaunchesData(request):
	# pd.set_option('display.width',1000)
	pd.options.display.max_colwidth = 300
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		name = NameForm(request.POST)
	# check whether it's valid:
	# if form.is_valid():
	# process the data in form.cleaned_data as required
	# ...
	# redirect to a new URL:
	# return HttpResponseRedirect('/thanks/')

	# if a GET (or any other method) we'll create a blank form
	else:
		name = NameForm()

	global s
	s = request.POST['launch_year']
	DataFrame = NewScraper.getlink(str(s))
	print("frame is :")
	print(DataFrame)
	# return render(request, 'personal/name.html', {'name': name})
	# ama3.getlink()
	return render(request, 'personal/outputA.html', { 'content' : DataFrame.to_html() })

