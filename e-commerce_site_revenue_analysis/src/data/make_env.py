from pathlib import Path
from typing import Dict
from io import StringIO
from dotenv import load_dotenv, dotenv_values
import logging


def main():
    load_dotenv()
    print(dotenv_values())

    logger = logging.getLogger(__name__)
    logger.info('Loading env files for project')
    logger.info(f'Variables: {dotenv_values()}')

if __name__ == "__main__":
    main()