def merge_sort(tareas):
    if len(tareas) <= 1:
        return tareas
    
    mid = len(tareas) // 2
    left = merge_sort(tareas[:mid])
    right = merge_sort(tareas[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if (left[i]["prioridad"] > right[j]["prioridad"]) or \
           (left[i]["prioridad"] == right[j]["prioridad"] and left[i]["tiempo"] < right[j]["tiempo"]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


tareas = [
    {"nombre": "N1", "prioridad": 3, "tiempo": 5},
    {"nombre": "N2", "prioridad": 2, "tiempo": 2},
    {"nombre": "N3", "prioridad": 3, "tiempo": 3},
    {"nombre": "N1", "prioridad": 7, "tiempo": 5},
    {"nombre": "N2", "prioridad": 1, "tiempo": 2},
    {"nombre": "N3", "prioridad": 5, "tiempo": 3}
]

print("Lista original")
print(tareas)

print("Lista ordenada: ")

tareas_ordenadas = merge_sort(tareas)
for tarea in tareas_ordenadas:
    
    print(f"Nombre: {tarea['nombre']}, Prioridad: {tarea['prioridad']}, Tiempo: {tarea['tiempo']}")
