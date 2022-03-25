from django.db import models
from django.db.models.fields import TextField

# Create your models here.

#This is a profile model function
class Profile(models.Model):
	profile_pic=models.ImageField(upload_to="profile/",blank=False)
	fullname=models.CharField(max_length=100)
	designation=models.CharField(max_length=100)
	bio=models.TextField()
	cv=models.FileField(upload_to="profile/cv/",max_length=100)

	class Meta:
		verbose_name="Profile"
		verbose_name_plural="Profiles"

	def __str__(self):
		return self.fullname

#This is a about model function
class About(models.Model):
	long_about=models.TextField()
	short_about=models.TextField()

	class Meta:
		verbose_name="About"
		verbose_name_plural="Abouts"

	def __str__(self):
		return self.short_about

#This is a skill model function
class PrimarySkill(models.Model):
	icon=models.ImageField(upload_to="PrimarySkill/")
	name=models.CharField(max_length=50)

	class Meta:
		verbose_name="PrimarySkill"
		verbose_name_plural="PrimarySkills"

	def __str__(self):
		return self.name

class SecondarySkill(models.Model):
	icon=models.ImageField(upload_to="SecondarySkill/")
	name=models.CharField(max_length=50)

	class Meta:
		verbose_name="SecondarySkill"
		verbose_name_plural="SecondarySkills"

	def __str__(self):
		return self.name

#This is a service model function
class Service(models.Model):
	link=models.CharField(max_length=150)
	name=models.CharField(max_length=100)

	class Meta:
		verbose_name="Service"
		verbose_name_plural="Services"

	def __str__(self):
		return self.name

#This is a portfolio model function
class Portfolio(models.Model):
	link=models.CharField(max_length=150)
	name=models.CharField(max_length=100)

	class Meta:
		verbose_name="Portfolio"
		verbose_name_plural="Portfolios"

	def __str__(self):
		return self.name

#This is a blog model function
class Blog(models.Model):
	link=models.CharField(max_length=150)
	heading=models.CharField(max_length=100)

	class Meta:
		verbose_name="Blog"
		verbose_name_plural="Blogs"

	def __str__(self):
		return self.heading

#This is a testimonial model function
class Testimonial(models.Model):
	image=models.ImageField(upload_to="Testimonial/")
	image_name=models.CharField(max_length=100)
	fullname=models.CharField(max_length=100)
	designation=models.CharField(max_length=100)
	quote=models.TextField()

	class Meta:
		verbose_name="Testimonial"
		verbose_name_plural="Testimonials"

	def __str__(self):
		return self.fullname

#This is a contact model function
class Contact(models.Model):
	fullname=models.CharField(max_length=100)
	phone_number=models.CharField(max_length=15)
	email=models.EmailField(max_length=254)
	subject=models.CharField(max_length=200)
	message=models.TextField()

	class Meta:
		verbose_name="Contact"
		verbose_name_plural="Contacts"

	def __str__(self):
		return self.fullname