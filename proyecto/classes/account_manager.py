from config.database import Database
from decimal import Decimal

class AccountManager:
    @staticmethod
    def get_account_balances(user_id):
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT BalanceUSD, BalanceEUR, BalancePEN FROM Accounts WHERE UserId = ?", user_id)
            return cursor.fetchone()
        finally:
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            if 'conn' in locals() and conn is not None:
                conn.close()

    @staticmethod
    def update_balances(user_id, divisa_origen, divisa_destino, monto, monto_convertido):
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(f"SELECT Balance{divisa_origen} FROM Accounts WHERE UserId = ?", user_id)
            balance_origen = Decimal(cursor.fetchone()[0])
            
            if balance_origen >= monto:
                nuevo_balance_origen = balance_origen - monto
                cursor.execute(f"UPDATE Accounts SET Balance{divisa_origen} = ? WHERE UserId = ?", 
                             nuevo_balance_origen, user_id)
                
                cursor.execute(f"SELECT Balance{divisa_destino} FROM Accounts WHERE UserId = ?", user_id)
                balance_destino = Decimal(cursor.fetchone()[0])
                nuevo_balance_destino = balance_destino + monto_convertido
                cursor.execute(f"UPDATE Accounts SET Balance{divisa_destino} = ? WHERE UserId = ?", 
                             nuevo_balance_destino, user_id)
                
                conn.commit()
                return True
            return False
            
        finally:
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            if 'conn' in locals() and conn is not None:
                conn.close()