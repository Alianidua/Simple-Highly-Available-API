# HA simple API

Using `HAProxy` to make a basic `Python` `Flask` API higly available.

## Installation

1. Install `HAProxy`. For instance, with apt :

``` bash
apt install haproxy
```

2. Install `Flask` :

``` python
pip install Flask
```

## How to use

1. Start all servers in 3 different terminals :

``` bash
python simple_api_1.py
python simple_api_2.py
haproxy -f haproxy.cfg
```

2. Now, you can open the following links in your browser :

- <a href="http://localhost:5001/" target="_blank">http://localhost:5001/</a> is the first API
- <a href="http://localhost:5002/" target="_blank">http://localhost:5002/</a> is the second API
- <a href="http://localhost:5000/" target="_blank">http://localhost:5000/</a> is the load balancer

3. By default, `HAProxy` uses the Round Robin algorithm to distribute the load.
   So, when refreshing the page, you should alternate between simple API 1 & 2.

4. Stop one of the API (Ctrl+C). Now, refreshing the page will always redirect to the same API.

