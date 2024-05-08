from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.http import Http404
from authors.forms import RegisterForm


def register_view(request: HttpRequest):
    register_form_data = request.session.get("register_form_data", None)
    form = RegisterForm(register_form_data)

    return render(request, "authors/pages/register_view.html", {"form": form})


def register_create(request: HttpRequest):
    POST = request.POST

    if not POST:
        raise Http404("Invalid request")

    request.session["register_form_data"] = POST
    form = RegisterForm(POST)

    return redirect("authors:register")
