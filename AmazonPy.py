# ----------Listas----------------
listUsers = []
listElectronic= []
listAppliance = []
listFurniture = []
listBook = []
listShoppingCart = []


#---Cores-do-Sistema----
RED   = "\033[1;31m"  
PURPLE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
GREY = "\033[1;90m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
YELLOW = "\033[1;33m"
REVERSE = "\033[;7m"


# --------------Classes-------------
#-------Classe-do-Cadastro---------
class Registration:
    name = None
    email = None
    password = None
    cpf = None


#-----Classe-dos-Produtos----
class functionProduct:
    description = None
    price = 0
    quantity = 0


#--------Funções---------------
# -----------Função-de-Dividir-Linha-------------
def divideLine():
    print(f"{BOLD}-{RESET}" * 40)


#------Funções-dos-Produtos----
#--------Função-dos-Eletronicos----

def Eletronics():
    products = functionProduct()
    products.description = 'Samsung Monitor - 21,5 - Preto Brilhante'
    products.price = 986.00
    listElectronic.append(products)
    products = functionProduct()
    products.description = 'Fone de Ouvido Philco - Bluetooth  - Preto'
    products.price = 130.00
    listElectronic.append(products)
    products = functionProduct()
    products.description = 'Caixa de som gamer Redragon Anvil RGB PRETO'
    products.price = 188.00
    listElectronic.append(products)
    products = functionProduct()
    products.description = 'Tablet M7S Go, Multilaser, Nb317, 16, 7'', Branco'
    products.price = 305.00
    listElectronic.append(products)


#----Função-dos-Eletrodomesticos------
def Appliances():
    products = functionProduct()
    products.description = 'Freezer portátil de carro 4L'
    products.price = 408.00
    listAppliance.append(products)
    products = functionProduct()
    products.description = 'Forno Elétrico De Embutir 46L'
    products.price = 880.00
    listAppliance.append(products)
    products = functionProduct()
    products.description = 'Fogão Star 4 Bocas Branco - Bivolt - Itatiaia'
    products.price = 519.00
    listAppliance.append(products)
    products = functionProduct()
    products.description = 'Micro-Ondas - Philco - 20 Litros - 220V'
    products.price = 469.00
    listAppliance.append(products)


#---Função-dos-Moveis-----
def Furniture():
    products = functionProduct()
    products.description = 'Cama Box Conjugado Casal - Ortobom'
    products.price = 389.00
    listFurniture.append(products)
    products = functionProduct()
    products.description = 'Guarda Roupa Casal Espelho 6 Portas 2 Gavetas Real Atualle'
    products.price = 485.00
    listFurniture.append(products)
    products = functionProduct()
    products.description = 'Sofá 3 Lugares Retrátil - Lubeck Plush Suede - Grafite'
    products.price = 840.00
    listFurniture.append(products)
    products = functionProduct()
    products.description = 'Estante Home para TV até 52 Polegadas - 2 Portas - Branca'
    products.price = 500.00
    listFurniture.append(products)


#----Função-dos-Livros---------
def Books():
    products = functionProduct()
    products.description = 'Coleção Harry Potter - 7 Volumes (português)'
    products.price = 135.00
    listBook.append(products)
    products = functionProduct()
    products.description = 'Box Percy Jackson e os olimpianos'
    products.price = 150.00
    listBook.append(products)
    products = functionProduct()
    products.description = 'Box Os Instrumentos Mortais'
    products.price = 160.00
    listBook.append(products)
    products = functionProduct()
    products.description = 'Pai rico, pai pobre: Edição de 20 anos atualizada e ampliada'
    products.price = 36.00
    listBook.append(products)


#---Função-do-Menu-Iniciar-----~
def Interface(User, Saldo):
    Title(User, Saldo)
    print(f"{PURPLE} {' → CADASTRE-SE (0)':^40} {RESET}")
    divideLine()
    print(f"{PURPLE} {' → ENTRAR NA CONTA (1)':^40} {RESET}")
    divideLine()
    print(f"{PURPLE} {' → PRODUTOS (2)':^40} {RESET}")
    divideLine()
    print(f"{PURPLE} {' → CARRINHO (3)':^40} {RESET}")
    divideLine()
    print(F"{PURPLE} {' → DESENVOLVEDORES (4)':^40} {RESET}")
    divideLine()
    print(f"{PURPLE} {' → SAIR (5)':^40} {RESET}")
    divideLine()


