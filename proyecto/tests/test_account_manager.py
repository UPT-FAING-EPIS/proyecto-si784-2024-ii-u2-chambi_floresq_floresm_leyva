import pytest
from unittest.mock import patch
from decimal import Decimal
from classes.account_manager import AccountManager
from config.database import Database

@pytest.fixture
def mock_database_connection():
    # Crea un mock de la conexión a la base de datos
    with patch.object(Database, 'get_connection') as mock_connection:
        mock_cursor = mock_connection.return_value.cursor.return_value
        mock_cursor.execute.return_value = None
        mock_connection.return_value.commit.return_value = None
        yield mock_connection

def test_get_account_balances_success(mock_database_connection):
    # Prueba que se obtienen los balances correctamente para un usuario existente
    mock_cursor = mock_database_connection.return_value.cursor.return_value
    mock_cursor.fetchone.return_value = (Decimal("1000.00"), Decimal("500.00"), Decimal("200.00"))
    
    balances = AccountManager.get_account_balances(1)
    assert balances == (Decimal("1000.00"), Decimal("500.00"), Decimal("200.00"))

def test_get_account_balances_no_user(mock_database_connection):
    # Prueba que se devuelve None si el usuario no existe
    mock_cursor = mock_database_connection.return_value.cursor.return_value
    mock_cursor.fetchone.return_value = None
    
    balances = AccountManager.get_account_balances(999)  # Usuario no existente
    assert balances is None

"""
def test_update_balances_success(mock_database_connection):
    # Prueba que se actualizan los balances correctamente cuando hay suficientes fondos
    mock_cursor = mock_database_connection.return_value.cursor.return_value
    mock_cursor.fetchone.side_effect = [Decimal("1000.00"), Decimal("500.00")]  # Balances iniciales
    
    result = AccountManager.update_balances(1, "USD", "EUR", Decimal("100.00"), Decimal("90.00"))
    
    assert result is True
    mock_cursor.execute.assert_any_call("UPDATE Accounts SET BalanceUSD = ? WHERE UserId = ?", Decimal("900.00"), 1)
    mock_cursor.execute.assert_any_call("UPDATE Accounts SET BalanceEUR = ? WHERE UserId = ?", Decimal("590.00"), 1)
"""

def test_update_balances_insufficient_funds(mock_database_connection):
    # Prueba que la actualización falla si los fondos son insuficientes
    mock_cursor = mock_database_connection.return_value.cursor.return_value
    mock_cursor.fetchone.side_effect = [Decimal("50.00"), Decimal("500.00")]  # Saldo insuficiente
    
    result = AccountManager.update_balances(1, "USD", "EUR", Decimal("100.00"), Decimal("90.00"))
    
    assert result is False
    mock_cursor.execute.assert_called_once_with("SELECT BalanceUSD FROM Accounts WHERE UserId = ?", (1,))

def test_update_balances_no_account(mock_database_connection):
    # Prueba que se devuelve un error si no se encuentra la cuenta del usuario
    mock_cursor = mock_database_connection.return_value.cursor.return_value
    mock_cursor.fetchone.side_effect = [None]  # No se encuentra la cuenta
    
    result = AccountManager.update_balances(1, "USD", "EUR", Decimal("100.00"), Decimal("90.00"))
    
    assert "error" in result  # Espera un mensaje de error
    assert result["error"] == "No se encontró la cuenta del usuario."

def test_update_balances_database_error(mock_database_connection):
    # Prueba que se maneja correctamente un error de base de datos
    mock_cursor = mock_database_connection.return_value.cursor.return_value
    mock_cursor.fetchone.side_effect = Exception("Database error")

    result = AccountManager.update_balances(1, "USD", "EUR", Decimal("100.00"), Decimal("90.00"))
    
    assert "error" in result  # Verifica que se maneje el error
    assert result["error"] == "Database error"