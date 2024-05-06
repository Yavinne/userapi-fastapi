from fastapi import FastAPI
import uvicorn
from model import Base, User

user_api = FastAPI()


@user_api.get("/users/{user_id}")
async def read_user(user_id: int):
    return User.read(user_id)

@user_api.post("/add")
async def create_user(name, gender, avatar, details):
    return User.create(name, gender, avatar, details)

@user_api.put("/update/{user_id}")
async def update_user(user_id: int, new_data: dict):
    return User.update(user_id, new_data)

@user_api.delete("/delete/{user_id}")
async def delete_user(user_id: int):
    return User.delete(user_id)

# Lancement du serveur uvicorn lorsque le fichier est exécuté directement
if __name__ == "__main__":
    uvicorn.run(user_api, host="127.0.0.1", port=8000)