#---Função-de-Informações-do-Usuario-----
def Title(User, Balance):
    divideLine()
    print(f"{CYAN} {'AMAZON.COM':^40} {RESET}")
    message = '  BEM-VINDO ' + User 
    messageBalance = 'Saldo: R$ ' + str(Balance)
    print(f"{CYAN} {message:^40} {RESET}")
    print(f"{GREEN} {messageBalance:^40} {RESET}")
    divideLine()
    

# --------------Função-de-Cadastro-----------------
def Inscribe():
    # --------------------Nome--------------------
    user_registrer = Registration()
    while True:
        divideLine()
        print(f"{PURPLE} {'»» SEU CRÉDITO SERÁ DE R$ 1.000,00 ««':^40} {RESET}")
        divideLine()
        print(f"{CYAN}• DIGITE SEU NOME: {RESET}")
        name = str(input(f"{GREEN}→ {RESET}"))
        divideLine()
        accountName = 0
        for travel in range(len(name)):
            if name[travel].isdigit() == False:
                accountName +=1
        if accountName == len(name):
            user_registrer.name = name
            break
        else:
            print("\n" *5)
            divideLine()
            print(f"{RED} {'» SOMENTE LETRAS «':^40} {RESET}")   


    # -----------------Email-----------------------
    while True:
        print(f"{CYAN}• DIGITE SEU E-MAIL: {RESET}")
        email = str(input(f"{GREEN}→ {RESET}"))
        counter = 0

        for emailCheck in range(len(listUsers)):
            if email == listUsers[emailCheck].email:
                counter+=1
            else:
                continue

        if counter == 0:    
            divideLine()
            if '@' in email:
                user_registrer.email = email
                break
            else:
                print(f"{RED} {'» SEU E-MAIL NÃO POSSUI @ «':^40} {RESET}")
                divideLine()
        else:
            divideLine()
            print(f"{RED} {'» EMAIL JÁ CADASTRADO «':^40} {RESET}")
            divideLine()


    # -----------------Senha-----------------------
    while True:
        print(f"{CYAN}• CRIE UMA SENHA (MÍNIMO DE 6 CARACTERES): {RESET}")
        password = str(input(f"{GREEN}→ {RESET}"))
        divideLine()
        if len(password) >= 6:
            user_registrer.password = password
            break
        else:
            print(f"{RED} {'» SUA SENHA DEVE POSSUIR NO MÍNIMO 6 CARACTERES! «':^40} {RESET}")
            divideLine()

    # -----------------CPF-----------------------
    while True:
        print(f"{CYAN}• DIGITE SEU CPF: (APENAS NÚMEROS){RESET}")
        cpf = str(input(f"{GREEN}→ {RESET}"))
        counter = 0

        sum1 = sum2 = 0
        if len(cpf) == 11:
            cpf = int(cpf)  # 11144477705
            cpf_nine = test1 = cpf // 100  # 111444777
            for i in range(2, 11):
                rest1 = test1 % 10  # 7
                sum1 += rest1 * i  # 7*2
                test1 = test1 // 10  # 11144477
            div1 = sum1 % 11  # resto 8
            if div1 < 2:
                dig1 = ('0')
                cpf_ten = str(cpf_nine) + dig1
            else:
                dig1 = 11 - div1
                dig1 = str(dig1)
                cpf_ten = test2 = str(cpf_nine) + dig1
            test2 = int(cpf_ten)
            for j in range(2, 12):
                rest2 = test2 % 10  # 3
                sum2 += rest2 * j  # 3*2
                test2 = test2 // 10
            div2 = sum2 % 11  # resto 6
            if div2 < 2:
                dig2 = ('0')
                cpfvalid = str(cpf_ten) + dig1
                cpfvalid = int(cpfvalid)
            else:
                dig2 = 11 - div2
                dig2 = str(dig2)
                cpfvalid = str(cpf_ten) + dig2
                cpfvalid = int(cpfvalid)

            for cpfCheck in range(len(listUsers)):
                if cpf == listUsers[cpfCheck].cpf:
                    counter+=1
                else:
                    continue
            if counter == 0:
                if cpf == cpfvalid:
                    user_registrer.cpf = cpf
                    break
                else:
                    divideLine()
                    print(f"{RED} {'» ESTE CPF NÃO É VÁLIDO! «':^40} {RESET}")
                    divideLine()
            else:
                divideLine()
                print(f"{RED} {'» CPF JÁ CADASTRADO «':^40} {RESET}")
                divideLine()
        else:
            divideLine()
            print(f"{RED} {'» ESTE CPF NÃO É VÁLIDO! «':^40} {RESET}")
            divideLine()


    divideLine()
    print("\n" *5)
    divideLine()
    print(f"{GREEN} {' ► USUÁRIO CADASTRADO COM SUCESSO! ◄':^40} {RESET}")
    listUsers.append(user_registrer)
    


