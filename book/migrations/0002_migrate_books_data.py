# Generated by Django 5.0.7 on 2024-08-11 20:44

from django.db import migrations
import json
import os


# Book 데이터 마이그레이션 함수
def migrate_books(apps, schema_editor):
    Book = apps.get_model("book", "Book")

    project_root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    json_file_path = os.path.join(project_root_dir, "data", "books_data.json")

    with open(json_file_path, "r", encoding="utf-8") as f:
        books_data = json.load(f)

    for book in books_data:
        Book.objects.create(
            title = book.get("title"),
            link = book.get("link"),
            author = book.get("author"),
            pubDate = book.get("pubDate"),
            description = book.get("description"),
            isbn = book.get("isbn"),
            itemId = book.get("itemId"),
            cover = book.get("cover"),
            categoryName = book.get("categoryName"),
            publisher = book.get("publisher")
        )

class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(migrate_books),
    ]
