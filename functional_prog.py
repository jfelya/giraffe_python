def double(list):
    new_arr = []
    for i in list:
        new_arr.append(i**2)
    return new_arr


orig_arr = [1, 2, 3, 4, 5, 6]
new_new_list = double(orig_arr)

# print(f"Original list: {orig_arr}")
# print(f"New list: {new_new_list}")


# Sumar números de una lista sin bucles
def Sumar_lista(lista, n):
    print(lista[n])
    # Caso base
    if n == 0:
        return lista[n]
    else:
        # Recursión
        return lista[n] + Sumar_lista(lista, n - 1)

mi_lista = [1, 2, 3]
print(Sumar_lista(mi_lista, len(mi_lista) - 1))

# Funciones de primera clase
