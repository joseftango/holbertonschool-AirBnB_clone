#!/usr/bin/python3

import uuid

print(dir(uuid)) # see module contains

x = uuid.uuid1()

print(uuid.uuid3(x, "name"))

print(uuid.uuid4())

