import pandas as pd
from sqlalchemy import *
from sqlalchemy.orm import *

db_name = 'ass'

#set up database and tables
try:
    #create engine
    engine = create_engine(f'mysql+pymysql://root@localhost/{db_name}', echo=True)

    #drop database if it exists and then recreate and use it
    with engine.connect() as conn:
        conn.execute(text(f"DROP SCHEMA IF EXISTS {db_name}"))
        conn.execute(text(f"CREATE DATABASE {db_name}"))
        conn.execute(text(f"USE {db_name}"))

    #declare mapping between data and database
    Base = declarative_base()

    #create mapped classes
    class Constituency(Base):
        __tablename__ = 'constituency'
        c_id = Column(Integer, primary_key=True)
        c_name = Column(String(100), nullable=False)
        c_mp_fname = Column(String(50), nullable=False)
        c_mp_sname = Column(String(50), nullable=False)

        #create relationship with station table
        stations_c = relationship('Station', back_populates='constituencies_s')
    
    class Station(Base):
        __tablename__ = 'station'
        s_id = Column(Integer, primary_key=True)
        c_id_fk = Column(Integer, ForeignKey('constituency.c_id'), nullable=False)
        s_name = Column(String(100), nullable=False)
        s_lat = Column(Float, nullable=False)
        s_long = Column(Float, nullable=False)
        
        #create relationship with constituency table and reading table
        constituencies_s = relationship('Constituency', back_populates='stations_c')
        readings_s = relationship('Reading', back_populates='stations_r')

    class Reading(Base):
        __tablename__ = 'reading'
        r_id = Column(Integer, primary_key=True)
        s_id_fk = Column(Integer, ForeignKey('station.s_id'), nullable=False)
        r_date_time = Column(DateTime, nullable=False)
        r_nox = Column(Float)
        r_no2 = Column(Float)
        r_no = Column(Float)
        r_pm10 = Column(Float)
        r_o3 = Column(Float)
        r_temperature = Column(Float)
        r_objectid = Column(Integer)
        r_nvpm10 = Column(Float)
        r_vpm10 = Column(Float)
        r_nvpm2_5 = Column(Float)
        r_pm2_5 = Column(Float)
        r_vpm2_5 = Column(Float)
        r_co = Column(Float)
        r_rh = Column(Float)
        r_pressure = Column(Float)
        r_so2 = Column(Float)
        
        #create relationship with station table
        stations_r = relationship('Station', back_populates='readings_s')

    class MetadataSchema(Base):
        __tablename__ = 'metadata_schema'
        m_id = Column(Integer, primary_key=True)
        m_measure = Column(String(25), nullable=False)
        reading_column_name = Column(String(25), nullable=False)
        m_desc = Column(String(150), nullable=False)
        m_unit = Column(String(25), nullable=False)

    # create tables
    Base.metadata.create_all(engine)

except Exception as e:
    print(f'Database setup failed: {e}')

#import data from csv files to populate supporting tables (constituency, station, and metadata_schema)

#get file paths of csvs
constituency_data = '/constituency.csv'
station_data = '/station.csv'
measure_data = '/metadata_schema.csv'

try:
    #read data
    c_df = pd.read_csv(constituency_data)
    s_df = pd.read_csv(station_data)
    m_df = pd.read_csv(measure_data)

    #insert data into tables
    with engine.connect() as conn:
        c_df.to_sql('constituency', con=conn, index=False, if_exists='append')
        s_df.to_sql('station', con=conn, index=False, if_exists='append')
        m_df.to_sql('metadata_schema', con=conn, index=False, if_exists='append')

    print('Data imported successfully')

except Exception as e:
    print(f'Data import failed: {e}')

#import data from csv file to populate reading table with cleansed cropped data

#get file path of csv
reading_data = '/cropped_data.csv'

try:
    #read data
    r_df = pd.read_csv(reading_data)

    #insert data into table
    with engine.connect() as conn:
        r_df.to_sql('reading', con=conn, index=False, if_exists='append')

    print('Data imported successfully')

except Exception as e:
    print(f'Data import failed: {e}')