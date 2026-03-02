def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido.")

def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Digite um número válido.")