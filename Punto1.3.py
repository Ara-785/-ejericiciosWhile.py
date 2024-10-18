# Solicitar al usuario que ingrese la calificación del estudiante  
calificacion = float(input("Introduce la calificación del estudiante: "))  

# Clasificar el rendimiento según la calificación  
if calificacion > 4.5:  
    rendimiento = "Excelente"  
elif 3.5 <= calificacion <= 4.5:  
    rendimiento = "Bueno"  
elif 3 <= calificacion < 3.5:  
    rendimiento = "Regular"  
elif 0 <= calificacion < 3:  
    rendimiento = "Insuficiente"  
else:  
    rendimiento = "Calificación no válida. Debe estar entre 0 y 5."  

# Mostrar el resultado  
print(f"La calificación del estudiante es: {rendimiento}")
