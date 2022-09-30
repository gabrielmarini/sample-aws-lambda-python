import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def getDDD(dddNumber):
    logger.info("DDD: %s" %(dddNumber))
    response = requests.get("https://brasilapi.com.br/api/ddd/v1/%s" %(dddNumber))

    dddData = response.json()

    return dddData