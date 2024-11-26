import pytest
from unittest.mock import patch
from classes.user_manager import UserManager
from config.database import Database

@pytest.fixture
def mock_database_connection():
    with patch.object(Database, 'get_connection') as mock_connection:
        mock_cursor = mock_connection.return_value.cursor.return_value
        mock_cursor.execute.return_value = None
        yield mock_connection

def test_verify_credentials_success(mock_database_connection):
    mock_cursor = mock_database_connection.return_value.cursor.return_value
    mock_cursor.fetchone.return_value = (1, "test_user", "hashed_password")
    
    user = UserManager.verify_credentials("test_user", "hashed_password")
    assert user == (1, "test_user", "hashed_password")

def test_verify_credentials_invalid_username(mock_database_connection):
    mock_cursor = mock_database_connection.return_value.cursor.return_value
    mock_cursor.fetchone.return_value = None  # No user found
    
    user = UserManager.verify_credentials("invalid_user", "hashed_password")
    assert user is None

def test_verify_credentials_incorrect_password(mock_database_connection):
    mock_cursor = mock_database_connection.return_value.cursor.return_value
    mock_cursor.fetchone.return_value = (1, "test_user", "hashed_password")
    
    user = UserManager.verify_credentials("test_user", "wrong_password")
    assert user is None

def test_verify_credentials_database_error(mock_database_connection):
    mock_cursor = mock_database_connection.return_value.cursor.return_value
    mock_cursor.execute.side_effect = Exception("Database error")
    
    user = UserManager.verify_credentials("test_user", "hashed_password")
    assert user is None