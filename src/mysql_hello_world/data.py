"""Ubiquitous data for the module."""

from pathlib import Path

# project root relative to the data file
ROOT_DIR = Path(__file__).parents[2]

# store your access information as environment variables on your local system
# https://www.twilio.com/blog/environment-variables-python
# follow the "Using .env files" header

ENV_VAR_USER_NAME = "MYSQL_USER_NAME"
ENV_VAR_USER_PASS = "MYSQL_USER_PASS"

CONFIG_PATH = ROOT_DIR.joinpath("conf")
CONFIG_NAME = "config"


if __name__ == "__main__":
    print(CONFIG_NAME)
    print(CONFIG_PATH)
