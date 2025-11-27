from fastapi import FastAOI, HTTPException
from pydantic import BaseModel

app=FastAPI(title="Vet Clinic API")

class Dog(BaseModel):
  id: int
  name: str
  age: int
  breed: str
dogs_db={}

@app.get("/dog")
def get_dogs():
  return list(dogs_db.values())
@app.post("/dogs")
def create_dog(dog: Dog):
  if dog.id in dogs_db:
    raise HTTPException(status_code=400, detail="Dog already exists")
    dogs_db[dog.id]=dog
    return dog
@app.get("/dogs/{dog_id}")
def get_dog(dog_id: int):
    if dog_id not in dogs_db:
        raise HTTPException(status_code=404, detail="Dog not found")
    return dogs_db[dog_id]

@app.put("/dogs/{dog_id}")
def update_dog(dog_id: int, dog: Dog):
    if dog_id not in dogs_db:
        raise HTTPException(status_code=404, detail="Dog not found")
    dogs_db[dog_id] = dog
    return dog

@app.delete("/dogs/{dog_id}")
def delete_dog(dog_id: int):
    if dog_id not in dogs_db:
        raise HTTPException(status_code=404, detail="Dog not found")
    del dogs_db[dog_id]
    return {"message": "Dog deleted"}
