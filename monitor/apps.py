from os import getenv

from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.db import connections


class MonitorConfig(AppConfig):
  default_auto_field = "django.db.models.BigAutoField"
  name = "monitor"

  def ready(self):
    conn = connections["default"]
    has_tables = len(conn.introspection.get_table_list(conn.cursor())) > 0

    if not has_tables:
      call_command("migrate")
      call_command("loaddata", "monitor")

      get_user_model().objects.create_superuser(
        getenv("ADMIN_NAME") or "admin",
        getenv("ADMIN_MAIL") or "admin@example.com",
        getenv("ADMIN_PASS") or "password",
      )
