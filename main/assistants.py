"""
In order not to load up much onto function views, refactoring is important 
so create your assistant classes or functions here.
"""
from django.http import Http404, HttpRequest
from random import choice, shuffle


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


def code_generator(length: int) -> str:
    """
    Generates a code with random digits and letters in provided length.
    """

    characters = '1234567890abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    output = []
    while len(output) < length:
        character = choice(characters)
        output.append(character)
    
    return ''.join(output)
