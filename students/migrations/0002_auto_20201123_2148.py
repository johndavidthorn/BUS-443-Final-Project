# Generated by Django 3.1.3 on 2020-11-24 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courseinfo',
            fields=[
                ('courseid', models.IntegerField(primary_key=True, serialize=False)),
                ('coursetitle', models.CharField(max_length=500)),
                ('coursename', models.CharField(max_length=500)),
                ('courseselectioncode', models.IntegerField()),
                ('coursedepartment', models.CharField(default='SOME STRING', max_length=500)),
                ('instructorname', models.CharField(default='SOME STRING', max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='studentdetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='gpa',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='major',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='studentid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='year',
            field=models.CharField(max_length=500),
        ),
    ]
