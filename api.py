from modal import Stub, web_endpoint

import name_generator as ng
import poke_name_gen as png

stub = Stub("name_generator")

@stub.function()
@web_endpoint()
def get_name():
    return ng.generate_name()
    

@stub.function()
@web_endpoint()
def get_pokemon_name():
    return png.generate_name()
