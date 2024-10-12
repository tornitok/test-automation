from typing import Final
from dotenv import load_dotenv
import os

load_dotenv()


class Secrets:
    USER_NAME: Final[str] = os.getenv('USER_NAME')
    PASSWORD: Final[str] = os.getenv('PASSWORD')

class URL:
    BASE_URL = 'https://toghrulmirzayev.github.io/ui-simulator'
    INDEX_PAGE = f'{BASE_URL}/index.html'
    HOVER_AND_SELECT_PAGE = f'{BASE_URL}/hover_and_select.html'
    CHECK_AND_VALIDATE = f'{BASE_URL}/check_and_validate.html'
