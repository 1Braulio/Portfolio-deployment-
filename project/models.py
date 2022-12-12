from django.db import models
import uuid 

# Create your models here.

class Project(models.Model):
	# tags
	tags = models.ManyToManyField('Tag', blank = True)
	# title
	title = models.CharField(max_length = 200)
	# description
	description = models.TextField(null = True, blank = True)
	# When it was created
	created = models.DateTimeField(auto_now_add = True)
	# When it was updated
	updated = models.DateTimeField(auto_now = True)
	# link to source code
	source_link = models.CharField(max_length = 100, null = True, blank = True)
	# votes
	vote_total = models.IntegerField(default = 0)
	# votes ratio
	vote_ratio = models.IntegerField(default = 0)
	# featured_image
	featured_image = models.ImageField(null = True, blank = True, default = 'default.jpg')
	# id 
	id = models.UUIDField(default = uuid.uuid4, unique = True,
		primary_key = True, editable = False)

	def __str__(self):
		return self.title

	@property
	def imageURL(self):
		# get img
		try:
			img = self.featured_image.url
		except:
			img = ''

		return img



class Review(models.Model):
	# vote values
	VOTE_TYPE = (
			('up', 'up'),
			('down', 'down'),
		)
	# foreign key to each instance of Project
	project = models.ForeignKey(Project, on_delete = models.CASCADE,
		null = True, blank = True)
	# review's body
	body = models.TextField(null = True, blank = True)
	# vote's value
	value = models.CharField(max_length = 50, choices = VOTE_TYPE)
	# when it was created
	created = models.DateTimeField(auto_now_add = True)
	# when it was updated
	updated = models.DateTimeField(auto_now = True)
	# id
	id = models.UUIDField(default = uuid.uuid4, unique = True,
		primary_key = True, editable = False)

	def __str__(self):
		return self.value

class Tag(models.Model):
	# tag name
	name = models.CharField(max_length = 200)
	# when it was created
	created = models.DateTimeField(auto_now_add = True)
	# id
	id = models.UUIDField(default = uuid.uuid4, unique = True,
		primary_key = True, editable = False)

	def __str__(self):
		return self.name