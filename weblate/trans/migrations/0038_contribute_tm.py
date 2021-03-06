# Generated by Django 2.2.5 on 2019-09-06 13:32

from django.db import migrations
from django.db.models import F


def migrate_tm(apps, schema_editor):
    apps.get_model("trans", "Project").objects.all().update(
        contribute_shared_tm=F("use_shared_tm")
    )


class Migration(migrations.Migration):

    dependencies = [("trans", "0037_auto_20190906_1526")]

    operations = [migrations.RunPython(migrate_tm, migrations.RunPython.noop)]
