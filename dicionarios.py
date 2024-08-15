meu_dicionario = {
    1: "Python",
    2: "Java",
    3: "PHP"
}
print(meu_dicionario)

print(type(meu_dicionario))

print(meu_dicionario.get(1))

print(len(meu_dicionario))

dicionario_frutas = dict({
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maçã", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
})

print(dicionario_frutas[1]["nome"])
print(dicionario_frutas[1]["tipo"])

print(dicionario_frutas[2]["nome"])
print(dicionario_frutas[2]["tipo"])

for chave, frutas in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {frutas['nome']}, Tipo: {frutas['tipo']}")
    


