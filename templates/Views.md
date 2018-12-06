# O que é

As Class-based views MainView e RelatedFormView, são soluções que abstraem vários mecanismos utilizados em views. O Django possui Class-based views built-in e estão descritas em sua documentação. Neste projeto foi utilizado um implementação personalizada.

# Pra que serve



# Como usar

A classe MainView deve ser utilizada como classe abstrata que será estendida pelas views do projeto.
A view que extender MainView deve definir alguns atributos.

* **form**: recebe uma classe do tipo ModelForm (obrigatório)
* **formalias**: o nome da variável que referencia o formulário no template. Por padrão este valor recebe 'form{}'.format([nome da model em minúsculo])
* **setalias**: o nome da variável que referencia a lista de registros da model. Por padrão este valor recebe 'set{}'.format([nome da model em minúsculo])
* **url_triggers**: recebe uma lista de strings que representem expressões regulares. Estas expressões servem como gatilho para a execução da view, baseada na url que estiver ativa no momento. Esta opção só faz sentido quando a view for filha de outra view.
* **children**: Esse atributo deve receber uma lista de classes que estendam MainView. Mais detalhes da seção das views filhas
* **related**: Esse atributo deve receber uma lista de classes que estendam RelatedFormView. Mais detalhes na seção do RelatedFormView
* **template_name**: O caminho para o template com a qual a view será renderizada
* **success_redirect**: recebe o nome de uma url para a qual a view será redicionada em caso de sucesso após um POST de criação ou edição. 
* **delete_redirect**: recebe o nome de uma url para a qual a view será redicionada em caso de sucesso após um POST/GET de deleção.

A MainView provê um mecanismo de hierarquia entre as views. 

# Views filhas

# Views relacionadas (paralelas)

# O que fica disponível nos templates

