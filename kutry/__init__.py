from django.db import migrations, models
from django.conf import settings

class Migration(migrations.Migration):
    dependencies = [
        # Add the migration dependencies here.
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # Use settings.AUTH_USER_MODEL instead of importing User
                ('user', models.OneToOneField(on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
