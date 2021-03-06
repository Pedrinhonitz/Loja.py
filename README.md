# **Simular uma Loja com Python**


## **Tarefas**

O objetivo de seu programa é possibilitar que clientes façam o seu cadastro, insiram itens em um carrinho de compras, visualizem o total de gastos e a lista de itens adicionados ao carrinho, consultar cliente, bem com possam realizar o pagamento.

O objetivo de seu programa é possibilitar que clientes façam o seu cadastro, **insiram seus itens em um carrinho de compras**, além de **mostrar o total de gastos** e a **lista de itens adquiridos**.

### **1 - Cadastrar novos clientes**

O cliente poderá criar um novo usuário informando o seu email e a sua senha (6 dígitos). Além disso, o cliente deve informar o seu nome e o seu CPF. Deve-se verificar se o usuário já existe no sistema e se o CPF já está cadastrado.

Sobre os dados cadastrais, deve ser observado o seguinte:
  * Email do cliente: verificar se o email é válido. Ou seja, deve-se verificar se contém o caracter '@' na string. 
  * Senha do cliente: necessária para realizar qualquer operação no caixa. Deve ser constituída de 6 dígitos.
  * Nome do cliente: o nome do titular da conta. É constituído por um conjunto de caracteres alfabéticos. Ex: João, Maria e Francisco.
  * CPF do cliente: deve ser verificado se o número de CPF é válido.  Mais informações podem ser encontradas no site http://www.macoratti.net/alg_cpf.htm

### **2 - Compras**

Cada usuário pode realizar compras até que seu limite de crédito seja atingido. O limite de crédito será de R$1.000,00 para cada cliente. Quando o limite estourar, deve ser mostrada uma mensagem para o usuário informando que ele não pode realizar a compra. 

O sistema terá um cadastro fixo dos itens que poderão ser comprados. Por exemplo:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1\. Pasta de dente - R\$ 5,00<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2\. Arroz 5kg&emsp;&emsp;&nbsp;&nbsp; - R\$ 10,00<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3\. Feijão 1kg&emsp;&emsp;&nbsp; - R\$ 4,00<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;20\. Açúcar 1kg&emsp;&nbsp; - R\$ 2,00

Assim o usuário irá escolher o item "1" ou "2" ... "20" para realizar as compras dos produtos.

### **3 - Mostrar carrinho**

Cada usuário poderá ter acesso ao seu carrinho de compras para verificar seu total de gastos.
A função deverá disponibilizar o total do carrinho e a opção para listar todos os itens. 

### **4 - Pagar conta**

O usuário poderá fazer o pagamento "virtual" de sua fatura para possibilitar a liberação de mais crédito.
