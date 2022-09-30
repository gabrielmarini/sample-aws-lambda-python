from asyncio import events
import json
import logging
from lib.dddService import getDDD
from lib.requests import getCEP


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    logger.info(json.dumps(event))

    cep = getCEP(event['cep'])

    if cep is None:
        return {
            'statusCode': 400,
            'message': 'Cep não encontrado'
        }
    else:
        listddd = getDDD('11')
        return {
            'CEP': cep,
            'DDD': listddd
        }
