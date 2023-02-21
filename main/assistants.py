"""
In order not to load up much onto function views, refactoring is important 
so create your assistant classes or functions here.
"""
from django.http import Http404, HttpRequest


class Police:
    """
    A class with some methods for checking the incoming traffic.
    """

    def __init__(self):
        """
        Initialize the methods.
        """

    
    def check_superuser(self, request: HttpRequest):
        """
        Raises an Http404 if the request user is not superuser else does nothing.
        """

        if request.user.is_superuser:
            pass
        else:
            raise Http404
