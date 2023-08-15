# programa que mostre a media do aluno com suas duas notas e mostre se ele foi aprovado ou reprovado

n1 = float(input('Digite sua 1º nota: '))
n2 = float(input('Digite sua 2º nota: '))

media = 7.0
mediaAluno = (n1+n2)/2

if mediaAluno >= media:
    print('o aluno tirou a media de {} e a media nescessaria para passar é {} então o aluno foi \033[32maprovado!\033[m' .format(
        mediaAluno, media))

else:
    print('o aluno tirou a media de {} e a media nescessaria para passar é {} então o aluno foi \033[31mReprovado!' .format(
        mediaAluno, media))
