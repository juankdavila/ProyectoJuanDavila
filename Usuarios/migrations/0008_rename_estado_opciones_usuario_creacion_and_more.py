# Generated by Django 5.0.6 on 2024-07-10 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0007_remove_opciones_eliminar_remove_opciones_genero_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opciones',
            old_name='estado',
            new_name='usuario_creacion',
        ),
        migrations.RemoveField(
            model_name='opciones',
            name='solo_lectura',
        ),
    ]