# --------------Função-de-Login-----------------
def Login(User):
    divideLine()
    print(f"{CYAN}• DIGITE SEU CPF: {RESET}")
    loginCpf = int(input(f"{GREEN}→ {RESET}"))
    divideLine()
    print(f"{CYAN}• DIGITE SEU E-MAIL: {RESET}")
    loginEmail = str(input(f"{GREEN}→ {RESET}"))
    divideLine()
    print(f"{CYAN}• DIGITE SUA SENHA: {RESET}")
    loginPassword = str(input(f"{GREEN}→ {RESET}"))
    for l in listUsers:
        if l.cpf == loginCpf and l.email == loginEmail:
            if l.password == loginPassword:
                divideLine()
                print("\n" *5)
                divideLine()
                print(f"{GREEN} {'► LOGIN EFETUADO COM SUCESSO! ◄':^40} {RESET}")
                User = l.name 
                break

    else:
        divideLine()
        print("\n" *5)
        divideLine()
        print(f"{RED} {'» USUÁRIO NÃO CADASTRADO! «':^40} {RESET}")
    return User


# -------------Função-do-Menu-dos-Produtos----------------
def menuProducts(totalPurchase, Balance):

    if Balance <= 0:
        print(f"{RED} {'► SALDO INSUFICIENTE, REALIZE O PAGAMENTO PARA LIBERAR MAIS CRÉDITO ◄':^40} {RESET}")
        totalPurchase, Balance = shoppingCart(totalPurchase, Balance)

    else:


        print(f"{PURPLE} {' → ELETRÔNICOS (0)':^40} {RESET}")
        divideLine()

        print(f"{PURPLE} {' → ELETRODOMÉSTICOS (1)':^40} {RESET}")
        divideLine()

        print(f"{PURPLE} {' → MÓVEIS (2)':^40} {RESET}") 
        divideLine()

        print(f"{PURPLE} {' → LIVROS (3)':^40} {RESET}")
        divideLine()

        print(f"{PURPLE} {' → MENU PRINCIPAL (4)':^40} {RESET}")
        divideLine()

        print(f"{PURPLE} {' → QUAL ABA DESEJA ACESSAR? ':^40} {RESET}")
        products_menu = str(input(f"{GREEN}→ {RESET}"))
        divideLine()


        if products_menu == '0':
            print("\n" *5)
            divideLine()
            print(f"{GREEN} {'► VOCÊ SELECIONOU ELETRÔNICOS ◄':^40} {RESET}")
            divideLine()
            print(f"{PURPLE}{'╔════════════════════════════════════════════════════╦════════════════════════╗'} {RESET}")
            print(f"{PURPLE}║               {CYAN} DESCRIÇÃO DO PRODUTO            {PURPLE}    ║      {GREEN}    PREÇO     {PURPLE}    ║ {RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣ {RESET}")
            print(f"{PURPLE}║{CYAN}1- Samsung Monitor - 21,5 - Preto Brilhante     {PURPLE}    ║      {GREEN}  R$ 986,00     {PURPLE}  ║ {RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣ {RESET}")
            print(f"{PURPLE}║{CYAN}2- Fone de Ouvido Philco - Bluetooth  - Preto    {PURPLE}   ║    {GREEN}    R$ 130,00      {PURPLE} ║{RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣ {RESET}")
            print(f"{PURPLE}║{CYAN}3- Caixa de som gamer Redragon Anvil RGB PRE      {PURPLE}  ║   {GREEN}     R$ 188,00  {PURPLE}     ║{RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣{RESET}")
            print(f"{PURPLE}║{CYAN}4- Tablet M7S Go, Multilaser, Nb317, 16, 7'', Branco{PURPLE}║   {GREEN}     R$ 305,00   {PURPLE}    ║{RESET}")
            print(f"{PURPLE}╚════════════════════════════════════════════════════╩════════════════════════╝{RESET}")
            divideLine()


            while True:
                print(f"{CYAN}• QUAL PRODUTO DESEJA COMPRAR? •{RESET}")
                option1 = str(input(f"{GREEN}→ {RESET}"))
                divideLine()
                if option1 == '1' or option1 == '2' or option1 == '3' or option1 == '4':
                  
                    option1 = int(option1)

                    print(f"{CYAN}• QUAL A QUANTIDADE DESDE PRODUTO? •{RESET}")
                    quantity1 = int(input(f"{GREEN}→ {RESET}"))
                    divideLine()
                    product = functionProduct()
                    product.description = listElectronic[option1 - 1].description
                    product.price = listElectronic[option1 - 1].price
                    product.quantity = quantity1


                    balanceChecker = 0
                    balanceChecker += product.price*product.quantity

                        

                    if balanceChecker <= Balance:


                        totalPurchase += product.price*product.quantity
                        Balance = Balance - product.price*product.quantity

                    
                        listShoppingCart.append(product)

                        print("\n" *5)
                        divideLine()
                        print(f"{GREEN}» SEU PRODUTO FOI ADICIONADO AO CARRINHO! « {RESET}")    

                        return totalPurchase, Balance   

                    else:
                        print("\n" *5)
                        divideLine()
                        print(f"{RED} {'► SALDO INSUFICIENTE ◄':^40} {RESET}")
                        return totalPurchase, Balance 
                
                else:
                    print(f"{RED} {'» ESTE PRODUTO NÃO EXISTE «':^40} {RESET}")
                    divideLine()
                    return totalPurchase, Balance 
                
                


        elif products_menu == '1':
            print("\n" *5)
            divideLine()
            print(f"{GREEN}{'► VOCÊ SELECIONOU ELETRODOMÉSTICOS ◄':^40} {RESET}")
            divideLine()
            print(f"{PURPLE}╔════════════════════════════════════════════════════╦════════════════════════╗{RESET}")
            print(f"{PURPLE}║    {CYAN}            DESCRIÇÃO DO PRODUTO       {PURPLE}         ║      {GREEN}    PREÇO  {PURPLE}       ║{RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣{RESET}")
            print(f"{PURPLE}║{CYAN}1- Freezer portátil de carro 4L                {PURPLE}     ║    {GREEN}    R$ 408,00  {PURPLE}     ║{RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣{RESET}")
            print(f"{PURPLE}║{CYAN}2- Forno Elétrico De Embutir 46L            {PURPLE}        ║   {GREEN}     R$ 880,00  {PURPLE}     ║{RESET}")    
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣{RESET}")
            print(f"{PURPLE}║{CYAN}3- Fogão Star 4 Bocas Branco - Bivolt - Itatiaia  {PURPLE}  ║    {GREEN}    R$ 519,00   {PURPLE}    ║{RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣{RESET}")
            print(f"{PURPLE}║{CYAN}4- Micro-Ondas - Philco - 20 Litros - 220V    {PURPLE}      ║   {GREEN}     R$ 469,00   {PURPLE}    ║{RESET}")
            print(f"{PURPLE}╚════════════════════════════════════════════════════╩════════════════════════╝{RESET}")
            divideLine()


            while True:
                print(f"{CYAN}• QUAL PRODUTO DESEJA COMPRAR? •{RESET}")
                option1 = str(input(f"{GREEN}→ {RESET}"))
                divideLine()
                if option1 == '1' or option1 == '2' or option1 == '3' or option1 == '4':
                  
                    option1 = int(option1)

                    print(f"{CYAN}• QUAL A QUANTIDADE DESDE PRODUTO? •{RESET}")
                    quantity1 = int(input(f"{GREEN}→ {RESET}"))
                    divideLine()
                    product = functionProduct()
                    product.description = listAppliance[option1 - 1].description
                    product.price = listAppliance[option1 - 1].price
                    product.quantity = quantity1


                    balanceChecker = 0
                    balanceChecker += product.price*product.quantity

                        

                    if balanceChecker <= Balance:


                        totalPurchase += product.price*product.quantity
                        Balance = Balance - product.price*product.quantity

                    
                        listShoppingCart.append(product)

                        print("\n" *5)
                        divideLine()
                        print(f"{GREEN}» SEU PRODUTO FOI ADICIONADO AO CARRINHO! « {RESET}")    

                        return totalPurchase, Balance   

                    else:
                        print("\n" *5)
                        divideLine()
                        print(f"{RED} {'► SALDO INSUFICIENTE ◄':^40} {RESET}")
                        return totalPurchase, Balance 
                
                else:
                    print(f"{RED} {'» ESTE PRODUTO NÃO EXISTE «':^40} {RESET}")
                    divideLine()
                    return totalPurchase, Balance 


        elif products_menu == '2':
            print("\n" *5)
            divideLine()
            print(f"{GREEN} {'► VOCÊ SELECIONOU MÓVEIS ◄':^40} {RESET}")
            divideLine()
            print(f"{PURPLE}╔════════════════════════════════════════════════════╦════════════════════════╗{RESET}")
            print(f"{PURPLE}║          {CYAN}      DESCRIÇÃO DO PRODUTO          {PURPLE}      ║    {GREEN}      PREÇO  {PURPLE}       ║{RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣{RESET}")
            print(f"{PURPLE}║{CYAN}1- Cama Box Conjugado Casal - Ortobom         {PURPLE}      ║   {GREEN}     R$ 389,00    {PURPLE}   ║{RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣{RESET}")
            print(f"{PURPLE}║{CYAN}2- Guarda Roupa Casal Espelho 6 Portas 2 Gavetas    {PURPLE}║   {GREEN}     R$ 485,00   {PURPLE}    ║{RESET}")
            print(f"{PURPLE}║       {CYAN}           Real Atualle             {PURPLE}         ║                        ║{RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣{RESET}")
            print(f"{PURPLE}║{CYAN}3- Sofá 3 Lugares Retrátil - Lubeck Plush Suede  {PURPLE}   ║     {GREEN}   R$ 840,00   {PURPLE}    ║{RESET}")         
            print(f"{PURPLE}║          {CYAN}           Grafite          {PURPLE}              ║                        ║{RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣{RESET}")
            print(f"{PURPLE}║{CYAN}4- Estante Home para TV até 52 Polegadas      {PURPLE}      ║     {GREEN}   R$ 500,00   {PURPLE}    ║{RESET}")         
            print(f"{PURPLE}║   {CYAN}          2 Portas - Branca      {PURPLE}                ║                        ║{RESET}")    
            print(f"{PURPLE}╚════════════════════════════════════════════════════╩════════════════════════╝{RESET}")
            divideLine()


            while True:
                print(f"{CYAN}• QUAL PRODUTO DESEJA COMPRAR? •{RESET}")
                option1 = str(input(f"{GREEN}→ {RESET}"))
                divideLine()
                if option1 == '1' or option1 == '2' or option1 == '3' or option1 == '4':
                  
                    option1 = int(option1)

                    print(f"{CYAN}• QUAL A QUANTIDADE DESDE PRODUTO? •{RESET}")
                    quantity1 = int(input(f"{GREEN}→ {RESET}"))
                    divideLine()
                    product = functionProduct()
                    product.description = listFurniture[option1 - 1].description
                    product.price = listFurniture[option1 - 1].price
                    product.quantity = quantity1


                    balanceChecker = 0
                    balanceChecker += product.price*product.quantity

                        

                    if balanceChecker <= Balance:


                        totalPurchase += product.price*product.quantity
                        Balance = Balance - product.price*product.quantity

                    
                        listShoppingCart.append(product)

                        print("\n" *5)
                        divideLine()
                        print(f"{GREEN}» SEU PRODUTO FOI ADICIONADO AO CARRINHO! « {RESET}")    

                        return totalPurchase, Balance   

                    else:
                        print("\n" *5)
                        divideLine()
                        print(f"{RED} {'► SALDO INSUFICIENTE ◄':^40} {RESET}")
                        return totalPurchase, Balance 
                
                else:
                    print(f"{RED} {'» ESTE PRODUTO NÃO EXISTE «':^40} {RESET}")
                    divideLine()
                    return totalPurchase, Balance 




        elif products_menu == '3':
            print("\n" *5)
            divideLine()
            print(f"{GREEN}{'► VOCÊ SELECIONOU LIVROS ◄':^40}{RESET}")
            divideLine()
            print(f"{PURPLE}╔════════════════════════════════════════════════════╦════════════════════════╗{RESET}")
            print(f"{PURPLE}║   {CYAN}             DESCRIÇÃO DO PRODUTO    {PURPLE}            ║    {GREEN}      PREÇO    {PURPLE}     ║{RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣{RESET}")
            print(f"{PURPLE}║{CYAN}1- Coleção Harry Potter - 7 Volumes (português)  {PURPLE}   ║     {GREEN}   R$ 135,00    {PURPLE}   ║{RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣{RESET}")
            print(f"{PURPLE}║{CYAN}2- Box Percy Jackson e os olimpianos         {PURPLE}       ║  {GREEN}      R$ 150,00   {PURPLE}    ║{RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣{RESET}")
            print(f"{PURPLE}║{CYAN}3- Box Os Instrumentos Mortais                {PURPLE}      ║    {GREEN}    R$ 160,00     {PURPLE}  ║{RESET}")
            print(f"{PURPLE}╠════════════════════════════════════════════════════╬════════════════════════╣{RESET}")
            print(f"{PURPLE}║{CYAN}4- Pai rico, pai pobre: Edição de 20 anos    {PURPLE}       ║   {GREEN}     R$ 36,00  {PURPLE}      ║{RESET}")
            print(f"{PURPLE}║{CYAN}          atualizada e ampliada              {PURPLE}       ║                        ║{RESET}")
            print(f"{PURPLE}╚════════════════════════════════════════════════════╩════════════════════════╝{RESET}")
            divideLine()


            while True:
                print(f"{CYAN}• QUAL PRODUTO DESEJA COMPRAR? •{RESET}")
                option1 = str(input(f"{GREEN}→ {RESET}"))
                divideLine()
                if option1 == '1' or option1 == '2' or option1 == '3' or option1 == '4':
                  
                    option1 = int(option1)

                    print(f"{CYAN}• QUAL A QUANTIDADE DESDE PRODUTO? •{RESET}")
                    quantity1 = int(input(f"{GREEN}→ {RESET}"))
                    divideLine()
                    product = functionProduct()
                    product.description = listBook[option1 - 1].description
                    product.price = listBook[option1 - 1].price
                    product.quantity = quantity1


                    balanceChecker = 0
                    balanceChecker += product.price*product.quantity

                        

                    if balanceChecker <= Balance:


                        totalPurchase += product.price*product.quantity
                        Balance = Balance - product.price*product.quantity

                    
                        listShoppingCart.append(product)

                        print("\n" *5)
                        divideLine()
                        print(f"{GREEN}» SEU PRODUTO FOI ADICIONADO AO CARRINHO! « {RESET}")    

                        return totalPurchase, Balance   

                    else:
                        print("\n" *5)
                        divideLine()
                        print(f"{RED} {'► SALDO INSUFICIENTE ◄':^40} {RESET}")
                        return totalPurchase, Balance 
                
                else:
                    print("\n" *5)
                    divideLine()
                    print(f"{RED} {'» ESTE PRODUTO NÃO EXISTE «':^40} {RESET}")
                    return totalPurchase, Balance 

        elif products_menu == '4':
            print("\n" *5)
            divideLine()
            print(f"{GREEN} {'► VOCÊ SELECIONOU MENU PRINCIPAL ◄':^40} {RESET}")
            return totalPurchase, Balance

        else:
            print("\n" *5)
            divideLine()
            print(f"{RED} {'» OPÇÃO INVÁLIDA «':^40} {RESET}")
            return totalPurchase, Balance


