import os

algo = os.listdir('algo')
for a in algo:
    if a.endswith('.py') and a != '__init__.py':
        exec('from . import {}'.format(a[:-3]))