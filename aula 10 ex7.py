def restaurante():
     print('''
     RESTAURANTE YZ
     FAÇA O SEU PEDIDO: 
     DIGITE  1 SALADA - 2 MACARRONADA - 3 SANDUICHE  - 4 SORVETE 
     ''')
     opcao = input('>>')
     if opcao == '1':
        print('Você escolheu salada') 
     elif opcao == '2':
        print('Você escolheu Macarronada')  
     elif opcao == '3':
        print('Você escolheu sanduiche')  
     elif opcao == '4':
        print('Você escolheu sorvete')
     else:
         print('Não existe essa opção')
         
restaurante()
