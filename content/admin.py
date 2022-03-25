from django.contrib import admin
from content.models import Profile, About, PrimarySkill, SecondarySkill, Service, Portfolio, Blog, Testimonial, Contact
#OR Use
#from content.models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(About)
admin.site.register(PrimarySkill)
admin.site.register(SecondarySkill)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(Contact)