import os

# Obtener las variables de entorno, si no están definidas, usar valores predeterminados
server = os.getenv('DB_SERVER', 'DESKTOP-6F24RCS')  # Por defecto usa '.' (localhost)
database = os.getenv('DB_NAME', 'CasaDeCambioDBTest')  # Usar 'CasaDeCambioDB' por defecto
username = os.getenv('DB_USERNAME', 'DESKTOP-6F24RCS\Jerson')
password = os.getenv('DB_PASSWORD', ' ')
driver = '{ODBC Driver 17 for SQL Server}'