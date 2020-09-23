## Get Country code 

This repository contains **Dockerfile** of [app to check country code] for [Docker](https://www.docker.com/)'s.


### Base Docker Image

* [dockerfile/python](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile)


### Installation

1. Install [Docker](https://www.docker.com/).

2. Download [automated build](https://registry.hub.docker.com/u/dockerfile/nginx/) from public [Docker Hub Registry](https://registry.hub.docker.com/): `docker pull dockerfile/nginx`

   (alternatively, you can build an image from Dockerfile: `docker build -t="dockerfile/nginx" github.com/dockerfile/nginx`)


### Usage

    1. docker build -t countrycode --no-cache .
    2. docker run -d -p  80:5000 countrycode
    

#### Data Source

1. [TinyDB](https://tinydb.readthedocs.io/en/latest/) is used as infileDB


#### APIs exposed

1. /health: checks the health of application
2. /diag:  Raw data used
3. /convert/<string:name>: This converts the country name to country code
4. /convert_name/<string:code>: This converts the country code to country name

