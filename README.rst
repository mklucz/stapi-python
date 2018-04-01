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
.. code-block:: python
 
    import stapi
    criteria = stapi.search_criteria.AnimalSearchCriteria(0, 50, "", avian=True)
    response = stapi.RestClient().animal.search(criteria)
    # response now contains results from the API, in this case the first fifty animals which are avians
