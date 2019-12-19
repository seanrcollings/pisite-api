import sys
sys.path.append('/var/www/pisite')

from app import create_app
from app.config import ProdConfig
application = create_app(ProdConfig)

