def cyk(grammar: dict, start_symbol: str, input_string: str) -> bool:
    n = len(input_string)
    # Inicializar la tabla CYK
    table = [[set() for _ in range(n)] for _ in range(n)]

    # Llenar la primera fila de la tabla
    for i in range(n):
        for production in grammar:
            if input_string[i] in grammar[production]:
                table[i][i].add(production)

    # Calcular las celdas restantes de la tabla
    for l in range(2, n + 1):
        for s in range(n - l + 1):
            for p in range(s, s + l - 1):
                for production in grammar:
                    for rule in grammar[production]:
                        if len(rule) == 2:
                            for a in table[s][p]:
                                for b in table[p + 1][s + l - 1]:
                                    if (a + b) in grammar[production]:
                                        table[s][s + l - 1].add(production)

    # Verificar si la cadena es aceptada
    return start_symbol in table[0][n - 1]

# Ejemplo de uso:
if __name__ == "__main__":
    # Lectura de la gramática
    grammar = {}
    num_productions = int(input())
    for _ in range(num_productions):
        num_non_terminals, num_queries = [int(_) for _ in input().split()]
        for _ in range(num_non_terminals):
            production_line = input().split()
            non_terminal = production_line[0]
            grammar[non_terminal] = set(production_line[1:])

        # Lectura de las consultas
        for _ in range(num_queries):
            input_string = input().strip()
            if cyk(grammar, 'S', input_string):
                print("yes")
            else:
                print("no")
