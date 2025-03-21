import random
import string

def generate_password(lengt=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(lengt))
    
    return password

if __name__ == '__main__':
    print('🔒 Generador de Contraseñas Seguras 🔒')
    
    try:
        length = int(input('Ingrese la longitud de la contraseña (minimo 6): '))
        if length < 6:
            print('La longitud mínima es 6. Se usará 6 por defecto.')
            length = 6
            
        password = generate_password(length)
        print(f'Tu contraseña generada es: {password}')
    
    except ValueError:
        print('⚠️ Error: Ingrese un número válido. ⚠️')