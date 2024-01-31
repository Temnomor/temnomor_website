from multiprocessing import cpu_count

from constants import SSL_CERTFILE_PATH, SSL_KEYFILE_PATH, HOST_PORT


wsgi_app = 'main:app'

workers = cpu_count() * 2 + 1

worker_class = 'uvicorn.workers.UvicornWorker'

bind = f'127.0.0.1:{HOST_PORT}'

forwarded_allow_ips = '*'

keyfile = SSL_KEYFILE_PATH

certfile = SSL_CERTFILE_PATH

preload_app = True
