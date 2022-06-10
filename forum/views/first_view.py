from django.http import HttpResponse
from ..models.user import humans_generator

def users_generator(request, number_of_users=100):
    
    return HttpResponse('<br>'.join(humans_generator(users=number_of_users)))