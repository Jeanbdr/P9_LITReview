from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models

# Create your views here.
@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    return render(request, "website/home.html", context={"tickets": tickets})


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            # set the uploader to the user before saving the model
            ticket.uploader = request.user
            # now we can save
            ticket.save()
            return redirect("home")
    return render(request, "website/create_ticket.html", context={"form": form})


@login_required
def create_review(request):
    form = forms.ReviewForm()
    if request.method == "POST":
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "website/create_review.html", context={"form": form})


@login_required
def create_own_review(request):
    ticket_form = forms.TicketForm
    review_form = forms.ReviewForm
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.uploader = request.user
            ticket.save()
            review_form.save()
            return redirect("home")
    context = {
        "ticket_form": ticket_form,
        "review_form": review_form,
    }
    return render(request, "URL", context=context)
