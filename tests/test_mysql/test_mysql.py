"""Test the python-MySQL interface."""

import os
import logging

from mysql import connector
from dotenv import load_dotenv

from src.mysql_hello_world.data import ENV_VAR_USER_NAME, ENV_VAR_USER_PASS, ROOT_DIR

# setup

logging.getLogger(__name__)
load_dotenv(ROOT_DIR)

_CONFIG_PATH = "../../conf"

_HOST = "localhost"
assert _HOST is not None

_USER = os.getenv(ENV_VAR_USER_NAME)
_PASSWD = os.getenv(ENV_VAR_USER_PASS)

# TODO: Catch certain exceptions
DB = connector.connect(host=_HOST, user=_USER, passwd=_PASSWD, database="testdb")

del _USER, _PASSWD  # cleanup

# tests


def test_connect():
    """This ensures the database is reachable"""
    assert DB is not None


def test_env_variables():
    """test importing environment variables."""
    user = os.getenv(ENV_VAR_USER_NAME)
    passwd = os.getenv(ENV_VAR_USER_PASS)

    assert user is not None
    assert passwd is not None


def test_create_database():
    """Create a test database."""
    cursor = DB.cursor()
    # cursor.execute("CREATE DATABASE testdb")
