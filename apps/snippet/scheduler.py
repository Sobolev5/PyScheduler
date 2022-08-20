import datetime

from croniter import croniter
from snippet.models import Snippet


def run_snippets():
    # python run.py snippet.scheduler "run_snippets()"

    datetime_now = datetime.datetime.now()
    snippets_ids = []
    for snippet_slice in Snippet.objects.filter(active=True).values_list("id", "cron_time"):
        snippet_id = snippet_slice[0]
        cron_time = snippet_slice[1]
        if croniter.is_valid(cron_time) and croniter.match(cron_time, datetime_now):
            snippets_ids.append(snippet_id)

    if snippets_ids:
        for snippet in Snippet.objects.filter(id__in=snippets_ids):
            try:
                exec(snippet.code)
                snippet.last_execution_date = datetime.datetime.now()
                snippet.save()
            except:
                continue
