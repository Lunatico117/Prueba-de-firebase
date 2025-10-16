# viewmodel/user_vm.py
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
import os
from model.user import User
import uuid  # Para generar IDs únicos

# Cargar .env
load_dotenv()
cred_path = os.getenv("FIREBASE_CREDENTIALS")
db_url = os.getenv("FIREBASE_DB_URL")

# Inicializar Firebase (una sola vez)
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred, {"databaseURL": db_url})

# Referencia principal de usuarios
users_ref = db.reference("users")

# CRUD
def create_user(name: str, email: str, password: str) -> str:
    """Crea un usuario en Firebase y devuelve su ID"""
    user_id = str(uuid.uuid4())  # Genera ID único
    user = User(user_id, name, email, password)
    users_ref.child(user_id).set(user.to_dict())
    return user_id

def get_user(user_id: str) -> dict:
    """Obtiene un usuario por su ID"""
    user_data = users_ref.child(user_id).get()
    return user_data

def update_user(user_id: str, name: str = None, email: str = None, password: str = None):
    """Actualiza campos de un usuario"""
    updates = {}
    if name:
        updates["name"] = name
    if email:
        updates["email"] = email
    if password:
        updates["password"] = password
    if updates:
        users_ref.child(user_id).update(updates)

def delete_user(user_id: str):
    """Elimina un usuario"""
    users_ref.child(user_id).delete()
