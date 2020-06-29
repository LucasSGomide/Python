#! python
import sys

print("Responda com 'V' ou 'F' as perguntas a seguir")

raça = input('Qual sua classe ? DRUID (D) SORCERER(S) KNIGHT(K) PALADIN(P)')
soft_boots = input('Está equipando soft boots?')
life_ring = input('Está equipando life ring?')
ROH = input('Está equipando ring of healing?')

reg_paladin = 2
reg_knight = 1
reg_sorc = 3
reg_druid = 3
reg_soft_seg = 5
reg_ROH_seg = 4
reg_LR_seg = 2
reg_comum = 2

if __name__ == '__main__':
    if len(raça) > 1 or len(soft_boots) > 1 or len(life_ring) > 1 or len(ROH) > 1:
        print('ERRO: SIGA DE FORMA CORRETA OS PARÂMETROS')
        print('Sintaxe: "V" ou "F" e INICIAL DA SUA CLASSE')
        sys.exit(1)
    if soft_boots == 'V' and life_ring == 'V' and ROH == 'F':
        print('Sua regeneração por min é:',
              ((reg_soft_seg + reg_LR_seg + reg_comum) * (60)))
    elif soft_boots == 'V' and life_ring == 'F' and ROH == 'V':
        print('Sua regeneração por min é:',
              ((reg_soft_seg + reg_ROH_seg + reg_comum) * (60)))
    else:
        print('ERRO: SIGA DE FORMA CORRETA OS PARÂMETROS')
        print('Sintaxe: "V" ou "F" e INICIAL DA SUA CLASSE')
        sys.exit(1)
else:
    sys.exit(1)
