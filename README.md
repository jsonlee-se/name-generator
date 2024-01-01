# Name Generator API

This project provides a simple API for generating random names. It includes two types of name generators: a general name generator and a Pokémon-themed name generator.

## Files

- `api.py`: This is the main file that sets up the web endpoints for the name generators.
- `name_generator.py`: This file contains the logic for generating a random name by combining an adjective and an animal name.
- `poke_name_gen.py`: This file contains the logic for generating a random Pokémon-themed name by combining a nature and a Pokémon name.

## API Endpoints

- `get_name`: This endpoint returns a randomly generated name from the general name generator.
- `get_pokemon_name`: This endpoint returns a randomly generated name from the Pokémon-themed name generator.

## License

This project is licensed under the MIT License. For more details, see the [`LICENSE`](LICENSE) file.

## Usage

To use this API, you need to call the desired endpoint. Here's an example of how to use the `get_name` endpoint:

```python
import requests

response = requests.get('http://localhost:5000/get_name')
print(response.json())
```

Replace `'http://localhost:5000/get_name'` with the URL of your deployed API.

## Development

To run the project locally, you need to have Python installed and the modal package. Then, you can run the `api.py` file:

```sh
modal deploy api.py
```

This will start a modal endpoint, and you can access the API endpoints given by modal in the terminal.
