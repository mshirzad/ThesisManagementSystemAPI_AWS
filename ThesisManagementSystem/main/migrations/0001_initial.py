# Generated by Django 3.2.15 on 2022-10-15 11:37

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsInfo',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('graduation_year', models.CharField(choices=[('1399', '1399'), ('1400', '1400'), ('1401', '1401'), ('1402', '1402'), ('1403', '1403'), ('1404', '1404'), ('1405', '1405'), ('1406', '1406'), ('1407', '1407'), ('1408', '1408'), ('1409', '1409'), ('1410', '1410'), ('1411', '1411'), ('1412', '1412'), ('1413', '1413'), ('1414', '1414'), ('1415', '1415'), ('1416', '1416'), ('1417', '1417'), ('1418', '1418'), ('1419', '1419'), ('1420', '1420'), ('1421', '1421'), ('1422', '1422'), ('1423', '1423'), ('1424', '1424'), ('1425', '1425')], max_length=4)),
                ('department', models.CharField(choices=[('SE', 'Software Engineering'), ('IT', 'Information Technology'), ('IS', 'Information System')], max_length=2)),
                ('monograph_title', models.CharField(max_length=255)),
                ('monograph_language', models.CharField(choices=[('EN', 'English'), ('FA', 'Farsi'), ('PA', 'Pashto')], max_length=2)),
                ('monograph_file', models.FileField(upload_to=main.models.file_path_generator_for_monographs, validators=[main.models.validate_monograph_file_extension])),
                ('source_code_files', models.FileField(blank=True, null=True, upload_to=main.models.file_path_generator_for_source_code, validators=[main.models.validate_source_code_file_extension])),
            ],
        ),
    ]
