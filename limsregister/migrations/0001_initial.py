# Generated by Django 5.0.4 on 2024-04-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmRegister',
            fields=[
                ('farm_id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('farm_name', models.CharField(max_length=500)),
                ('size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unit_of_measure', models.CharField(max_length=50)),
                ('size_in_hectares', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ownership', models.CharField(max_length=250)),
                ('owner_name', models.CharField(max_length=250)),
                ('company_name', models.CharField(max_length=250)),
                ('nationality', models.CharField(max_length=50)),
                ('gazette_status', models.CharField(max_length=50)),
                ('diagram_no', models.CharField(max_length=50)),
                ('title_type', models.CharField(max_length=50)),
                ('deed_no', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('previous_district', models.CharField(max_length=70)),
                ('current_district', models.CharField(max_length=50)),
                ('farm_activity', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=500)),
            ],
        ),
    ]
