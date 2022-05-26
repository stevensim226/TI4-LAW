# Installation Guide
1. Make sure `python3` and `pip3` is installed
2. Install the requirements using `pip3 install -r requirements.txt`
3. Run each microservice using `python3 read_svc.py` and `python3 update_svc.py`

# NGINX Configuration Guide
1. Make sure NGINX is installed in your machine
2. Paste the config inside `proxy_w_cache.conf` into `nginx.conf`'s `http` directive or to another file that has been included to the original config
3. Make sure you have `/data/nginx/cache` directory on your machine