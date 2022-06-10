from typing import NamedTuple
from faker import Faker

fake = Faker()

class Human(NamedTuple):
    name: str
    email: str

def human_generator():
    name = fake.first_name()
    email = fake.unique.ascii_email()
    return f'{name} {email}'

def humans_generator(users=100):
    for _ in range(users):
        yield human_generator()
        