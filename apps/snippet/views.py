import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import reverse
from django.views.decorators.csrf import csrf_exempt
from snippet.models import Snippet


@csrf_exempt
@login_required(login_url="/")
def snippet_list(request):

    d = {}
    d["snippets"] = Snippet.objects.all().order_by("active", "creation_date")
    d["snippet_nav_menu"] = True

    return render(request, "snippet/snippet_list.html", context=d)


@csrf_exempt
@login_required(login_url="/")
def snippet_edit(request, snippet_id=None):

    if snippet_id:
        try:
            snippet = Snippet.objects.get(id=snippet_id)
        except:
            raise Http404
    else:
        snippet = None

    if request.method == "POST" and "execute" in request.POST and snippet:
        try:
            exec(snippet.code)
        except Exception as e:
            messages.error(request, str(e))
        snippet.last_execution_date = datetime.datetime.now()
        snippet.save()

    if request.method == "POST" and not "execute" in request.POST:
        if not snippet:
            snippet = Snippet()

        snippet.user_profile = request.user_profile
        snippet.title = request.POST.get("title", "snippet")
        snippet.description = request.POST.get("description", "description")
        snippet.cron_time = request.POST.get("cron_time", "*/2 * * * *")
        snippet.code = request.POST.get("code", "print('hello')")
        active = request.POST.get("active", "off")
        if active == "on":
            snippet.active = True
        else:
            snippet.active = False
        snippet.save()

        messages.success(request, "%s" % "Snippet sucessfully changed")
        return HttpResponseRedirect(reverse("snippet:snippet_edit", kwargs={"snippet_id": snippet.id}))

    if request.method == "DELETE":
        snippet.delete()
        messages.success(request, "%s" % "Snippet sucessfully deleted")
        return JsonResponse({"delete": 1})

    d = {}
    d["snippet"] = snippet
    d["snippet_nav_menu"] = True

    return render(request, "snippet/snippet_edit.html", context=d)
