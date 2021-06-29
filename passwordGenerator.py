# resumo: gerador de senhas simples, status: funciona!
import random

lower = 'abcdefghijkmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKMNOPQRSTUVWXYZ'
numbers = '0123456789'

caracteres = lower + upper + numbers
# Em length determinamos a quantia de caracteres da senha
length = 10
password = ''.join(random.sample(caracteres, length))
print('Sua senha será: {}'.format(password))