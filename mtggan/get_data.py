import json
from os import listdir
import re
from subprocess import run
from time import sleep


def get_card_images(card_list: str = 'data/artwork.json'):
    """Pull card images from server

    This function uses the scryfall api and saves all card images in the
    :code:`data` folder.

    Parameters
    ----------
    card_list: str
        Name of the file containing the artwork data and urls. This can be
        obtained by going to `scryfall
        <https://scryfall.com/docs/api/bulk-data>`_ and downloading their
        :code:`Unique Artwork` file.
    """

    # import list of cards
    cards = json.load(open(card_list, 'r'))

    # download images
    for card in cards:

        # try to wget each image
        try:

            # get ofname
            name = re.sub('[^a-zA-Z0-9]+', '_', card['name'])
            count = len([
                file
                for file in listdir('data')
                if file.startswith(name)
            ])
            suffix = f'-{count}' if count else ''
            ofname = f'data/{name}{suffix}.jpg'

            # get image
            run(
                [
                    'wget',
                    card['image_uris']['normal'],
                    '-O',
                    ofname,
                ],
                capture_output=True,
                check=True,
            )

        # ignore missing data
        except KeyError:
            pass

        # don't overload scryfall api
        sleep(0.1)


if __name__ == '__main__':
    get_card_images()
