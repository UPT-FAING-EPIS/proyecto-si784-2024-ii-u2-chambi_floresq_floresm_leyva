from behave import given, when, then

# Given un usuario sin cuenta registrada
@given(u'un usuario sin cuenta registrada')
def step_impl(context):
    context.user = None  # Representa que el usuario no tiene cuenta

# When el usuario proporciona los datos válidos para la cuenta
@when(u'el usuario proporciona los datos válidos para la cuenta')
def step_impl(context):
    # Simulamos la creación de una cuenta con datos válidos
    context.user = {"name": "Juan Pérez", "balance": 1000}  # Ejemplo de cuenta creada

# Then la cuenta se crea exitosamente
@then(u'la cuenta se crea exitosamente')
def step_impl(context):
    assert context.user is not None  # Verificamos que la cuenta se haya creado

# Given un usuario intenta registrar una cuenta
@given(u'un usuario intenta registrar una cuenta')
def step_impl(context):
    context.user = None  # El usuario no ha completado el registro

# When el usuario no completa todos los campos requeridos
@when(u'el usuario no completa todos los campos requeridos')
def step_impl(context):
    context.registration_error = "Campos incompletos"  # Simulamos un error de registro

# Then se muestra un error indicando datos faltantes
@then(u'se muestra un error indicando datos faltantes')
def step_impl(context):
    assert context.registration_error == "Campos incompletos"

# When el usuario consulta el saldo de su cuenta
@when(u'el usuario consulta el saldo de su cuenta')
def step_impl(context):
    context.balance = context.user["balance"]  # Consultamos el saldo de la cuenta

# Then se muestra el saldo actual
@then(u'se muestra el saldo actual')
def step_impl(context):
    assert context.balance == 1000  # Verificamos que el saldo es correcto

# When el usuario intenta consultar el saldo
@when(u'el usuario intenta consultar el saldo')
def step_impl(context):
    if context.user is None:
        context.error_message = "No existen cuentas"  # Error por no tener cuenta

# Given un usuario con una cuenta activa
@given(u'un usuario con una cuenta activa')
def step_impl(context):
    context.user = {"name": "Juan Pérez", "balance": 1000, "active": True}  # Cuenta activa

# When el usuario solicita eliminar su cuenta
@when(u'el usuario solicita eliminar su cuenta')
def step_impl(context):
    context.user["active"] = False  # Elimina la cuenta al desactivarla

# Then la cuenta se elimina correctamente
@then(u'la cuenta se elimina correctamente')
def step_impl(context):
    assert not context.user["active"]  # Verificamos que la cuenta esté desactivada

# Given un usuario sin cuentas registradas
@given(u'un usuario sin cuentas registradas')
def step_impl(context):
    context.user = None  # No tiene cuentas registradas

# When el usuario solicita eliminar una cuenta
@when(u'el usuario solicita eliminar una cuenta')
def step_impl(context):
    if context.user is None:
        context.error_message = "No existen cuentas"  # Error al intentar eliminar una cuenta inexistente

# Then se muestra un mensaje indicando que no existen cuentas
@then(u'se muestra un mensaje indicando que no existen cuentas')
def step_impl(context):
    assert context.error_message == "No existen cuentas"  # Verificamos el mensaje de error
