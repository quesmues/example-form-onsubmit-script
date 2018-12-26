# example-form-onsubmit-script
Exemplo de formulário (Form) com Ajax na ação de onsubmit no Flask usando Jinja2.

O problema que tinhamos encontrado era como poderiamos criar forms de forma dinamica dentro de um for-loop, onde cada linha teria um formulário idempendente para edição e criação de comentários.

Encontremos um solução onde passamos o número da interação do for usando o {{loop.index}} e chamando o evento de onsubmit dentro da tag do próprio form:

<form onsubmit="return enviar(event, {{loop.index}})">
  
O loop index faz com que eu consiga coletar qual elemento é de cada linha, para passar através do Ajax:

codigoErro: $("input[name='codigoErro']")[arg-1].value, //arg é o loop.index, como os elementos dentro do array começa em 0
sugestao: $("input[name='sugestao']")[arg-1].value,     //apenas adicionei o -1, também poderiamos ter feito o loop.index 
file: $("input[name='file']")[arg-1].value              //começar em 0
  
Apenas isto não foi o suficiente pois precisariamos de que funcionasse de forma idenpendente ao carregamento da página, por isto utilizamos Ajax, mas ai surgiu outro problema, como fazer a página não recarregar após o envio do formulário e o segredo veio atráves de 2 itens.

//Função Ajax para multiplos forms com jinja2
    	enviar = function(e, arg) {
    	console.log(arg)
    	console.log(e)
        $.ajax({
            data: {
                codigoErro: $("input[name='codigoErro']")[arg-1].value,
                sugestao: $("input[name='sugestao']")[arg-1].value,
                file: $("input[name='file']")[arg-1].value
            },
            type: 'POST',
            url: '/api/'
        });
        e.preventDefault();               //Um método do evento onsubmit, normalmente utilizado junto com o ajax em um form
        return false;                     //Para evitar que o formulário recarregue a página (ou faça um post indesejado)
    	};
      
 E o 
