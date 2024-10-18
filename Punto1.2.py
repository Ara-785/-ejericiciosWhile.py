# Normalizar el ángulo a un rango entre 0 y 360 grados  
angulo = angulo % 360  

# Determinar en qué cuadrante se encuentra el ángulo  
if 0 <= angulo < 90:  
    print("El ángulo se encuentra en el primer cuadrante.")  
elif 90 <= angulo < 180:  
    print("El ángulo se encuentra en el segundo cuadrante.")  
elif 180 <= angulo < 270:  
    print("El ángulo se encuentra en el tercer cuadrante.")  
elif 270 <= angulo < 360:  
    print("El ángulo se encuentra en el cuarto cuadrante.")  
else:  
    print("El ángulo es 0 o 360 grados y está sobre el eje positivo X.")
