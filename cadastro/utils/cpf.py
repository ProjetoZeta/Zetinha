"""
function created according the rules described on http://www.geradorcpf.com/algoritmo_do_cpf.htm
"""
import re

def fetch_check_digit(snippet, list_weights):
    total = 0
    for algarism in snippet:
        weight = list_weights.pop(0)
        total += int(algarism) * weight
    rest = total % 11
    if rest < 2:
        return 0
    else:
        return 11 - rest

def is_cpf_valid(raw_cpf):
    """
    cpf_is_valid(): It receives a cpf and return True if it's valid or False otherwise
    """
    cpf = raw_cpf.replace('.', '').replace('-', '')  # It removes dots and hyphens
    cpf_pattern = re.compile("^[0-9]{11}$")  # It defines that the string must contais 11 number characters
    if cpf_pattern.match(cpf):
        first_check_digit = fetch_check_digit(cpf[0:9], [10,9,8,7,6,5,4,3,2])
        second_check_digit = fetch_check_digit("{}{}".format(cpf[0:9], first_check_digit), [11,10,9,8,7,6,5,4,3,2])
        return cpf == "{}{}{}".format(cpf[0:9], first_check_digit, second_check_digit)
    else:
        return False


def is_cnpj_valid(raw_cpf):
    """
    cpf_is_valid(): It receives a cpf and return True if it's valid or False otherwise
    """
    cnpj = raw_cpf.replace('.', '').replace('-', '').replace('/', '')  # It removes dots and hyphens
    cpf_pattern = re.compile("^[0-9]{14}$")  # It defines that the string must contais 14 number characters
    if cpf_pattern.match(cnpj):
        first_check_digit = fetch_check_digit(cnpj[0:12], [5,4,3,2,9,8,7,6,5,4,3,2])
        second_check_digit = fetch_check_digit("{}{}".format(cnpj[0:12], first_check_digit), [6,5,4,3,2,9,8,7,6,5,4,3,2])
        return cnpj == "{}{}{}".format(cnpj[0:12], first_check_digit, second_check_digit)
    else:
        return False