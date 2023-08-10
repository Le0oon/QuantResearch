from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(
        "mysql+pymysql://root:dress768596@localhost:3306/baostock",
)
Base = declarative_base()

class StockData(Base):
    __tablename__ = 'stock_data'
    id = Column(Integer, primary_key=True,autoincrement=True)
    TradingDay = Column(DateTime)
    SecuCode = Column(String(255))
    Time = Column(DateTime)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    amount = Column(Float)
    adjustflag = Column(String(255))


class StockData(Base):
    __tablename__ = 'stock_data_test'
    id = Column(Integer, primary_key=True,autoincrement=True)
    TradingDay = Column(DateTime)
    SecuCode = Column(String(255))
    Time = Column(DateTime)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    amount = Column(Float)
    adjustflag = Column(String(255))



if __name__ == "__main__":
    # Create the table
    Base.metadata.create_all(engine)

