from config.database import Database
from decimal import Decimal

class AccountManager:
    @staticmethod
    def get_account_balances(user_id):
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT BalanceUSD, BalanceEUR, BalancePEN FROM Accounts WHERE UserId = ?", (user_id,))
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
            
            # Obtener el balance de la divisa de origen
            cursor.execute(f"SELECT Balance{divisa_origen} FROM Accounts WHERE UserId = ?", (user_id,))
            balance_origen = cursor.fetchone()

            # Verifica si se encontró el balance
            if balance_origen is None:
                raise ValueError("No se encontró la cuenta del usuario.")
            
            # Ahora balance_origen es un Decimal directamente
            balance_origen = Decimal(balance_origen)  # Aquí no necesitas [0]

            if balance_origen >= monto:
                nuevo_balance_origen = balance_origen - monto
                
                # Actualiza el balance de la divisa de origen
                cursor.execute(f"UPDATE Accounts SET Balance{divisa_origen} = ? WHERE UserId = ?", 
                            (nuevo_balance_origen, user_id))
                
                # Obtener el balance de la divisa de destino
                cursor.execute(f"SELECT Balance{divisa_destino} FROM Accounts WHERE UserId = ?", (user_id,))
                balance_destino = cursor.fetchone()
                
                # Verifica si se encontró el balance de destino
                if balance_destino is None:
                    raise ValueError("No se encontró la cuenta de destino.")
                
                balance_destino = Decimal(balance_destino)  # Aquí tampoco necesitas [0]
                nuevo_balance_destino = balance_destino + monto_convertido
                
                # Actualiza el balance de la divisa de destino
                cursor.execute(f"UPDATE Accounts SET Balance{divisa_destino} = ? WHERE UserId = ?", 
                            (nuevo_balance_destino, user_id))
                
                conn.commit()
                return True
            
            return False

        except Exception as e:
            return {"error": str(e)}
        
        finally:
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            if 'conn' in locals() and conn is not None:
                conn.close()