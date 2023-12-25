:html_theme.sidebar_secondary.remove:

#################
Random Collection
#################

.. toctree::
   :hidden:

   books

Build instructions
##################

RanDoc is available on https://github.com/grembeter/randoc. You need :program:`python3` to built it
from scratch:

.. code-block:: shell

   git clone https://github.com/grembeter/randoc
   cd randoc
   python3 -m venv .venv
   source .venv/bin/activate
   python3 -m pip install -r requirements.txt

   make -C docs/ html
   make -C docs/ latexpdf

Open :file:`docs/build/html/index.html` page in browser.
