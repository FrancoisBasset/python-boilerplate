#!/usr/bin/env python
from pokenux.tyradex import get_random_pokemon, get_pokemon_by_id

def main():
    pokemon_id = ''

    while pokemon_id != 'q':
        try:
            pokemon_id = input('Pokémon ID (empty for random) (q to quit) : ')
        except KeyboardInterrupt:
            print()
            exit()

        if pokemon_id == '':
            print(get_random_pokemon())
        elif pokemon_id.isdigit():
            print(get_pokemon_by_id(pokemon_id))

if __name__ == '__main__':
    main()
