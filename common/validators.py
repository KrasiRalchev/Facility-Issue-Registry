from django.core.exceptions import ValidationError


# not in use after cloudinary config

def validate_file_size_1mb(value, max_size=1):
    if value.size > max_size * 1024 * 1024:
        raise ValidationError("File size should not exceed 1 MB.")

def validate_file_size_2mb(value, max_size=2):
    if value.size > max_size * 1024 * 1024:
        raise ValidationError("File size should not exceed 2 MB.")