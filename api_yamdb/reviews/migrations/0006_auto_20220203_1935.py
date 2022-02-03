# Generated by Django 2.2.16 on 2022-02-03 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_category_comment_genre_review_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=1, help_text='Введите текст комментария', verbose_name='Текст комментария'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='score',
            field=models.IntegerField(default=1, help_text='Введдите оценку', verbose_name='Оценка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(default=1, help_text='Введите текст отзыва', verbose_name='Текст отзыва'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, help_text='Дата публикации комментария', verbose_name='Дата публикации комментария'),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, help_text='Дата публикации отзыва', verbose_name='Дата публикации отзыва'),
        ),
    ]