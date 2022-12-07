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

			How_would_you_summarise_the_event=form.cleaned_data['How_would_you_summarise_the_event']
			As_a_writer_How_would_you_rate_the_event_out_of_10=form.cleaned_data['As_a_writer_How_would_you_rate_the_event_out_of_10']
			conclusion=form.cleaned_data['conclusion']
			What_was_the_inspiration_for_this_event=form.cleaned_data['What_was_the_inspiration_for_this_event']
			Would_you_like_to_give_special_credits_to_anyone=form.cleaned_data['Would_you_like_to_give_special_credits_to_anyone']
			

			data={'event_name':event_name}
			data['event_date']=event_date
			data['How_would_you_summarise_the_event']=How_would_you_summarise_the_event
			data['As_a_writer_How_would_you_rate_the_event_out_of_10']=As_a_writer_How_would_you_rate_the_event_out_of_10
			data['conclusion']=conclusion
			data['What_was_the_inspiration_for_this_event']=What_was_the_inspiration_for_this_event
			data['Would_you_like_to_give_special_credits_to_anyone']=Would_you_like_to_give_special_credits_to_anyone

			
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
	

    