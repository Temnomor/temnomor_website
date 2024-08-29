import platform

import uvicorn

from constants import HOST_PORT, SSL_CERTFILE_PATH, SSL_KEYFILE_PATH


def get_config() -> uvicorn.Config:
    uvicorn_config = {
        'app': 'main:app',
        'port': HOST_PORT,
        'log_level': 'info',
        'workers': 9,
        'forwarded_allow_ips': '*'
    }

    if platform.system().lower() == 'windows':
        return uvicorn.Config(**uvicorn_config)
    else:
        uvicorn_config['ssl_keyfile'] = SSL_KEYFILE_PATH
        uvicorn_config['ssl_certfile'] = SSL_CERTFILE_PATH
        return uvicorn.Config(**uvicorn_config)
