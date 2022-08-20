import binascii
import random
import struct
import time

import shortuuid
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from eth_account.messages import defunct_hash_message
from user_profile.models import UserProfile
from web3.auto import w3
from settings import ALLOWED_WALLETS
from settings import HOST


@csrf_exempt
def auth_web3(request):
    
    def short_hash(s):
        return binascii.b2a_base64(struct.pack("i", hash(s)))

    public_address = request.POST["accountAddress"]
    signature = request.POST["signature"]

    rightnow = int(time.time())
    sortanow = rightnow - (rightnow % 600)

    original_message = f"Signing in to {HOST} at {sortanow}"
    message_hash = defunct_hash_message(text=original_message)
    signer = w3.eth.account.recoverHash(message_hash, signature=signature)

    if signer not in ALLOWED_WALLETS:
        raise Http404

    if signer == public_address:

        uuid_1 = shortuuid.uuid()

        user_profile = UserProfile.objects.filter(eth_account_address=public_address).first()
        if user_profile:
            try:
                user = user_profile.user
            except:
                messages.add_message(request, messages.WARNING, "Profile not found")
                return HttpResponseRedirect(
                    reverse(
                        "main:user_login",
                    )
                )
            user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user)
            return HttpResponseRedirect(reverse("snippet:snippet_list"))

        else:
            password = "stFCcxD" + str(random.randint(10000000, 99999999))
            email = f"{uuid_1}@{HOST}"
            user = User.objects.create_user(email=email, username=uuid_1, first_name="Web3", last_name="Auth", password=password)

            user_profile = UserProfile()
            user_profile.user = user
            user_profile.name = f"Web3 Auth"
            user_profile.eth_account_address = public_address
            user_profile.save()

            user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user)

            messages.success(request, "Successful registration")
            return HttpResponseRedirect(reverse("snippet:snippet_list"))

    else:
        messages.add_message(request, messages.WARNING, "Refresh the page and try again")
        return HttpResponseRedirect(
            reverse(
                "main:user_login",
            )
        )


def user_login(request):
    if not request.user.is_authenticated:
        return render(request, "main/login.html")
    else:
        user = User.objects.get(id=request.user.id)
        user_profile = UserProfile.objects.filter(user=user).first()

        if user_profile:
            return HttpResponseRedirect(reverse("snippet:snippet_list"))
        else:
            logout(request)
            return render(request, "main/login.html")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("main:user_login"))


def handler404(request, *args, **argv):
    response = render(request, "404.html", {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, "500.html", {})
    response.status_code = 500
    return response
