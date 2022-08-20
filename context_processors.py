from settings import HOST
from settings import HOST_PRETTY

def common(request):
    return {
        "HOST": HOST,
        "HOST_PRETTY": HOST_PRETTY,
    }
