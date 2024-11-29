from behave import given, when, then

# Given un usuario tiene una cuenta con un saldo inicial de 1000
@given(u'un usuario tiene una cuenta con un saldo inicial de 1000')
def step_impl(context):
    # Guardamos el saldo inicial de la cuenta del usuario
    context.account_balance = 1000

# When el usuario realiza un depósito de 500
@when(u'el usuario realiza un depósito de 500')
def step_impl(context):
    # Lógica para depositar 500 en la cuenta
    context.account_balance += 500

# Then el saldo de la cuenta debe ser 1500
@then(u'el saldo de la cuenta debe ser 1500')
def step_impl(context):
    assert context.account_balance == 1500

# Given el saldo de la cuenta es 1000
@given(u'el saldo de la cuenta es 1000')
def step_impl(context):
    context.account_balance = 1000

# When el usuario solicita retirar 300
@when(u'el usuario solicita retirar 300')
def step_impl(context):
    # Lógica para retirar 300
    if context.account_balance >= 300:
        context.account_balance -= 300
        context.withdrawal_success = True
    else:
        context.withdrawal_success = False

# Then el saldo de la cuenta debe ser 700
@then(u'el saldo de la cuenta debe ser 700')
def step_impl(context):
    assert context.account_balance == 700
    assert context.withdrawal_success is True

# Given un usuario intenta retirar más dinero del que tiene
@given(u'un usuario intenta retirar más dinero del que tiene')
def step_impl(context):
    context.account_balance = 200
    context.withdrawal_amount = 500

# When el usuario intenta retirar 500
@when(u'el usuario intenta retirar 500')
def step_impl(context):
    # Lógica para intentar retirar más de lo que hay en la cuenta
    if context.account_balance < context.withdrawal_amount:
        context.error_message = "Fondos insuficientes"
        context.withdrawal_success = False
    else:
        context.account_balance -= context.withdrawal_amount
        context.withdrawal_success = True

# Then se muestra un mensaje de error "Fondos insuficientes"
@then(u'se muestra un mensaje de error "Fondos insuficientes"')
def step_impl(context):
    assert context.error_message == "Fondos insuficientes"
    assert context.withdrawal_success is False

# Given un usuario desea cambiar la información de su cuenta
@given(u'un usuario desea cambiar la información de su cuenta')
def step_impl(context):
    context.account_info = {
        "name": "Juan Pérez",
        "email": "juan@example.com"
    }

# When el usuario actualiza su correo electrónico a "juan.perez@nuevo.com"
@when(u'el usuario actualiza su correo electrónico a "juan.perez@nuevo.com"')
def step_impl(context):
    # Lógica para actualizar la información de la cuenta
    context.account_info["email"] = "juan.perez@nuevo.com"

# Then la cuenta del usuario debe tener el correo actualizado
@then(u'la cuenta del usuario debe tener el correo actualizado')
def step_impl(context):
    assert context.account_info["email"] == "juan.perez@nuevo.com"

# Given el sistema tiene una lista de cuentas registradas
@given(u'el sistema tiene una lista de cuentas registradas')
def step_impl(context):
    context.accounts = {
        "user1": {"balance": 1000, "email": "user1@example.com"},
        "user2": {"balance": 2000, "email": "user2@example.com"}
    }

# When el usuario consulta el saldo de la cuenta "user1"
@when(u'el usuario consulta el saldo de la cuenta "user1"')
def step_impl(context):
    # Lógica para consultar el saldo de la cuenta
    context.account_balance = context.accounts["user1"]["balance"]

# Then el saldo de la cuenta "user1" debe ser 1000
@then(u'el saldo de la cuenta "user1" debe ser 1000')
def step_impl(context):
    assert context.account_balance == 1000

# Given el sistema tiene una cuenta activa
@given(u'el sistema tiene una cuenta activa')
def step_impl(context):
    context.account_active = True

# When el usuario desactiva la cuenta
@when(u'el usuario desactiva la cuenta')
def step_impl(context):
    # Lógica para desactivar la cuenta
    context.account_active = False

# Then la cuenta debe estar desactivada
@then(u'la cuenta debe estar desactivada')
def step_impl(context):
    assert context.account_active is False

# When I create a new account with name "John Doe" and balance 1000
@when(u'yo creo una nueva cuenta con nombre "John Doe" y saldo 1000')
def step_impl(context):
    # Crear la cuenta
    context.account = context.account_manager.create_account("John Doe", 1000)

# Then the account "John Doe" should be created with balance 1000
@then(u'la cuenta "John Doe" debería ser creada con saldo 1000')
def step_impl(context):
    assert context.account.name == "John Doe"
    assert context.account.balance == 1000
