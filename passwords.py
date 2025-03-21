import random
import string

def generate_password(lengt=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(lengt))
    
    return password

def save_passwords(password):
    with open('passwords.txt', 'a') as file:
        file.write(password + '\n')
    print('✅Contraseña guardada en "passwords.txt".✅')
    
if __name__ == '__main__':
    print('🔒 Generador de Contraseñas Seguras 🔒')
    
    try:
        num_passwords = int(input('¿Cuantas contraseñas desea generar? '))
        while num_passwords != 0:
            length = int(input('Ingrese la longitud de la contraseña (minimo 6): '))
            if length < 6:
                print('⚠️ La longitud mínima es 6. Se usará 6 por defecto. ⚠️')
                length = 6
            password = generate_password(length)
            print(f'Tu contraseña generada es: {password}\n')
            
            save = input('¿Desea guardar su contraseña? (s/n): ').strip().lower()
            if save == 's':
                save_passwords(password)
            
            num_passwords = num_passwords - 1 
    
    except ValueError:
        print('⚠️ Error: Ingrese un número válido. ⚠️')