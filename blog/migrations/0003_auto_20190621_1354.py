# Generated by Django 2.2.2 on 2019-06-21 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_commenter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'permissions': (('can_post_comment', 'Post comment'),)},
        ),
    ]
