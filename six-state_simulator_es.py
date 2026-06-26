import random

FOTONCIO = "Fotoncio"
BITBERTO = "Bitberto"
EVETRON = "Evetron"

BASES = ["Z", "X", "Y"]
BITS = [0, 1]


def generar_lista(opciones, cantidad):
    return [random.choice(opciones) for _ in range(cantidad)]


def medir(bit_original, base_original, base_medicion):
    if base_original == base_medicion:
        return bit_original
    return random.choice(BITS)


def mostrar_lista(nombre, lista):
    print(f"{nombre}: {' '.join(map(str, lista))}")


def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("¿Cuántos bits quieres simular? Ejemplo 10, 20, 50: "))
            if cantidad > 0:
                return cantidad
            print("Escribe un número mayor que 0.")
        except ValueError:
            print("Escribe un número válido.")


def elegir_rol():
    print("Elige tu rol:")
    print("1. Ser Fotoncio")
    print("2. Ser Bitberto")
    print("3. Ser Evetron")

    rol = input("Escribe 1, 2 o 3: ").strip()

    while rol not in ["1", "2", "3"]:
        print("Opción no válida.")
        rol = input("Escribe 1, 2 o 3: ").strip()

    return rol

def preguntar_si_no(pregunta):
    while True:
        respuesta = input(pregunta + " (si/no): ").lower().strip()
        if respuesta in ["si", "s"]:
            return True
        if respuesta in ["no", "n"]:
            return False
        print("Por favor, responde 'si' o 'no'.")

def simular_six_state_protocol():
    rol = elegir_rol()

    print("\n=== SIMULADOR DEL PROTOCOLO DE SEIS ESTADOS (ESPAÑOL): Fotoncio, Bitberto y Evetron ===\n")

    cantidad = pedir_cantidad()

    # Decidir si hay espionaje
    if rol == "3":
        print("\n😈 Eres Evetron. Vas a espiar automáticamente.")
        evetron_activo = True
    else:
        evetron_activo = preguntar_si_no(f"¿{EVETRON} va a espiar? sí/no: ")

    # Generación
    bits_fotoncio = generar_lista(BITS, cantidad)
    bases_fotoncio = generar_lista(BASES, cantidad)
    bases_bitberto = generar_lista(BASES, cantidad)

    # Evetron interviene
    if evetron_activo:
        bases_evetron = generar_lista(BASES, cantidad)
        bits_despues_evetron = []

        for i in range(cantidad):
            bit_interceptado = medir(
                bits_fotoncio[i],
                bases_fotoncio[i],
                bases_evetron[i]
            )
            bits_despues_evetron.append(bit_interceptado)
    else:
        bases_evetron = ["-"] * cantidad
        bits_despues_evetron = bits_fotoncio.copy()

    # Bitberto mide
    bits_bitberto = []

    for i in range(cantidad):
        bit_recibido = medir(
            bits_despues_evetron[i],
            bases_fotoncio[i],
            bases_bitberto[i]
        )
        bits_bitberto.append(bit_recibido)

    # Crear clave (solo donde coinciden bases)
    clave_fotoncio = []
    clave_bitberto = []

    for i in range(cantidad):
        if bases_fotoncio[i] == bases_bitberto[i]:
            clave_fotoncio.append(bits_fotoncio[i])
            clave_bitberto.append(bits_bitberto[i])

    # Contar errores
    errores = 0
    for i in range(len(clave_fotoncio)):
        if clave_fotoncio[i] != clave_bitberto[i]:
            errores += 1

    # RESULTADOS SEGÚN ROL
    print("\n--- RESULTADOS SEGÚN TU ROL ---")

    if rol == "1":
        print(f"\nTú eres {FOTONCIO}.")
        mostrar_lista("Tus bits originales", bits_fotoncio)
        mostrar_lista("Tus bases", bases_fotoncio)
        mostrar_lista("Bases públicas de Bitberto", bases_bitberto)

    elif rol == "2":
        print(f"\nTú eres {BITBERTO}.")
        mostrar_lista("Tus bases", bases_bitberto)
        mostrar_lista("Tus bits medidos", bits_bitberto)
        mostrar_lista("Bases públicas de Fotoncio", bases_fotoncio)

    elif rol == "3":
        print(f"\nTú eres {EVETRON}.")
        mostrar_lista("Tus bases de espionaje", bases_evetron)
        mostrar_lista("Bits que intentaste medir", bits_despues_evetron)
        print("Si usaste la base equivocada, cambiaste algunos bits sin darte cuenta.")

    # INFORMACIÓN PÚBLICA
    print("\n--- INFORMACIÓN PÚBLICA ---")
    mostrar_lista("Bases de Fotoncio", bases_fotoncio)
    mostrar_lista("Bases de Bitberto", bases_bitberto)

    # CLAVE COMPARTIDA
    print("\n--- CLAVE COMPARTIDA ---")
    print("Solo se usan los bits donde Fotoncio y Bitberto eligieron la misma base.")

    if len(clave_fotoncio) == 0:
        print("No hay clave porque nunca coincidieron las bases.")
    else:
        mostrar_lista("Clave de Fotoncio", clave_fotoncio)
        mostrar_lista("Clave de Bitberto", clave_bitberto)

    # DETECCIÓN
    print("\n--- DETECCIÓN DE ESPIONAJE ---")

    if len(clave_fotoncio) == 0:
        print("No se pudo analizar la seguridad (sin clave).")

    elif errores > 0:
        print(f"🚨 ALERTA: Se detectaron {errores} errores.")
        print(f"{EVETRON} fue detectado espiando.")
        print("La clave NO es segura y debe descartarse.")

    else:
        if evetron_activo:
            print("⚠️ No se detectaron errores, PERO hubo espionaje.")
            print(f"{EVETRON} intervino, pero pudo pasar desapercibido.")
            print("La clave podría NO ser segura.")
        else:
            print("✅ No hubo espionaje.")
            print("La clave es segura.")

    # RESUMEN
    print("\n--- RESUMEN ---")
    print(f"Bits simulados: {cantidad}")
    print(f"Coincidencias de bases: {len(clave_fotoncio)}")
    print(f"Errores detectados: {errores}")

    if evetron_activo:
        print("Estado real: Evetron SI intervino.")
    else:
        print("Estado real: Evetron NO intervino.")


simular_six_state_protocol()
