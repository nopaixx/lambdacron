import db
from sqlalchemy import Column, Integer, String

class Pedidos(db.Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True)
    fieldname = Column(String(50), nullable=False)


    def doSomething(self):
        """
        Do somthing with this pedido
        implementa aqui lo que quieras.... con este pedido
        """
        # ...

        return {
                    "PedidoId": self.id
                    "status": "SUCESS_PROCESSED"
                }
