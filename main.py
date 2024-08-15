from operaçoes import calcular_media, foi_reprovado, gerar_relatorio_reprovados


dados_alunos = {
    26: {'nome': 'Maria', 'notas': [7.5, 8.0, 6.5, 7.0]},
    13: {'nome': 'João', 'notas': [5.5, 6.0, 6.5, 6.0]},
    101: {'nome': 'Ana', 'notas': [4.5, 5.0, 5.5, 4.9]},
    37: {'nome': 'Ágatha', 'notas': [8.0, 6.0, 7.5, 9.0]},
    72: {'nome': 'Joaquim', 'notas': [6.0, 5.5, 5.0, 7.0]},
    5: {'nome': 'Félix', 'notas': [10.0, 8.0, 8.0, 8.0]}  

}


matriculas_reprovados = []


for matricula, dados in dados_alunos.items():
    media = calcular_media(dados['notas'])
    dados_alunos[matricula]['media'] = media  
    
    if foi_reprovado(media):
        matriculas_reprovados.append(matricula)

relatorio_reprovados = gerar_relatorio_reprovados(dados_alunos, matriculas_reprovados)
for linha in relatorio_reprovados:
    print(linha)


