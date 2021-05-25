import boto3
import os
from botocore.exceptions import ClientError


class Secrets:

    def __init__(self):

        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name,
        )
    
        secret_name = os.environ.get("SECRETMANAGER_NAME_TO_USER","ENV-COMPANY-DEPT-PROJECT")


    def getDbURI(self):

        return self.client.get_secret_value(
                SecretId=self.secret_name
            ).get('DBURI')

    def getDbUser(self):

        return self.client.get_secret_value(
                SecretId=self.secret_name
            ).get('DBUSER')

    def getDbPwd(self):

        return self.client.get_secret_value(
                SecretId=self.secret_name
            ).get('DBPWD')
