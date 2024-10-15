from pandas import DataFrame, read_csv, read_json, to_datetime
from typing import Dict
from .enums import TableEnum
from dotenv import dotenv_values
import requests

def extract(year: int, csv_folder: str = dotenv_values()["DATASET_ROOT_PATH"]) -> Dict[str, DataFrame]:
    table_mappings = list(TableEnum)
    dataframes = {}
    for mapping in table_mappings:
        name = mapping.name
        file_path = mapping.value
        dataframes[name] = read_csv(csv_folder+file_path)
    dataframes["public_holidays"] = get_public_holidays(year)
    return dataframes

def get_public_holidays(year: int) -> DataFrame:
    public_holidays_url = dotenv_values()["PUBLIC_HOLIDAYS_URL"]
    response = requests.get(public_holidays_url + '/{0}/BR'.format(year))
    data = read_json(response.text)
    data["date"] = to_datetime(data["date"])
    data = data.drop(['types', 'counties'], axis=1)
    return data