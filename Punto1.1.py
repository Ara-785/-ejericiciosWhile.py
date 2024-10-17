# Solicitar al usuario una letra  
letra = input("Introduce una letra: ").lower()  

# Verificar que la entrada sea una letra  
if len(letra) != 1 or not letra.isalpha():  
    print("Por favor, introduce solo una letra.")  
else:  
    # Evaluar si la letra está en las primeras o últimas letras del alfabeto  
    if letra >= 'a' and letra <= 'm':  
        print("La letra está en las primeras letras del alfabeto.")  
    else:  
        print("La letra está en las últimas letras del alfabeto.")
