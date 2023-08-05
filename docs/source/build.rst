==================
Build instructions
==================

RanDoc is available on https://github.com/grembeter/randoc

.. code-block:: shell
   :linenos:

   git clone https://github.com/grembeter/randoc
   cd randoc
   python3 -m venv .venv
   source .venv/bin/activate
   python3 -m pip install -r requirements.txt

   make -C docs/ html
   make -C docs/ latexpdf

Open ``docs/build/html/index.html`` page in browser.
