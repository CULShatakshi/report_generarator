from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from crispy_forms.layout import Column
from crispy_forms.layout import Row
from django.forms import ModelForm
from .models import Post

 


# class SkillWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','','','','','',''])

# class SkillsField(forms.MultiValueField):
# 	widget=SkillWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),
# 			forms.CharField(),
# 			forms.CharField(),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]} {data_list[3]} {data_list[4]} {data_list[5]} {data_list[6]}'


# class ExpWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput()#,
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','',''])

# class ExpField(forms.MultiValueField):
# 	widget=ExpWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),#validators can be added
# 			forms.CharField(),
# 			forms.CharField(),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]}'

# class EduWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput()#,
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','',''])

# class EduField(forms.MultiValueField):
# 	widget=EduWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),#validators can be added
# 			forms.CharField(),
# 			forms.CharField(),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]}'


class ContactForm(forms.Form):
	event_name=forms.CharField(required=False)
	event_date=forms.DateField(required=False)
	How_would_you_summarise_the_event_in_one_line=forms.CharField(required=False)
	main_body=forms.CharField(required=False)
	conclusion=forms.CharField(required=False)
	Time=forms.CharField(required=False)
	

	# How_would_you_summarise_the_event_in_one_line

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.helper=FormHelper
		self.helper.form_class = ' container justify-content-center '
		# self.helper.label_class = ''
		# self.helper.field_class = 'col-md-6 col-xs-9'
		self.helper.form_method="post"
		self.helper.layout=Layout(
			Row(
                Column('event_name', css_class='form-group col-md-12  mb-15'),
                Column('event_date', css_class='form-group col-md-3 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('How_would_you_summarise_the_event_in_one_line', css_class='form-group col-md-12  mb-15'),
				Column('main_body', css_class='form-group col-md-12  mb-15'),
				Column('Time', css_class='form-group col-md-12  mb-15'),
				Column('conclusion', css_class='form-group col-md-12  mb-15'),

               
                css_class='form-row  center'
            ),
			
			Submit('submit','Submit',css_class="btn-success")
			)
class FormalForm(forms.Form):
	event_name1=forms.CharField(required=False)
	event_date1=forms.DateField(required=False)
	introduction1=forms.CharField(required=False)
	main_body1=forms.CharField(required=False)
	conclusion1=forms.CharField(required=False)
	

	

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.helper=FormHelper
		self.helper.form_class = ' container justify-content-center '
		# self.helper.label_class = ''
		# self.helper.field_class = 'col-md-6 col-xs-9'
		self.helper.form_method="post"
		self.helper.layout=Layout(
			Row(
                Column('event_name1', css_class='form-group col-md-12 mb-15'),
                Column('event_date1', css_class='form-group col-md-3 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('introduction1', css_class='form-group col-md-12  mb-15'),
				Column('main_body1', css_class='form-group col-md-12  mb-15'),
				Column('conclusion1', css_class='form-group col-md-12  mb-15'),
               
                css_class='form-row  center'
            ),
			
			Submit('submit','Submit',css_class="btn-success")
			)

class PostForm(ModelForm):
	class meta:
		model=Post
		fields= '__all__'
		
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.helper=FormHelper
		self.helper.form_class = ' container justify-content-center '