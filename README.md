# DHT
Gerenciamento de Dados Distribuídos - Tabela Hash Distribuída (DHT)

Estrutura :

Uso de lista para armazenar os nodos ordenados da DHT e Operacoes.

DHT  = lista de objetos

Nodos - Nodos sao objetos com atributos - ID(inteiro),ATIVO(0 ou 1),sus(Valor do Sucessor),Tabela({dicionario}).



Desenvolvimento pensamento:

Dificuldades

Lookup nao esta funcionando.
A problemas em atualizar a tabela de alguns nodos da DHT



1. Leitura das Entradas -

	1.1 - Le o arquivo do Stdin uma lista que recebe as entradas, e faz um split separando 
	pelos 4 campos de possivei operacoes para E,S,L,I, cada linha de entrada se torna uma Indice da lista com uma sub-lista operacoes.

2.Execucao das entradas.

	2.1 - Loop que le cada operacao da lista e identifica pelo segundo campo que pode ser E,S,L,I
	      
	      Se operacao  = E e for primeira entrada.
			Adiciona um nodo na lista de Nodos, ordenado pela sua ID que foi recebida do valor de entrada.
			
	      senao: Caso ja exista uma entrada
			Adiciona um nodo na lista de Nodos, ordenado pela sua ID que foi recebida do valor de entrada.
			e tambem calcule a tabela com o sucessor baseado na formula do log_2(tamanho_dht) e a formula para cada ID QUE ENTRA NA LISTA.
	
	2.2 - Operacao de S Saida basicamente pega o nodo copia a chaves e seus valores e insere no sucessor e depois fazer  na tabela de rotas e passar para a tabela do nodo sucessor e ainda
	      atualiza a tabela de rotas novamente para que nao exista discrepancias.

	2.3 - Operacao de I inserir, insere um chave na tabela do nodo, calcula o sucessor da chave e atribui e cria a rota para o novo elemento atribuido, ou seja
	      quando o novo elemento entrar ele ira calcular a nova rota


	2.3 - operacao de lookup, funcao lookup pega o valor procurado caso ele nao esteja na tabela do nodo ele entao procura o maior nodo mais proximo e retorna como busca
	      e assim para o nova busca imprimindo o L, e caso nao encontre o L e a tabela
