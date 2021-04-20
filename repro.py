from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


url = "mssql+pyodbc://sa:yourStrong(!)Password@localhost:1433/repro?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(url)
SQLAlchemyInstrumentor().instrument(
    engine=engine,
)
Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))


def main():
    Base.metadata.drop_all(bind=engine)


if __name__ == "__main__":
    main()
