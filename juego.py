import sys
import time

def juego_guardianes_de_lumina():
   
    print("==========================================")
    print("   Videojuego: Guardianes de Lumina       ")
    print("==========================================")
    
    iniciar = input("¿Deseas iniciar el juego? (Sí/No): ").strip().lower()
    
    if iniciar not in ['si', 'sí', 's']:
        print("\nSaliendo del juego...")  
        sys.exit()

    print("\n--- SELECCIÓN / CREACIÓN DE GUARDIÁN ---")
    guardian_nombre = input("Ingresa el nombre de tu Guardián: ")
    print(f"Guardián '{guardian_nombre}' creado con éxito.")

    print("\n--- ELEGIR DIFICULTAD ---")
    print("1. Fácil\n2. Normal\n3. Difícil")
    dificultad = input("Selecciona la dificultad (1-3): ")

    niveles = [
        "Nivel 1: Bosque de Éter",
        "Nivel 2: Templo del Sol",
        "Nivel 3: Ciudadela de Lumina (FINAL)"
    ]
    indice_nivel_actual = 0
    nivel_actual = niveles[indice_nivel_actual]  
    
    guardian_vivo = True
    jefe_derrotado = False

    while True:
        print("\n" + "="*40)
        print(f"    [ BUCLE PRINCIPAL - {nivel_actual.upper()} ]    ")
        print("="*40)

        if not guardian_vivo:
            print("\n----------------------------------")
            print("       PANTALLA DE DERROTA        ")
            print("----------------------------------")
            print("Has caído en batalla. Reintentando el nivel...")
            guardian_vivo = True  
            continue  

        if jefe_derrotado:
            print("\n----------------------------------")
            print("       ¡JEFE DERROTADO!           ")
            print("----------------------------------")
            
            print("Mostrar Recompensas: +500 Monedas, +1 Objeto Épico")

            if indice_nivel_actual == len(niveles) - 1:
                print("\n==============================================")
                print(" ¡FELICIDADES! HAS COMPLETADO EL NIVEL FINAL ")
                print("        ¡HAS SALVADO EL MUNDO DE LUMINA!      ")
                print("==============================================")
                break  
            else:

                indice_nivel_actual += 1
                nivel_actual = niveles[indice_nivel_actual]
                print(f"\nCargando siguiente nivel: {nivel_actual}...")
                jefe_derrotado = False
                continue 

        print("\n[ Actualizando Enemigos, Trampas y Poderes... ]")

        print(f"\n--- HUD ---")
        print(f"Jugador: {guardian_nombre} | Ubicación: {nivel_actual}")
        print("Vida: 100/100 | Maná: 50/50 | Monedas: 120")
        print("Habilidades disponibles: [1] Ataque Básico [2] Bola de Fuego")

        print("\nAcciones disponibles:")
        print("1. Mover")
        print("2. Atacar")
        print("3. Usar Habilidad")
        print("4. Pausa")
        print("5. [Simulación] Perder vida y Morir")
        print("6. [Simulación] Derrotar al Jefe del nivel actual")
        
        accion = input("Procesar entrada del jugador: ").strip()

        if accion == "1":
            print(f"-> {guardian_nombre} se desplaza por el {nivel_actual}.")
        elif accion == "2":
            print(f"-> {guardian_nombre} realiza un ataque!")
        elif accion == "3":
            print(f"-> {guardian_nombre} usa una habilidad especial.")
        elif accion == "4":
            print("-> Juego en Pausa.")
        elif accion == "5":
            print("-> Te has quedado sin vida...")
            guardian_vivo = False
        elif accion == "6":
            print(f"-> ¡Has propinado el golpe final al jefe de {nivel_actual}!")
            jefe_derrotado = True
        else:
            print("-> Acción no válida, intenta de nuevo.")
            
        time.sleep(1)

if __name__ == "__main__":
    juego_guardianes_de_lumina()