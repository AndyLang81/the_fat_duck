#!/usr/bin/env python
"""Django’s command-line utility for administrative tasks."""
import os  # interact with the operating system
import sys  # access command-line arguments


def main():
    """Run administrative tasks."""
    # Ensure Django knows which settings module to use
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_fat_duck.settings')
    try:
        # Import Django’s command-line executor
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise a clear error if Django isn’t installed or not on PYTHONPATH
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Pass control and any CLI args through to Django
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Entry point: call main() when script is run directly
    main()
