import pytest
from unittest.mock import patch
from decimal import Decimal
from classes.account_manager import AccountManager

def test_mutant_get_account_balances_query_modification():
    """
    Mutant test: Verifica que cambios en la consulta SQL sean detectados
    """
    with patch('config.database.Database.get_connection') as mock_connection:
        mock_cursor = mock_connection.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = None

        # Simulate a potential mutation in the SQL query
        with patch.object(mock_cursor, 'execute', wraps=mock_cursor.execute) as mock_execute:
            AccountManager.get_account_balances(1)
            
            # Check that the expected SQL query was used
            mock_execute.assert_called_once_with(
                "SELECT BalanceUSD, BalanceEUR, BalancePEN FROM Accounts WHERE UserId = ?", 
                (1,)
            )

def test_mutant_update_balances_amount_check():
    """
    Mutant test: Verifica diferentes escenarios de actualización de balance
    """
    with patch('config.database.Database.get_connection') as mock_connection:
        mock_cursor = mock_connection.return_value.cursor.return_value
        
        # Scenarios to test
        scenarios = [
            # Scenario with sufficient balance
            {
                "initial_balance": Decimal("100.00"),
                "monto": Decimal("50.00"),
                "expected": True
            },
            # Scenario with insufficient balance
            {
                "initial_balance": Decimal("100.00"),
                "monto": Decimal("150.00"),
                "expected": False
            },
            # Scenario with balance exactly equal to amount
            {
                "initial_balance": Decimal("100.00"),
                "monto": Decimal("100.00"),
                "expected": True
            }
        ]

        for scenario in scenarios:
            # Reset mocks before each scenario
            mock_cursor.reset_mock()
            mock_cursor.fetchone.side_effect = [
                (scenario["initial_balance"],),  # Source balance
                (Decimal("500.00"),)             # Destination balance
            ]

            result = AccountManager.update_balances(
                1, "USD", "EUR", scenario["monto"], Decimal("45.00")
            )
            assert result is scenario["expected"], f"Failed for scenario: {scenario}"

def test_mutant_update_balances_error_handling():
    """
    Mutant test: Verifica diferentes escenarios de manejo de errores
    """
    with patch('config.database.Database.get_connection') as mock_connection:
        scenarios = [
            # No account found
            {
                "side_effect": [None],
                "expected_result": {"error": "No se encontró la cuenta del usuario."}
            },
            # Database connection error
            {
                "side_effect": [Exception("Connection error")],
                "expected_result": {"error": "Connection error"}
            }
        ]

        for scenario in scenarios:
            with patch.object(mock_connection.return_value.cursor.return_value, 'fetchone', 
                               side_effect=scenario["side_effect"]):
                result = AccountManager.update_balances(
                    1, "USD", "EUR", Decimal("100.00"), Decimal("90.00")
                )
                assert result == scenario["expected_result"]

