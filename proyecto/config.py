import os

# Obtener las variables de entorno, si no están definidas, usar valores predeterminados
server = os.getenv('DB_SERVER', '.')  # Por defecto usa '.' (localhost)
database = os.getenv('DB_NAME', 'CasaDeCambioDBTest')  # Usar 'CasaDeCambioDB' por defecto
username = os.getenv('DB_USERNAME', 'sa')
password = os.getenv('DB_PASSWORD', 'epis')
driver = '{ODBC Driver 17 for SQL Server}'