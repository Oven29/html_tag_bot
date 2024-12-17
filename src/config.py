import logging
import dotenv
import os
import pathlib
from typing import Final, Optional


ROOT_DIR: Final[str] = pathlib.Path(__file__).parents[1]
dotenv.load_dotenv(
    dotenv_path=os.path.join(ROOT_DIR, '.env'),
    override=True,
    encoding='utf-8',
)

BOT_TOKEN: Final[str] = os.getenv('BOT_TOKEN')

LOGGING_LEVEL: Final[str] = logging._nameToLevel.get(os.getenv('LOGGING', 'INFO').upper(), logging.INFO)

BOT_USERNAME: Optional[str] = ...

LOGS_DIR: Final[str] = os.path.join(ROOT_DIR, 'logs')
