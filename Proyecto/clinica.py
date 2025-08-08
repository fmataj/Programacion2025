# Datos de pacientes
pacientes = [
    ["116640019", 61727979, "San José", "Desamparados", "gripe", "acetaminofen"],
    ["603240305", 120450711, "Heredia", "Santo Domingo", "gastritis", "antiácido"],
    ["503980535", 70713699, "Alajuela", "San Carlos", "tos", "jarabe"],
    ["111111111", 11111111, "Cartago", "Paraíso", "migraña", "acetaminofen"],
    ["116310912", 88070036, "San José", "Curridabat", "dolor", "acetaminofen"],
    ["604830325", 83155658, "Puntarenas", "Osa", "gripe", "acetaminofen"],
    ["111111111", 64069212, "Guanacaste", "Liberia", "gastritis", "antiácido"],
    ["111860150", 88447416, "Limón", "Puerto Viejo", "diabetes", "insulina"],
    ["110283", 61088556, "San José", "Escazú", "asma", "salbutamol"],
    ["503810832", 83076969, "Heredia", "Barva", "gripe", "acetaminofen"],
    ["114740407", 70112487, "Cartago", "Turrialba", "hipotiroidismo", "levotiroxina"],
    ["205750691", 83349456, "San José", "Montes de Oca", "alergias", "loratadina"],
    ["215487963", 78823654, "Guanacaste", "Nicoya", "migraña", "acetaminofen"],
    ["318540762", 65892345, "Alajuela", "Grecia", "presión alta", "amlodipino"],
    ["457821904", 72908475, "Cartago", "Oreamuno", "dolor de espalda", "ibuprofeno"],
    ["602948176", 61928374, "Heredia", "Belén", "ansiedad", "clonazepam"],
    ["111111111", 63487294, "Limón", "Guápiles", "diabetes", "insulina"],
    ["825613092", 72845312, "Puntarenas", "Coto Brus", "asma", "salbutamol"],
    ["908124753", 71239485, "San José", "Moravia", "alergias", "cetirizina"],
    ["120450711", 63749562, "Heredia", "San Isidro", "gastritis", "omeprazol"],
    ["200145879", 78546932, "Guanacaste", "Santa Cruz", "presión alta", "losartán"],
    ["305946278", 65849371, "Puntarenas", "Golfito", "tos", "jarabe"],
    ["412598764", 73284956, "San José", "Tibás", "dolor de espalda", "paracetamol"],
    ["507812394", 69231875, "Cartago", "El Guarco", "ansiedad", "diazepam"],
    ["602938574", 61249375, "Limón", "Siquirres", "diabetes", "metformina"],
    ["715498372", 74938261, "Alajuela", "Atenas", "asma", "fluticasona"],
    ["823654091", 69829375, "San José", "Pérez Zeledón", "alergias", "loratadina"],
    ["912475683", 73485629, "Cartago", "Jiménez", "hipotiroidismo", "levotiroxina"],
    ["104598273", 68597312, "Heredia", "San Rafael", "gripe", "acetaminofen"],
    ["205963184", 71928364, "Puntarenas", "Esparza", "gastritis", "pantoprazol"],
    ["301456897", 64395721, "San José", "Alajuelita", "migraña", "ibuprofeno"],
    ["401598723", 71928574, "Limón", "Matina", "presión alta", "enalapril"],
    ["510298374", 62938475, "Guanacaste", "Bagaces", "asma", "salbutamol"],
    ["621095837", 75928346, "Cartago", "Turrialba", "diabetes", "insulina"],
    ["732145609", 68495731, "Heredia", "Flores", "dolor", "acetaminofen"],
    ["802149357", 72938475, "San José", "Goicoechea", "gastritis", "omeprazol"],
    ["913256748", 65849371, "Puntarenas", "Buenos Aires", "presión alta", "amlodipino"],
    ["102548397", 67293857, "Limón", "Talamanca", "asma", "salbutamol"],
    ["204985763", 74583925, "Guanacaste", "Carrillo", "gripe", "acetaminofen"]
]

while True:
    print("\n=== MAPA EPIDEMIOLÓGICO ===")
    print("1. Conteo por provincia y enfermedad")
    print("2. Medicina más recetada")
    print("3. Ranking de enfermedades más comunes")
    print("4. Buscar brote en provincia")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        provincias = []
        conteo = []
        for p in pacientes:
            clave = (p[2], p[4])
            if clave in provincias:
                conteo[provincias.index(clave)] += 1
            else:
                provincias.append(clave)
                conteo.append(1)
        print("\n--- Pacientes por provincia y enfermedad ---")
        for i in range(len(provincias)):
            print(f"{provincias[i][0]} - {provincias[i][1]}: {conteo[i]} casos")

    elif opcion == "2":
        medicinas = []
        conteo = []
        for p in pacientes:
            if p[5] in medicinas:
                conteo[medicinas.index(p[5])] += 1
            else:
                medicinas.append(p[5])
                conteo.append(1)
        max_cantidad = max(conteo)
        mas_usada = medicinas[conteo.index(max_cantidad)]
        print(f"\n💊 La medicina más recetada es '{mas_usada}' con {max_cantidad} recetas.")

    elif opcion == "3":
        enfermedades = []
        conteo = []
        for p in pacientes:
            if p[4] in enfermedades:
                conteo[enfermedades.index(p[4])] += 1
            else:
                enfermedades.append(p[4])
                conteo.append(1)
        # Ranking manual (sin sort)
        print("\n🏆 Ranking de enfermedades:")
        for _ in range(len(enfermedades)):
            idx = conteo.index(max(conteo))
            print(f"{enfermedades[idx]} - {conteo[idx]} casos")
            conteo[idx] = -1

    elif opcion == "4":
        provincia = input("Ingrese la provincia: ")
        enfermedades_prov = []
        conteo = []
        for p in pacientes:
            if p[2].lower() == provincia.lower():
                if p[4] in enfermedades_prov:
                    conteo[enfermedades_prov.index(p[4])] += 1
                else:
                    enfermedades_prov.append(p[4])
                    conteo.append(1)
        for i in range(len(enfermedades_prov)):
            if conteo[i] > 3:
                print(f"⚠️ ALERTA: Brote de {enfermedades_prov[i]} ({conteo[i]} casos)")
        if not enfermedades_prov:
            print("No se encontraron pacientes en esa provincia.")

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción no válida.")
