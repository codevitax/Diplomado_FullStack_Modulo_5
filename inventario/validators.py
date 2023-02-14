from django.core.exceptions import ValidationError


def validar_par(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s No es un numero par',
            params={'value':value}
        )

def validation_categoria(value):
    if value == 'No permitido':
        raise ValidationError('No es una opcion permitida')

def validar_nombre(value):
    if value == 'Comida':
        raise ValidationError('Comida no es una opcion permitida')