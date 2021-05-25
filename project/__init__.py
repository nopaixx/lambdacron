from project.db import db, init_db
from project.secrets import Secrets
from project.tables import Pedidos

init_db(Secrets())


def lambda_handler(event, context):

    pedidos = db.session.query(Pedidos).filter_by(field_name='condition').all()


    ret = [pedido.doSomething() for pedido in pedidos]

    return {
         ‘statusCode’: 200,
         ‘body’: json.dumps(ret)
     }
