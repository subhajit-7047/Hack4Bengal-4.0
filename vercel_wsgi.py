import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "toy.settings")  # replace 'toy' with your project folder name
app = get_wsgi_application()
