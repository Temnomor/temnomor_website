from importlib import import_module
import os


api_routers = []

current_path = os.path.dirname(__file__)

for module in os.listdir(current_path):
    if not module.startswith('_'):
        module = module.replace('.py', '')
        router = import_module(f'.{module}', 'routers').router
        api_routers.append(router)

__all__ = ('api_routers',)
