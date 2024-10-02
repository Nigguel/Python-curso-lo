primer_valor = input("Escriba um valor: ")
segundo_valor = input("Escriba otro valor: ")

int_primer_valor = int(primer_valor)
int_segundo_valor = int(segundo_valor)

if int_primer_valor > int_segundo_valor:
    print(
        f"El primer valor ({int_primer_valor}) es mayor que el segundo valor ({int_segundo_valor})"
    )
elif int_segundo_valor > int_primer_valor:
    print(
        f"El segundo valor ({int_segundo_valor}) es mayor que el primer valor ({int_primer_valor})"
    )
else:
    print("Los valores son iguales")
