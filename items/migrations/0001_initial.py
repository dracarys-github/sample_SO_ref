# Generated by Django 3.1.2 on 2021-05-04 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item_Cat_Mast',
            fields=[
                ('item_cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_cat_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item_Mast',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_cat_mast', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.item_cat_mast')),
            ],
        ),
    ]