# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from .extract import extract
from .load import load
from dotenv import dotenv_values


#@click.command()
#@click.argument('input_filepath', type=click.Path(exists=True))
#@click.argument('output_filepath', type=click.Path())
#@click.argument('return_engine', type=click.BOOL)
def main(input_filepath, output_filepath, return_engine=False):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    #project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    # load_dotenv(find_dotenv())

    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    logger.info('Extracting data into dataframes')
    dataframes = extract(2017)
    logger.info('Done!')

    logger.info("Loading DataFrames to Data Warehouse in SQLite")
    db_engine = load(dataframes)
    logger.info('Done!')

    if return_engine == True:
        logger.info('return_engine=True, returning DB Engine...')
        return db_engine


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    #load_dotenv(find_dotenv())

    main()
