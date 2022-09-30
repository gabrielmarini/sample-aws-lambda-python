import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def getCEP(cepNumber):
    logger.info("Cep: %s" %(cepNumber))
    response = requests.get("https://brasilapi.com.br/api/cep/v2/%s" %(cepNumber))

    cep = response.json()

    return cep