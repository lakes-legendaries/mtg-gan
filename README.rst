#################
MTG Art Generator
#################

This is just a fun project to investigate using Generative Adverserial Networks
(GANs) to generate art, specifically for generating new MTG cards.

**********
Quickstart
**********

#. Prepare your environment. We tested this code using Python 3.9.

   .. code-block:: bash

      python -m venv .venv
      source .venv/bin/activate
      pip install --upgrade pip
      pip install -r requirements.txt

#. Get the necessary data file by going to `scryfall
   <https://scryfall.com/docs/api/bulk-data>`_ and downloading their
   :code:`Unique Artwork` file.

#. Fetch data with:

   .. code-block:: bash

      python mtggan/get_data.py

   This will output many card images to your :code:`data` folder.
