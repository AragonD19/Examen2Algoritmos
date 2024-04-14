def count_combinations(n):
    # Mapping del teclado del Nokia 3230
    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]

    # Inicializar la memoria para almacenar los resultados de los subproblemas
    memo = {}

    # Función auxiliar para calcular el número de combinaciones posibles para una longitud n y un dígito específico
    def count_combinations_recursive(n, digit):
        # Verificar si el resultado para el subproblema ya está en la memoria
        if (n, digit) in memo:
            return memo[(n, digit)]

        # Caso base: cuando n es 1, solo hay una combinación posible
        if n == 1:
            return 1

        x, y = divmod(digit, 3)
        adjacent_keys = [(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        total_combinations = 0

        # Calcular el número de combinaciones para dígitos de longitud n
        for nx, ny in adjacent_keys:
            if 0 <= nx < 4 and 0 <= ny < 3 and keypad[nx][ny] != '#':
                next_digit = nx * 3 + ny
                total_combinations += count_combinations_recursive(n - 1, next_digit)

        # Guardar el resultado en la memoria
        memo[(n, digit)] = total_combinations
        return total_combinations

    total_combinations = 0

    # Calcular el número de combinaciones posibles para dígitos de longitud n comenzando desde cada dígito
    for i in range(10):
        total_combinations += count_combinations_recursive(n, i)

    return total_combinations

# Ejemplo de uso
n = 10
print("Cantidad de combinaciones posibles para n =", n, ":", count_combinations(n))
