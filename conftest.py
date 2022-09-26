import os

import pytest

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_REPORT_PATH = os.path.join(ROOT_DIR, 'html_report', 'report.html')


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = HTML_REPORT_PATH
