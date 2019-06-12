# Notes(steps) on learning how to setup the polls app

**Notes**:
+ The three-step guide to making model changes:
    + 1. Change your models (in models.py).
    + 2. Run `python manage.py makemigrations` to create migrations for those changes
    + 3. Run `python manage.py migrate` to apply those changes to the database.


## Part1:
+ Creating a project¶
  	+ `$ django-admin startproject mysite`

+ The development server¶
	+ `$ python manage.py runserver`

+ Creating the Polls app¶
	+ `$ python manage.py startapp polls`

+ Write your first view¶
	+ [polls/views.py](https://github.com/xx94xuan/mysite/blob/master/polls/views.py) & [polls/urls.py](https://github.com/xx94xuan/mysite/blob/master/polls/urls.py) & [mysite/urls.py](https://github.com/xx94xuan/mysite/blob/master/mysite/urls.py)

## Part2:
+ Database setup¶
	+ mysite/settings.py- DATABASES
	+ `$ python manage.py migrate`

+ Creating models¶
	+ [polls/models.py](https://github.com/xx94xuan/mysite/blob/master/polls/models.py)
	+ [mysite/settings.py](https://github.com/xx94xuan/mysite/blob/master/mysite/settings.py)  - INSTALLED_APP
	+ `$ python manage.py makemigrations polls` 
    + (`$ python manage.py sqlmigrate polls 0001`)
	+ `$ python manage.py migrate`

+ Playing with the API
	+ `$ python manage.py shell`
		```
		# import the model class
		from polls.models import Question

		# list out all the data of Question model
		questions = Question.objects.all()

		from django.utils import timezone

		# create a new Question
		q = Question(question_text="What's new?", pub_date=timezone.now())

		# save the record to database
		q.save()
		```

### Introducing the Django Admin¶

+ Creating an admin user
    + `$ python manage.py createsuperuser`
+ Start the development server
Enter the admin site
Make the poll app modifiable in the admin
    + [polls/admin.py](https://github.com/xx94xuan/mysite/blob/master/polls/admin.py) 

+ Explore the free admin functionality¶
	+ #class be registered would show on admin index page

## Writing your first Django app, part 3¶
+ [polls/views.py](https://github.com/xx94xuan/mysite/blob/master/polls/views.py) & [polls/urls.py](https://github.com/xx94xuan/mysite/blob/master/polls/urls.py)

> When somebody requests a page from your website – say, “/polls/34/”, Django will load the mysite.urls Python module because it’s pointed to by the ROOT_URLCONF setting. It finds the variable named urlpatterns and traverses the patterns in order. After finding the match at 'polls/', it strips off the matching text ("polls/") and sends the remaining text – "34/" – to the ‘polls.urls’ URLconf for further processing. There it matches '<int:question_id>/', resulting in a call to the detail() view like so

+ Write views that actually do something¶
	+ [polls/views.py](https://github.com/xx94xuan/mysite/blob/master/polls/views.py)
	+ [polls/templates/polls/index.html](https://github.com/xx94xuan/mysite/blob/master/polls/templates/polls/index.html)
> Your project’s TEMPLATES setting describes how Django will load and render templates. The default settings file configures a DjangoTemplates backend whose APP_DIRS option is set to True. By convention DjangoTemplates looks for a “templates” subdirectory in each of the INSTALLED_APPS.

+ template loader:

	``` template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

    shortcut(same as):
    return render(request, 'polls/index.html', context)

+ template system¶
	+ dot-lookup syntax: 
        + 1. dictionary lookup
        + 2. attributes lookup
        + 3. list-index lookup

+ Removing hardcoded URLs in templates¶(path_name in urls.py)
	+ `<a href="/polls/{{ question.id }}/">{{ question.question_text }}</a>`
	===> `<a href="{% url 'detail' question.id %}">{{ question.question_text }}</a>`

+ Namespacing URL names¶
	+ urls.py: app_name=???
	+ template: '???:path_name'

## Write a simple form¶
> all POST forms that are targeted at internal URLs should use the {% csrf_token %} template tag

> Always return an HttpResponseRedirect after successfully dealing with POST data

> request.POST values are always strings
