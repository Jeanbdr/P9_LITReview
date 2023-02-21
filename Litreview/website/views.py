from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.db.models import Q
from authentication.models import User
from website.models import Ticket, Review, OwnReview
from django.views.generic import ListView
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    tickets = models.Ticket.objects.filter(Q(user__in=request.user.following.all()))
    return render(request, "website/home.html", context={"tickets": tickets})


@login_required
def profile(request, pk):
    if request.user.is_authenticated:
        profile = User.objects.get(id=pk)
        tickets = Ticket.objects.filter(user_id=pk)
        reviews = Review.objects.filter(user_id=pk)
        return render(
            request,
            "website/profile.html",
            context={"profile": profile, "tickets": tickets, "reviews": reviews},
        )


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("home")
    return render(request, "website/create_ticket.html", context={"form": form})


@login_required
def create_review(request, pk):
    form = forms.ReviewForm(ticket_id=pk)
    if request.method == "POST":
        form = forms.ReviewForm(request.POST, ticket_id=pk)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("home")
    return render(request, "website/reviewing.html", context={"form": form})


@login_required
def create_own_review(request):
    review_form = forms.OwnReviewForm()
    if request.method == "POST":
        review_form = forms.OwnReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("home")
    return render(
        request, "website/create_review.html", context={"review_form": review_form}
    )


@login_required
def follow_users(request):
    current_user = request.user
    if request.method == "POST":
        search_query = request.POST.get("search_box")
        searched_user = User.objects.filter(username=search_query).values()
        action = request.POST["follow"]
        if searched_user:
            if action == "follow":
                current_user.following.add(searched_user[0]["id"])
        else:
            user = request.POST.get("follow")
            jesus = User.objects.filter(username=user).values()
            if user.__eq__(jesus):
                current_user.following.remove(jesus[0]["id"])
        context = {"searched_query": search_query, "searched_user": searched_user}
        return render(request, "website/follower.html", context)
    return render(request, "website/follower.html")


@login_required
def update_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    form = forms.TicketForm(instance=ticket)
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            # set the uploader to the user before saving the model
            ticket.user = request.user
            # now we can save
            ticket.save()
        return redirect("home")
    return render(
        request,
        "website/update.html",
        context={"form": form},
    )


@login_required
def delete_ticket(request, pk):
    item = Ticket.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("home")
    return render(request, "website/delete.html", {"item": item})


@login_required
def update_review(request, pk):
    review = Review.objects.get(id=pk)
    form = forms.ReviewForm(instance=review)
    if request.method == "POST":
        form = forms.ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
        return redirect("home")
    return render(
        request,
        "website/update_review.html",
        context={"form": form},
    )


@login_required
def delete_review(request, pk):
    item = Review.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("home")
    return render(request, "website/delete_review.html", {"item": item})
