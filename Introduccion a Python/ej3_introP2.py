def dado(numero):
    if numero < 1 or numero > 6:
        return "inkorrect numerou"
    else:
        return 7 - numero

print(dado(5))