#import aiofiles

import asyncio

from fastapi import FastAPI
#from pydantic import BaseModel
from pydantic.dataclasses import dataclass

app = FastAPI()

# https://docs.python.org/3/library/math.html
from math import pi, sqrt

#import os
from os import system

# https://realpython.com/python-data-classes/
# http://zetcode.com/python/dataclass/
from dataclasses import dataclass

@dataclass(frozen=True)
class Circle:
    name: str = "NULL"
    diameter: float = 0.0 #Variable annotations: https://www.python.org/dev/peps/pep-0526/

#    async def diameterInput(self):
#        self.name = str("Circle")
#        self.diameter = float

    async def diameterCalculations(self):
        self.radius = float(self.diameter /2)
        self.area = float(pi * sqrt(self.radius))
        self.circumference = float(2 * pi * self.radius)
        print("Radius ", self.radius)
        #print("Area: ", self.area)
        #print("Circumference: ", self.circumference)

@dataclass
class Rectangle:
    name: str = "NULL"
    side1: float = 0.0
    side2: float = 0.0
    
    async def rectangleInput(self):
        self.side1 = float(input("Input the first side of two: "))
        self.side2 = float(input("Input the first side of two: "))
        self.name = str("Rectangle")

# GET request for root.
@app.get("/")
async def root_get():
   return {"message": "All your GET is belong to us."}

# POST request for root.
@app.post("/")
async def root_post():
    return {"message": "All your POST is belong to us."}

# GET request for /circle.
@app.get("/circle/{id}")
async def post_item(id: str):
    Circle(2)

#prepare_for_foo()
#task = loop.create_task(foo())
#remaining_work_not_depends_on_foo()
#loop.run_until_complete(task)

##loop = asyncio.get_event_loop()

def main():
    c = Circle('a', 33.0)   # This must finish before print.
#    printCircle(c)          # https://www.python.org/dev/peps/pep-0492/#types-coroutine
#    print(circle)
    print(Circle.diameterCalculations(c))


#if __name__ == "__main__":
#    asyncio.run(main())


def adder(i1, i2):
  #return i1 + i2
  return i1 + i2
