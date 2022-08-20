from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import reverse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@login_required(login_url="/")
def edit_profile(request):

    if request.method == "POST" and "edit_profile_form" in request.POST:

        # User
        request.user.first_name = request.POST["first_name"]
        request.user.last_name = request.POST["last_name"]
        request.user.save()

        # UserProfile
        request.user_profile.name = f"{request.user.first_name} {request.user.last_name}"
        request.user_profile.name = f"{request.user.first_name} {request.user.last_name}"
        request.user_profile.save()

        messages.success(request, "Profile successfully edited")
        return HttpResponseRedirect(reverse("user_profile:edit_profile"))

    if request.method == "DELETE":

        with transaction.atomic():

            messages.success(request, "Profile successfully deleted")
            logout(request)
            return JsonResponse({"delete": 1})

    d = {}
    d["profile_nav_menu"] = True
    return render(request, "user_profile/edit_profile.html", d)
