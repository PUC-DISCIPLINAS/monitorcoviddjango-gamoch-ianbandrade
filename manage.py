#!/usr/bin/env python

from os import environ
from sys import argv

from dotenv import load_dotenv


def main():
  load_dotenv()
  environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

  try:
    from django.conf import settings
    from django.core.management import execute_from_command_line
    from django.core.management.commands.runserver import Command as RunServer
  except ImportError as exc:
    raise ImportError("Couldn't import Django.") from exc

  RunServer.default_addr = settings.RUNSERVER_ADDR
  RunServer.default_port = settings.RUNSERVER_PORT

  execute_from_command_line(argv)


if __name__ == "__main__":
  main()
