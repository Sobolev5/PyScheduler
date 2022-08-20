from user_profile.models import UserProfile


class GetUserData:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        if hasattr(user, "id") and user.id:

            try:
                user_profile = UserProfile.objects.get(user=user)
            except:
                user_profile = None

            if user_profile:
                request.user_profile = user_profile

        response = self.get_response(request)
        return response
