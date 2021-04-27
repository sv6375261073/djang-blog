from django.core.exceptions import ValidationError
def file_size(file):
    value=file.size
    if value>100000000:
        raise ValidationError('Maximum size is 10 MB')
