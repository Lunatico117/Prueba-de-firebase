# main.py
from viewmodel.user_vm import create_user, get_user, update_user, delete_user

def menu():
    print("\n--- CRUD Usuarios ---")
    print("1. Crear usuario")
    print("2. Ver usuario")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")
    return input("Elige una opcion: ")

while True:
    opcion = menu()

    if opcion == "1":
        name = input("Nombre: ")
        email = input("Correo: ")
        password = input("Contraseña: ")
        user_id = create_user(name, email, password)
        print(f"Usuario creado con ID: {user_id}")

    elif opcion == "2":
        user_id = input("ID del usuario: ")
        user = get_user(user_id)
        if user:
            print("Usuario:", user)
        else:
            print("Usuario no encontrado.")

    elif opcion == "3":
        user_id = input("ID del usuario: ")
        name = input("Nuevo nombre (dejar vacio si no cambia): ")
        email = input("Nuevo correo (dejar vacio si no cambia): ")
        password = input("Nueva contraseña (dejar vacio si no cambia): ")
        update_user(user_id, name=name or None, email=email or None, password=password or None)
        print("Usuario actualizado.")

    elif opcion == "4":
        user_id = input("ID del usuario: ")
        delete_user(user_id)
        print("Usuario eliminado.")

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opcion invalida. Intenta de nuevo.")
