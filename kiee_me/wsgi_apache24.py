from django.core.wsgi import get_wsgi_application
from pathlib import Path

import os
import sys


path_home = str(Path(__file__).parents[1])
if path_home not in sys.path:
    sys.path.append(path_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'kiee_me.settings'

application = get_wsgi_application()