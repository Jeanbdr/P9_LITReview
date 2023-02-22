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
        fields = ["ticket", "rating", "headline", "body"]

    def __init__(self, *args, **kwargs):
        self.ticket_id = kwargs.pop("ticket_id", None)
        super().__init__(*args, **kwargs)
        if self.ticket_id is not None:
            self.initial["ticket"] = self.ticket_id
            self.fields["ticket"].disabled = True


class OwnReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "headline", "body"]
