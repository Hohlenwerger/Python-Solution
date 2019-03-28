# Author: HohlenwergerMB
# Git: https://github.com/Hohlenwerger/Python-Solution

Após receber o projeto no dia 15/03, comecei a desenhar o modelo utilizando JavaScript, linguagem  em que eu já tinha experiêcia devido ao meu último estágio como Web Developer. Entretanto, me ocorreu que eu deveria tentar fazer algo em Python, tendo em vista que é uma linguagem que tem ganhado cada vez mais destaque. Comecei a estudar a mesma no dia 16/03 e o projeto aqui apresentado representa parte do que eu pude aprender em 10 dias.

Explicação de Escopo do Projeto:
	Pasta "dbFix":
		Pasta com os 3 Métodos de Correção: dbFixNames, dbFixPrices e dbFixQuantities.

		Existe um quarto arquivo, "jsonUtils", com métodos de leitura, escrita e impressão de JSON, que é importado pelos demais. Tais métodos poderiam ser implementados junto aos arquivos, porém acredito que ficaria repetitivo e pouco dinamico em uma futura necessidade de alteração.

		Os nomes dos arquivos são intuitivos. O dbFixName possui método para consertar os nomes no arquivo JSON, o dbFixPrice, os preços, e o dbFixQuantity, as quantidades.

		Todos os Arquivos foram indentados usando TAB, o que eu notei que era relevante já que espaços e tabs são diferentes em Python.

		Todos os Arquivos possuem comentários para agilizar o entendimento.

		Dentro desta Pasta existe outra denominada "Results of Methods" que possui arquivos JSON com o resultado de cada método de correção. Um destes contém os resultados de todos os métodos. Aqui também, os nomes são intuitivos:
			resultOf_allMethods    -> Após passar por todos os métodos 
			resultOf_FixNames 	   -> Após passar pelo dbFixNames.py
			resultOf_FixPrices 	   -> Após passar pelo dbFixPrices.py
			resultOf_FixQuantities -> Após passar pelo dbFixQuantities.py

Pasta "dbValidate":
	Pasta com os 2 Métodos de Validação: printOrdained, stockValueCalc.

		Da mesma forma que em "dbFix", existe um arquivo chamado "jsonUtils" com métodos de leitura, escrita e impressão de arquivos JSON, que é importado pelos demais arquivos.

		O printOrdained é a validação "a)" requisitada no projeto, que imprime uma lista com todos os nomes dos produtos, ordenados primeiro por categoria, em ordem alfabética, e depois por id, em ordem crescente.

		O stockValueCalc é a validação "b)", também requisitada no projeto, que calcula e imprime o valor total do estoque por categoria, ou seja, a soma do valor de todos os produtos em estoque de cada categoria, considerando a quantidade de cada produto.

		Dentro desta Pasta existe outra denominada "Validated Outputs" que possui arquivos de texto com a saida de cada método de validação.
			outputOf_printOrdained  -> Saida do printOrdained.py
			outputOf_stockValueCalc -> Saida do stockValueCalc.py
