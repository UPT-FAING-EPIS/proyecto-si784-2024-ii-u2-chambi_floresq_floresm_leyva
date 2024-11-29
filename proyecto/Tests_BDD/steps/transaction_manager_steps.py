from behave import given, when, then

# Given un usuario tiene 1000 en su cuenta
@given(u'un usuario tiene 1000 en su cuenta')
def step_impl(context):
    # Establecemos un saldo inicial para el usuario
    context.user_account_balance = 1000

# When el usuario deposita 500 en su cuenta
@when(u'el usuario deposita 500 en su cuenta')
def step_impl(context):
    # Lógica para realizar el depósito
    context.user_account_balance += 500

# Then el saldo de la cuenta aumenta en 500
@then(u'el saldo de la cuenta aumenta en 500')
def step_impl(context):
    assert context.user_account_balance == 1500

# Given un usuario tiene 300 en su cuenta
@given(u'un usuario tiene 300 en su cuenta')
def step_impl(context):
    context.user_account_balance = 300

# When intenta retirar 500
@when(u'intenta retirar 500')
def step_impl(context):
    # Verificar si hay fondos suficientes
    if context.user_account_balance < 500:
        context.error_message = "Fondos insuficientes"
    else:
        context.user_account_balance -= 500

# Then se muestra un mensaje indicando fondos insuficientes
@then(u'se muestra un mensaje indicando fondos insuficientes')
def step_impl(context):
    assert context.error_message == "Fondos insuficientes"

# Given dos cuentas activas con saldo suficiente
@given(u'dos cuentas activas con saldo suficiente')
def step_impl(context):
    context.account_A_balance = 500
    context.account_B_balance = 300

# When el usuario transfiere 100 de la cuenta A a la cuenta B
@when(u'el usuario transfiere 100 de la cuenta A a la cuenta B')
def step_impl(context):
    # Lógica para realizar la transferencia
    context.account_A_balance -= 100
    context.account_B_balance += 100

# Then el saldo de la cuenta A disminuye en 100 y el saldo de la cuenta B aumenta en 100
@then(u'el saldo de la cuenta A disminuye en 100 y el saldo de la cuenta B aumenta en 100')
def step_impl(context):
    assert context.account_A_balance == 400
    assert context.account_B_balance == 400

# Given un usuario sin cuentas registradas
@given(u'un usuario sin cuentas registradas')
def step_impl(context):
    context.account = None  # No hay cuenta registrada

# When intenta depositar 500
@when(u'intenta depositar 500')
def step_impl(context):
    if context.account:
        context.account.deposit(500)
    else:
        context.error_message = "Cuenta inexistente"

# Then se muestra un mensaje de error indicando cuenta inexistente
@then(u'se muestra un mensaje de error indicando cuenta inexistente')
def step_impl(context):
    assert context.error_message == "Cuenta inexistente"
