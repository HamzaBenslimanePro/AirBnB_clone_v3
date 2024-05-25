from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

# Check the storage type from environment variables
storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