#---Função-do-carrinho--------
def shoppingCart(totalPurchase, Balance):
    divideLine()
    cod = 1
  
    print(f"{PURPLE}╔═════╦══════════════════════════════════════════════════════════════╦═════════╦═══════╦═════════════╗{RESET}")
    print(f"{PURPLE}║ {GREY}Cód{PURPLE} ║            {CYAN}         Descrição do Produto             {PURPLE}        ║ {GREEN} Preço {PURPLE} ║ {YELLOW} Qnt {PURPLE} ║ {RED}   Total   {PURPLE} ║{RESET}")
    for product in listShoppingCart:
        print(f"{PURPLE}╠═════╬══════════════════════════════════════════════════════════════╬═════════╬═══════╬═════════════╣{RESET}")
        print(f"{PURPLE}║{GREY} {cod} {PURPLE}  ║{CYAN} {product.description:^60} {PURPLE}║{GREEN} {product.price:^6} {PURPLE} ║{YELLOW} {product.quantity:^4} {PURPLE} ║ {RED} R$ {product.price * product.quantity:^7} {PURPLE}║{RESET}  ")
        cod +=1
    print(f"{PURPLE}╠═════╩══════════════════════════════════════════════════════════════╩═════════╩═══════╩═════════════╣{RESET}")
    print(f"{PURPLE}║                                                                            {GREEN}     TOTAL: {totalPurchase:^7}  {PURPLE}   ║{RESET}") 
    print(f"{PURPLE}╚════════════════════════════════════════════════════════════════════════════════════════════════════╝{RESET}") 


    
    
    divideLine()
    print(f"{PURPLE}{' → PAGAR CONTA (0)':^40} {RESET}")
    divideLine()
    print(f"{PURPLE}{' → REMOVER ITENS (1)':^40}{RESET}")
    divideLine()
    print(f"{PURPLE}{' → VOLTAR AO MENU (2)':^40}{RESET}")
    choice_cart = str(input(f"{GREEN}→ {RESET}"))
    divideLine()
        
    if choice_cart == '0':
        print("\n" *5)
        divideLine()
        print(f"{GREEN}{'► VOCÊ SELECIONOU PAGAR ◄':^40}{RESET}")
        divideLine()
        print(f"{PURPLE}{'→ TOTAL À VISTA (0)':^40}{RESET}")
        divideLine()
        print(f"{PURPLE}{'→ VOLTAR AO MENU (1)':^40}{RESET}")
        divideLine()
            
        choice_payment = str(input(f"{GREEN}→ {RESET}"))
        divideLine()
        
        if choice_payment == '0':
            print("\n" *5)
            divideLine()
            print(f"{GREEN}{'► VOCÊ SELECIONOU PAGAMENTO TOTAL À VISTA ◄':^40}{RESET}")
            divideLine()
            print(f"{GREEN}{' ► PAGAMENTO EFETUADO COM SUCESSO ◄':^40}{RESET}")
            listShoppingCart.clear()
            totalPurchase -= totalPurchase
            Balance = 1000

            return totalPurchase, Balance
            
        elif choice_payment == '1':
            print("\n" *5)
            divideLine()
            print(f"{GREEN}{'► VOCÊ SELECIONOU VOLTAR AO MENU ◄':^40}{RESET}")
            return totalPurchase, Balance

        else:
            print("\n" *5)
            divideLine()
            print(f"{RED} {'» OPÇÃO INVÁLIDA «':^40} {RESET}")
            return totalPurchase, Balance 
        
        
    elif choice_cart == '1':
        print("\n" *5)
        divideLine()
        print(f"{GREEN}{'► VOCÊ SELECIONOU REMOVER ITENS ◄':^40}{RESET   }")
        listShoppingCart.clear()
        totalPurchase = 0.0
        Balance = 1000.00
        divideLine()
        print(f"{GREEN}{'VOCÊ REMOVEU TODOS OS ITENS':^40}{RESET}")
        return totalPurchase, Balance
                

            
        
        
    elif choice_cart == '2':
        print("\n" *5)
        divideLine()
        print(f"{GREEN}{'► VOCÊ SELECIONOU VOLTAR AO MENU ◄':^40}{RESET}")
        return totalPurchase, Balance

    else:
        print("\n" *5)
        divideLine()
        print(f"{RED} {'» OPÇÃO INVÁLIDA «':^40} {RESET}")
        return totalPurchase, Balance


