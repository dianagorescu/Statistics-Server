import logging
from logging.handlers import RotatingFileHandler

# Configurați logging-ul
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('webserver.log', maxBytes=1024*1024, backupCount=5)
    ]
)

# Crearea unui logger
logger = logging.getLogger('webserver')

# Exemplu de logare cu nivelul INFO
logger.info('Aceasta este o intrare de log cu nivelul INFO')

# Exemplu de logare cu nivelul ERROR
logger.error('Aceasta este o intrare de log cu nivelul ERROR')