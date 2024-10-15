from pathlib import Path
from pandas import DataFrame
from sqlalchemy import create_engine
from pathlib import Path
from dotenv import dotenv_values
from typing import Dict


def load(dataframes: Dict[str, DataFrame]):
    # Create .sql file
    Path(dotenv_values()["SQLITE_BD_ABSOLUTE_PATH"]).touch()

    # DB Engine
    db_engine = create_engine(rf"sqlite:///{dotenv_values()["SQLITE_BD_ABSOLUTE_PATH"]}", echo=False)

    # Create table for each dataset
    for dataframe_key, dataframe in dataframes.items():
        print(dataframe_key)
        dataframe.to_sql(name=dataframe_key, con=db_engine, if_exists="replace")
    
    return db_engine