#------------------Função-dos-Creditos------------------
def showCredits():
    print(f"{CYAN}• Desenvolvedores:{RESET}")
    print(f"{GREEN}» Ana Julia Perin Tecchio e Pedro Henrique Klein{RESET}")
    print(f"{GREEN}» Alunos de Ciência da Computação 2021/1{RESET}")
    print(f"{GREEN}» Universidade Federal da Fronteira Sul - Campus Chapecó{RESET}")
    divideLine()
    print(f"{CYAN}• Professores:{RESET}")
    print(f"{GREEN}» Andrei de Almeida Sampaio Braga e Guilherme Dal Bianco «{RESET}")

    divideLine()
    print(f"{CYAN}{'► VOLTAR AO MENU (0) ◄':^40}{RESET}")
    divideLine()
    choice_credits = str(input(f"{GREEN}→ {RESET}"))
    divideLine()
    if choice_credits == '0':
        print("\n" *5)
        divideLine()
        print(f"{GREEN}{'► VOCÊ SELECIONOU VOLTAR AO MENU ◄':^40}{RESET}")

    else:
        print("\n" *5)
        divideLine()
        print(f"{RED} {'» OPÇÃO INVÁLIDA «':^40} {RESET}")
        divideLine()
        showCredits()


#---Função-que-Verifica-as-Abas-Escolhidas------
def Menu():
    User = ''
    totalPurchase = 0.0
    Balance = 1000.00


    if Balance <= 0:
        print(f"{GREEN} {'► SALDO INSUFICIENTE ◄':^40} {RESET}")


    while True:
        Interface(User, Balance)
        print(f"{PURPLE} {' → QUAL ABA DESEJA ACESSAR? ':^40} {RESET}")
        menu_choice = str(input("→ "))
        divideLine()
        if menu_choice == '0':
            print("\n" *5)
            divideLine()
            print(f"{GREEN} {'► VOCÊ SELECIONOU CADASTRE-SE ◄':^40} {RESET}")
            Inscribe()
        

        elif menu_choice == '1':
            print("\n" *5)
            divideLine()
            print(f"{GREEN} {'► VOCÊ SELECIONOU ENTRAR NA CONTA ◄':^40} {RESET}")
            User = Login(User)
            


        elif menu_choice == '2':
            print("\n" *5)
            if Balance <= 0:
                print(f"{RED} {'► SALDO INSUFICIENTE, REALIZE O PAGAMENTO PARA LIBERAR MAIS CRÉDITO ◄':^40} {RESET}")
                totalPurchase, Balance = shoppingCart(totalPurchase, Balance)

            else:
                if User != '':
                    print("\n" *5)
                    divideLine()
                    print(f"{GREEN} {'► VOCÊ SELECIONOU COMPRAR PRODUTOS ◄':^40} {RESET}")
                    divideLine()
                    totalPurchase, Balance = menuProducts(totalPurchase, Balance)
                else:
                    print("\n" *5)
                    divideLine()
                    print(f"{RED} {'» USUÁRIO NÃO ESTÁ LOGADO! «':^40} {RESET}")


        elif menu_choice == '3':
            print("\n" *5)
            if User != '':
                divideLine()
                print(f"{GREEN} {'► VOCÊ SELECIONOU CARRINHO ◄':^40} {RESET}")
                totalPurchase, Balance = shoppingCart(totalPurchase, Balance)
            else:
                print("\n" *5)
                divideLine()
                print(f"{RED} {'» USUÁRIO NÃO ESTÁ LOGADO! «':^40} {RESET}")
                #User = Login(User)
            


        elif menu_choice == '4':
            print("\n" *5)
            divideLine()
            print(f"{GREEN} {'► VOCÊ SELECIONOU CRÉDITOS ◄':^40} {RESET}")
            divideLine()
            showCredits()

        elif menu_choice == '5':
            print("\n" *5)
            divideLine()
            print(f"{GREEN} {'► VOCÊ SAIU DO PROGRAMA ◄':^40} {RESET}")
            divideLine()
            break

        else:
            print("\n" *5)
            divideLine()
            print(f"{RED} {'► OPÇÃO INVÁLIDA ◄':^40} {RESET}")

#------------------Parte-Principal-do-Programa------------------
#--Inicia-as--Listas-dos-Produtos-----
Eletronics()
Appliances()
Furniture()
Books()
#-------Inicia-o-Menu-----------
Menu()