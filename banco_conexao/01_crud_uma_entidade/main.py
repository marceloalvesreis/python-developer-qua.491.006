# importar a biblioteca sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

try:
    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")
    Base = declarative_base()

    class Pessoa(Base):
        __tablename__ = "pessoa"

        id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String, nullable=False)
        email = Column(String, nullable=False, unique=True)
        data_nascimento = Column(Date, nullable=False)

    Base.metadata.create_all(engine)
    
    # NOTE: engine para o Mysql
    # engine = create_engine("mysql+mysqlconnector://senha:root@localhost:3306/nome_do_banco")
except Exception as e:
    print(f"Não foi possível conectar ao banco. {e}")