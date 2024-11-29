from behave import given, when, then

# Given un usuario quiere convertir 100 USD a EUR
@given(u'un usuario quiere convertir 100 USD a EUR')
def step_impl(context):
    # Guardamos el monto y la moneda
    context.amount = 100
    context.from_currency = "USD"
    context.to_currency = "EUR"

# When realiza la conversión
@when(u'realiza la conversión')
def step_impl(context):
    # Lógica para realizar la conversión (esto es un ejemplo simple)
    # Deberías tener la lógica de la conversión aquí, utilizando algún servicio o API
    conversion_rate = 0.85  # Ejemplo de tipo de cambio USD -> EUR
    context.converted_amount = context.amount * conversion_rate

# Then se muestra el monto equivalente en EUR
@then(u'se muestra el monto equivalente en EUR')
def step_impl(context):
    assert context.converted_amount == 85  # 100 USD * 0.85 = 85 EUR

# Given el sistema tiene acceso a tipos de cambio actualizados
@given(u'el sistema tiene acceso a tipos de cambio actualizados')
def step_impl(context):
    # Aquí podrías verificar que el sistema tenga acceso a una fuente de datos
    context.exchange_rates_available = True

# When el usuario consulta el tipo de cambio de USD a EUR
@when(u'el usuario consulta el tipo de cambio de USD a EUR')
def step_impl(context):
    # Lógica para obtener el tipo de cambio
    context.exchange_rate = 0.85  # Ejemplo de tipo de cambio USD -> EUR

# Then se muestra el tipo de cambio actual
@then(u'se muestra el tipo de cambio actual')
def step_impl(context):
    assert context.exchange_rate == 0.85

# Given el sistema no tiene registro de la moneda XYZ
@given(u'el sistema no tiene registro de la moneda XYZ')
def step_impl(context):
    # Simulamos que XYZ no existe en los registros del sistema
    context.currency_exists = False

# When el usuario consulta el tipo de cambio de XYZ
@when(u'el usuario consulta el tipo de cambio de XYZ')
def step_impl(context):
    # El sistema no tiene información de la moneda XYZ
    if not context.currency_exists:
        context.error_message = "Moneda desconocida"

# Then se muestra un mensaje de error indicando moneda desconocida
@then(u'se muestra un mensaje de error indicando moneda desconocida')
def step_impl(context):
    assert context.error_message == "Moneda desconocida"


# Given un usuario intenta convertir -50 USD a EUR
@given(u'un usuario intenta convertir -50 USD a EUR')
def step_impl(context):
    context.amount = -50  # Cantidad negativa
    context.from_currency = 'USD'
    context.to_currency = 'EUR'

# Then se muestra un mensaje indicando que la cantidad debe ser positiva
@then(u'se muestra un mensaje indicando que la cantidad debe ser positiva')
def step_impl(context):
    assert context.error_message == "La cantidad debe ser positiva."
