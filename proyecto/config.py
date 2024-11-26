import os

# Obtener las variables de entorno, si no están definidas, usar valores predeterminados
<<<<<<< HEAD
server = os.getenv('DB_SERVER', 'DESKTOP-6F24RCS')  # Por defecto usa '.' (localhost)
database = os.getenv('DB_NAME', 'CasaDeCambioDBTest')  # Usar 'CasaDeCambioDB' por defecto
username = os.getenv('DB_USERNAME', 'DESKTOP-6F24RCS\Jerson')
password = os.getenv('DB_PASSWORD', ' ')
=======
server = os.getenv('DB_SERVER', '.')  # Por defecto usa '.' (localhost)
database = os.getenv('DB_NAME', 'CasaDeCambioDBTest')  # Usar 'CasaDeCambioDB' por defecto
username = os.getenv('DB_USERNAME', 'sa')
password = os.getenv('DB_PASSWORD', 'epis')
>>>>>>> 48af20b231d8df85174d2daa3dc090ba006e3ecd
driver = '{ODBC Driver 17 for SQL Server}'