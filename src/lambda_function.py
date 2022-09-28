import json
import boto3
import os
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    logger.info(json.dumps(event))
    
    aws_region_name = "us-east-1"
    
    # Criação de sessão para recuperar secrets
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=aws_region_name
    )
    
    try:
        # Recuepra secret
        # SECRET_DB_HOST = ARN da secret
        get_secret_string_db_host = client.get_secret_value(SecretId=os.getenv('SECRET_DB_HOST'))
        logger.info(json.dumps(get_secret_string_db_host, default=str))
        secret = get_secret_string_db_host['SecretString']
        logger.info(secret)


        # Secret json
        get_secret_Json_db_host = client.get_secret_value(SecretId=os.getenv('SECRET_PARAMETERS'))
        logger.info(json.dumps(get_secret_Json_db_host, default=str))
        secret_json = json.loads(get_secret_Json_db_host['SecretString'])
        logger.info(json.dumps(secret_json))
        logger.info(secret_json['lambda_ativo'])


            
    except Exception as e:
        logger.error('Erro ao recuperar secret!!')
        logger.error(e)
        raise e

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(secret)
    }
