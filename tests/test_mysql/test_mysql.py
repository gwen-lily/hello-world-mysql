"""Test the python-MySQL interface."""

import os
import logging

from mysql import connector
from mysql.connector.errors import ProgrammingError
from dotenv import load_dotenv
import pandas as pd

from src.mysql_hello_world.data import (
    CSV_SEP,
    ENV_VAR_USER_NAME,
    ENV_VAR_USER_PASS,
    ROOT_DIR,
    TEST_DATA_PATH,
    TEST_DATABASE_NAME,
    TEST_TABLE_NAME,
)

# setup

logging.getLogger(__name__)
load_dotenv(ROOT_DIR)

_CONFIG_PATH = "../../conf"

_HOST = "localhost"
assert _HOST is not None

_USER = os.getenv(ENV_VAR_USER_NAME)
_PASSWD = os.getenv(ENV_VAR_USER_PASS)

try:
    DB = connector.connect(host=_HOST, user=_USER, passwd=_PASSWD, database=TEST_DATABASE_NAME)

except ProgrammingError:
    DB = connector.connect(host=_HOST, user=_USER, passwd=_PASSWD)

    _cursor = DB.cursor()
    q1 = f"CREATE DATABASE {TEST_DATABASE_NAME}"
    _cursor.execute(q1)

    DB.disconnect()
    DB = connector.connect(host=_HOST, user=_USER, passwd=_PASSWD, database=TEST_DATABASE_NAME)


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
    q1 = f"CREATE DATABASE {TEST_DATABASE_NAME}"

    try:
        cursor.execute(q1)
    except connector.errors.DatabaseError:
        test_drop_database()


def test_create_table():
    """Create a test table."""
    cursor = DB.cursor()
    q1 = f"CREATE TABLE {TEST_TABLE_NAME} (personID int PRIMARY KEY AUTO_INCREMENT, name varchar(50), wallet BIGINT, region varchar(2))"

    try:
        cursor.execute(q1)
    except ProgrammingError:
        pass


def test_insert_into_table():
    """Create some data for the test table."""
    cursor = DB.cursor()

    q1 = f"INSERT INTO {TEST_TABLE_NAME} (name, wallet, region) VALUES (%s,%s,%s)"

    df = pd.read_csv(TEST_DATA_PATH.joinpath("boosters.csv"), sep=CSV_SEP)
    values = list(df.itertuples(index=False, name=None))

    cursor.executemany(q1, values)
    DB.commit()


def test_describe_table():
    """Describe the test table"""

    cursor = DB.cursor()
    q1 = f"DESCRIBE {TEST_TABLE_NAME}"

    cursor.execute(q1)


def test_drop_database():
    """Drop the test database."""
    cursor = DB.cursor()
    Q1 = f"DROP DATABASE {TEST_DATABASE_NAME}"

    cursor.execute(Q1)
