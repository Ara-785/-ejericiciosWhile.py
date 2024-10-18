# Solicitar al usuario que ingrese la temperatura  
temperatura = float(input("Introduce la temperatura en grados Celsius: "))  

# Clasificar la temperatura  
if temperatura < 10:  
    clasificacion = "Frío"  
elif 10 <= temperatura <= 25:  
    clasificacion = "Templado"  
else:  
    clasificacion = "Cálido"  

# Mostrar el resultado  
print(f"La temperatura es clasificada como: {clasificacion}") 
