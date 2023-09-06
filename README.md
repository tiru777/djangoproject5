```commandline
Function Based Views
```

```commandline
Function based as simillar to Class based views only thing we are going to use functions for handling data
```

```commandline
- After installing Django project and configuration
- Create Templates folder and configure in Settings.py file
- create static folder and configure in settings.py file
```

```commandline
function based views

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from app.models import Employee
from app.forms import EmployeeForm

render
    - it used for to return context and html and request of particular function
    
Template return
    - Just template return we can use render
forms.py
    - we have to create model forms or django forms
       from django.forms import ModelForm
    - check app/forms.py file 
Creat function
    - this function is using for taking end user form data and saving to database
    - Before saving the data which we are getting assigining to form
    - validating request getting post or not
        -  then saving form data and redirecting to HTTPSResponseredirect url
        - else returning html file based created forms
        
list function
    - this function is used for getting list of data stored in database using Django ORM
    - So the data we are going to return to HTML file using render.

Delete function
    - This function before going to delete any objects we have to specify which object you need to delete.
    - You have to pass specific ID to the function and fetch the particular object data using ORM of GET.

Read function
    - This function is used for fetching particular objects by using ORM of GET for that you have to pass specific Id to the function

Update Function
    - This function is used for to update specific or particular objects.
    - Before updating we have to fetch particular object data by using ORM of GET.
    - After fetching the data assign it to the respective form.
    - Validate the data coming from end user as request.POST
        - If the request satisfy save the form data 
        - else render the form data to html file

Note: refer code
```