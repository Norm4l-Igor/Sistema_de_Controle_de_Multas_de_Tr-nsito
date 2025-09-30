placa_do_veiculo = input()
nome_do_motorista = input()
velocidade_registrada = int(input())
velocidade_maxima_permitida = int(input())
multado_anteriorment = input()
pagemento = input()
infracao_leve = 130.16
infracao_grave = 195.23
infracao_gravissima = 880.41

print("Placa:", placa_do_veiculo)
print("Motorista:", nome_do_motorista)
print("Velocidade registrada:", velocidade_registrada, "km/h")
print("Velocidade máxima permitida:", velocidade_maxima_permitida, "km/h")


if velocidade_registrada <= velocidade_maxima_permitida:
    print("Infração: Nenhuma. Nenhuma penalidade aplicada.")
elif velocidade_registrada <= velocidade_maxima_permitida * 1.2:
    print(f"Infração: Leve - Multa de R$ {infracao_leve}, 0 pontos na CNH.")
elif velocidade_registrada <= velocidade_maxima_permitida * 1.5:
    if multado_anteriorment == 'sim':
        print("Multa DOBRADA por reincidência!")
        desconto = input("Deseja pagar a multa agora (Sim/Não): ")
        if desconto == 'nao':
            print(f"Infração grave: Multa de R$ {infracao_grave * 2} e adição de 5 pontos na CNH.")
            print(f"Atenção: Multa DOBRADA por reincidência!")
        elif desconto == 'sim':
            print(f"Você recebeu um desconto de 20%: R$ {infracao_grave * 0.8}")
        else:
            print("Opção inválida para desconto.")
    else:
        print(f"Infração grave: Multa de R$ {infracao_grave} e adição de 5 pontos na CNH.")
else:
    if multado_anteriorment == 'sim' or multado_anteriorment == 'Sim' or multado_anteriorment == 'SIM':     
        print(f"Infração: Gravíssima - Multa de R$ {infracao_gravissima:.2f}, 7 pontos na CNH e suspensão da carteira.")
        print(f"Atenção: Multa DOBRADA por reincidência!")
        print("Atenção: CNH suspensa! Compareça ao Detran.")
        print("Atenção: Você precisa fazer um curso de reciclagem no Detran.")
        if pagemento == 'Sim' or pagemento == 'sim':
            print(f"Pagamento realizado! Você recebeu um desconto de 20%. Valor final: {infracao_gravissima * 2 * 0.8:.2f}")
    else:
        if multado_anteriorment == 'nao' or multado_anteriorment == 'Nao' or multado_anteriorment == 'NAO':
            print(f"Infração: Gravíssima - Multa de R$ {infracao_gravissima:.2f}, 7 pontos na CNH e suspensão da carteira.")
            print(f"Atenção: Multa DOBRADA por reincidência!")
            print("Atenção: CNH suspensa! Compareça ao Detran.")
            print("Atenção: Você precisa fazer um curso de reciclagem no Detran.")
        if pagemento == 'Sim' or pagemento == 'sim':
                print(f"Pagamento realizado! Você recebeu um desconto de 20%. Valor final: {infracao_gravissima * 0.8:.2f}")


