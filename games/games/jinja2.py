# Assuming this is in your_project/jinja2.py or similar
from jinja2 import Environment, FileSystemLoader


def environment(**options):
    # Create a Jinja2 environment with desired options
    env = Environment(**options)

    # Add custom filters, extensions, globals, etc. if needed
    # For static files handling:
    from django.contrib.staticfiles.storage import staticfiles_storage
    from django.urls import reverse

    env.globals.update(
        {
            "static": staticfiles_storage.url,
            "url_for": reverse,
            # Add other globals as needed
        }
    )

    return env
