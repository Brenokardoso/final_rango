# Generated by Django 4.1.7 on 2023-04-03 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_choice_question_delete_escolha_delete_pesquisa_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='questoes',
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Data de publicamento:'),
        ),
    ]