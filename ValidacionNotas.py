nota=float(input("Ingrese la nota final (0-20): "))
#1 y 2. Validación
if nota <0 or nota >20:
    print("Nota fuera de rango")
else:
    #3. Asignar categoria.
    if nota >=18:
        categoria="Sobresaliente"
    elif nota >=16 and nota <=18:
        categoria="Muy bueno"
    elif nota>=14 and nota <=16:
        categoria="Bueno"
    elif nota >=12 and nota <=14:
        categoria="Suficiente"
    else:
        categoria ="Insuficiente"
    print("Categoria: ",categoria)
    #4. Mensaje extra si es insuficiente y <8
    if categoria=="Insuficiente" and nota<8:
        print("Debe asistir a tutorias obligatorias")
    #5.Mensaje entre si es Sobresaliente y nota>=19.5
    if categoria=="Sobresaliente" and nota >=19.5:
        print("Candidato a mención de honor")
        