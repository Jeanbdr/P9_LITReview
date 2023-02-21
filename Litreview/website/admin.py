from django.contrib import admin
from website.models import Ticket, Review, OwnReview

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(OwnReview)
