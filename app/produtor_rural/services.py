def validate_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    digit_1 = 11 - (total % 11)
    if digit_1 > 9:
        digit_1 = 0

    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    digit_2 = 11 - (total % 11)
    if digit_2 > 9:
        digit_2 = 0

    if int(cpf[9]) == digit_1 and int(cpf[10]) == digit_2:
        return True
    else:
        return False

def validate_cnpj(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))

    if len(cnpj) != 14:
        return False

    total = 0
    pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(12):
        total += int(cnpj[i]) * pesos[i]
    digit_1 = 11 - (total % 11)
    if digit_1 > 9:
        digit_1 = 0

    # Calcula o segundo dígito verificador
    total = 0
    pesos.insert(0, 6)
    for i in range(13):
        total += int(cnpj[i]) * pesos[i]
    digit_2 = 11 - (total % 11)
    if digit_2 > 9:
        digit_2 = 0

    # Verifica se os dígitos verificadores estão corretos
    if int(cnpj[12]) == digit_1 and int(cnpj[13]) == digit_2:
        return True
    else:
        return False
