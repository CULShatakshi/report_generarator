from django.shortcuts import render
from .forms import ContactForm, FormalForm, PostForm
from .models import Post
from django.http import HttpResponseRedirect
 
from django.contrib.auth.decorators import login_required

def report_informal(request):
	return render(request, 'report_informal.html', {})
def report_formal(request):
	return render(request, 'report_formal.html', {})


def homepage(request):
	return render(request, 'homepage.html', {})





def info(request):
	form=ContactForm()
	if request.method == 'POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			event_name=form.cleaned_data['event_name']
			event_date=form.cleaned_data['event_date']

			How_would_you_summarise_the_event_in_one_line=form.cleaned_data['How_would_you_summarise_the_event_in_one_line']
			main_body=form.cleaned_data['main_body']
			conclusion=form.cleaned_data['conclusion']
			time=form.cleaned_data['Time']
			

			data={'event_name':event_name}
			data['event_date']=event_date
			data['How_would_you_summarise_the_event_in_one_line']=How_would_you_summarise_the_event_in_one_line
			data['main_body']=main_body
			data['conclusion']=conclusion
			data['time']=time

			
			return render(request,'report_informal.html',data)
			#to add more go to : forms.py
			# print(name,email)
	return render(request,'info.html',{'form':form})

def formal(request):
	form=FormalForm()
	if request.method == 'POST':
		form=FormalForm(request.POST)
		if form.is_valid():
			event_name1=form.cleaned_data['event_name1']
			event_date1=form.cleaned_data['event_date1']

			introduction1=form.cleaned_data['introduction1']
			main_body1=form.cleaned_data['main_body1']
			conclusion1=form.cleaned_data['conclusion1']
			

			data={'event_name1':event_name1}
			data['event_date1']=event_date1
			data['introduction1']=introduction1
			data['main_body1']=main_body1
			data['conclusion1']=conclusion1

			
			return render(request,'report_formal.html',data)
			#to add more go to : forms.py
			# print(name,email)
	return render(request,'formal.html',{'form':form})

def new(request):
	
    new_item=Post()
    
    new_item.first_name=request.POST.get('first_name')
    new_item.last_name=request.POST.get('last_name')
    new_item.save()
    return render (request, "new.html")
	

    