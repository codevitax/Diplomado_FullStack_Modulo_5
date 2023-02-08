from django.core.exceptions import ValidationError


def validar_par(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s No es un numero par',
            params={'value':value}
        )