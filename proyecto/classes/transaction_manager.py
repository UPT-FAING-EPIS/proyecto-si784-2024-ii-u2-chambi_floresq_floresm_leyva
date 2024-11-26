from config.database import Database
from datetime import datetime

class TransactionManager:
    @staticmethod
    def register_transaction(user_id, divisa_origen, divisa_destino, monto, tasa_conversion, monto_convertido):
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO Transactions 
                (UserId, FromCurrency, ToCurrency, Amount, Rate, Result, TransactionDate) 
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                user_id, divisa_origen, divisa_destino, monto, tasa_conversion, 
                monto_convertido, datetime.now())
            
            conn.commit()
            return True
            
        finally:
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            if 'conn' in locals() and conn is not None:
                conn.close()

    @staticmethod
    def get_user_transactions(user_id):
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Transactions WHERE UserId = ? ORDER BY TransactionDate DESC", user_id)
            return cursor.fetchall()
        finally:
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            if 'conn' in locals() and conn is not None:
                conn.close()