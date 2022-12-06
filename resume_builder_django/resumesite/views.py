from django.shortcuts import render
from .forms import ContactForm, FormalForm

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

			introduction=form.cleaned_data['introduction']
			main_body=form.cleaned_data['introduction']
			conclusion=form.cleaned_data['introduction']
			highlights=form.cleaned_data['highlights']
			

			data={'event_name':event_name}
			data['event_date']=event_date
			data['introduction']=introduction
			data['main_body']=main_body
			data['conclusion']=conclusion
			data['highlights']=highlights

			
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
