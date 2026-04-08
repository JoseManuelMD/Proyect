from linked_list import LinkedList
from visualizer import clear_screen, print_histogram
from utils import generate_random_list
# from algorithms import bubble_sort, selection_sort, ... (importa todos)

def main():
    while True:
        clear_screen()
        print("=" * 70)
        print("     VISUALIZADOR DE ORDENAMIENTO - LISTAS LIGADAS")
        print("=" * 70)
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Salir")
        print("-" * 70)

        try:
            opcion = int(input("\nElige una opción (1-6): "))
            if opcion == 6:
                print("\n¡Hasta luego!")
                break
            if opcion < 1 or opcion > 5:
                input("Opción inválida...")
                continue
        except:
            input("Entrada inválida...")
            continue

        # Resto del código (tamaño, velocidad, crear lista, ejecutar algoritmo, etc.)

        # Al final:
        input("\nPresiona Enter para volver al menú...")

if __name__ == "__main__":
    main()
