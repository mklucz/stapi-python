============
stapi-python
============

A python client for the Star Trek API http://stapi.co/

Installation
------------
.. code-block:: bash
   
    $ pip3 install stapi

Usage
-----

Searching for an entry:

.. code-block:: python
 
    >>> import stapi
    >>> criteria = stapi.search_criteria.AnimalSearchCriteria(0, 50, "", avian=True)
    >>> response = stapi.RestClient().animal.search(criteria)
    # response now contains results from the API, in this case the first fifty animals which are avians

Fetching an entry using an uid:

.. code-block:: python

   >>> import stapi
   >>> rest_client = stapi.RestClient()
   >>> loracus = rest_client.astronomicalObject.get("ASMA0000012319")
   >>> loracus.astronomicalObjectType
   'PLANET'
