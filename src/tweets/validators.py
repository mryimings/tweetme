from django.core.exceptions import ValidationError

def validate_content(value):
    content = value
    if content == "":
        raise ValidationError("String cannot be empty")
    if content == "shabi":
        raise ValidationError("bie ma ren")
    return value