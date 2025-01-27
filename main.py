from fastapi import FastAPI

import name_generator as ng
import poke_name_gen as png

app = FastAPI()


@app.get("/names")
def get_name():
    return {"name": ng.generate_name()}


@app.get("/pokenames")
def get_pokemon_name():
    return {"name": png.generate_name()}
