from django.contrib.auth.models import User
from snippet.models import Snippet
from user_profile.models import UserProfile


def fill_database():
    # python run.py fill_database "fill_database()"

    User.objects.all().delete()
    UserProfile.objects.all().delete()
    Snippet.objects.all().delete()

    superuser = User.objects.create_superuser(username="root", email="root@root.root", password="PASSWORD")
    superuser.save()

    code = """
    
import requests
TELEGRAM_CRON_ADMIN_CHAT_IDS = [YOUR_CHAT_ID]

for chat_id in TELEGRAM_CRON_ADMIN_CHAT_IDS:
    requests.post(url="https://api.telegram.org/bot{}/{}".format("YOUR_API_TOKEN", "sendMessage"), data={"chat_id": chat_id, "text": f"Test PyScheduler"})
    
    """

    snippet = Snippet()
    snippet.title = "Test snippet"
    snippet.description = "Description test snippet"
    snippet.cron_time = "*/2 * * * *" # every 2 minutes
    snippet.code = code
    snippet.save()
    print(snippet.id)
