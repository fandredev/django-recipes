from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.http import Http404
from authors.forms import RegisterForm
from django.contrib import messages
from django.urls import reverse


def register_view(request: HttpRequest):
    register_form_data = request.session.get("register_form_data", None)
    form = RegisterForm(register_form_data)

    return render(
        request,
        "authors/pages/register_view.html",
        {"form": form, "form_action": reverse("authors:create")},
    )


def register_create(request: HttpRequest):
    POST = request.POST

    if not POST:
        raise Http404("Invalid request")

    request.session["register_form_data"] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, "User registered successfully")

        del request.session["register_form_data"]

    return redirect("authors:register")
