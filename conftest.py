import os

import pytest
from dotenv import load_dotenv


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    load_dotenv()
    return {
        **browser_context_args,
        'base_url': os.getenv('BASE_URL'),
        'ignore_https_errors': True,
        'viewport': {
            'width': 1920,
            'height': 1080,
        }
    }
