def registrar_gasto(gastos):
    descripcion = input("Ingrese la descripción del gasto: ").strip()

    while True:
        try:
            monto = float(input("Ingrese el monto del gasto ($): "))
        except ValueError:
            print("Error: escriba un número (ej. 12.50).")
            continue

        if monto <= 0:
            print("Error: el monto debe ser mayor a 0.")
            continue

        break

    categoria = input("Ingrese la categoría (Comida/Transporte/Ocio/Otros): ").strip().capitalize()

    gastos.append({
        "descripcion": descripcion,
        "monto": monto,
        "categoria": categoria
    })
    print("-> Gasto registrado con éxito.")


def ver_gastos(gastos):
    if not gastos:
        print("Aún no hay gastos registrados.")
        return

    print("\n--- TODOS LOS GASTOS ---")
    for i, gasto in enumerate(gastos, start=1):
        print(f"{i}. {gasto['descripcion']} | {gasto['categoria']} | ${gasto['monto']:.2f}")


def filtrar_por_categoria(gastos):
    categoria = input("Ingrese la categoría a filtrar: ").strip().capitalize()
    gastos_filtrados = [g for g in gastos if g["categoria"] == categoria]

    if not gastos_filtrados:
        print(f"No hay gastos en la categoría '{categoria}'.")
        return

    print(f"\n--- GASTOS DE {categoria.upper()} ---")
    for i, gasto in enumerate(gastos_filtrados, start=1):
        print(f"{i}. {gasto['descripcion']} | ${gasto['monto']:.2f}")


def ver_resumen_total(gastos):
    if not gastos:
        print("Aún no hay gastos registrados.")
        return

    total = 0
    por_categoria = {}

    for gasto in gastos:
        total += gasto["monto"]
        cat = gasto["categoria"]
        por_categoria[cat] = por_categoria.get(cat, 0) + gasto["monto"]

    print("\n--- RESUMEN DE GASTOS ---")
    print(f"Total general: ${total:.2f}")
    for cat, subtotal in por_categoria.items():
        print(f"* {cat}: ${subtotal:.2f}")


gastos = []

while True:
    print("\n=== GESTOR DE GASTOS ===")
    print("1. Registrar gasto")
    print("2. Ver todos los gastos")
    print("3. Filtrar por categoría")
    print("4. Ver resumen total")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        registrar_gasto(gastos)
    elif opcion == "2":
        ver_gastos(gastos)
    elif opcion == "3":
        filtrar_por_categoria(gastos)
    elif opcion == "4":
        ver_resumen_total(gastos)
    elif opcion == "5":
        print("Saliendo del gestor de gastos...")
        break
    else:
        print("Opción inválida. Por favor, elija una opción válida.")
   

       


      
       
