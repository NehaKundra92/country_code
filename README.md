## Get Country code 

This repository contains **[Dockerfile](https://github.com/NehaKundra92/country_code/blob/master/Dockerfile)** of [CountryCodeLookUp](https://github.com/NehaKundra92/country_code/blob/master/code/lookup.py).


### Base Docker Image

* [dockerfile/python](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile)


### Installation

1. Install [Docker](https://www.docker.com/).

   


### Usage

    1. docker build -t countrycode --no-cache .
    2. docker run -d -p  80:5000 countrycode
    3. curl localhost/health
    4. curl localhost/diag
    5. curl localhost/convert/India
    6. curl localhost/convert_name/AU
    
    

### Data Source

   1. [TinyDB](https://tinydb.readthedocs.io/en/latest/) is used as infileDB


#### APIs exposed

   1. /health: checks the health of application
   2. /diag:  Raw data used
   3. /convert/<string:name>: This converts the country name to country code
   4. /convert_name/<string:code>: This converts the country code to country name






![Example](https://github.com/NehaKundra92/country_code/blob/master/curl.png?raw=true "Example")
