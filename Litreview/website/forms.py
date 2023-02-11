from django import forms
from website.models import Ticket, Review
from django.contrib.auth import get_user_model


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["ticket", "rating", "headline", "body", "user"]


User = get_user_model()


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["follows"]
