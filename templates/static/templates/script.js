$(document).ready(function () {

    $(".date-input").mask("00/00/0000", {placeholder: "__/__/____"});

    $(".cpf-input").mask("000.000.000-00", {placeholder: "___.___.___-__"});

    $(".cnpj-input").mask("00.000.000/0000-00", {placeholder: "__.___.___/____-__"});

    $(".cep-input").mask("00000-000", {placeholder: "_____-___"});

    $(".telefone-input").mask("(00) 0000-0000", {placeholder: "(__) ____-____"});

    $(".celular-input").mask("(00) 0 0000-0000", {placeholder: "(__) 9 ____-____"});


    function limpa_formulário_cep() {
             // Limpa valores do formulário de cep.
             $("#id_endereco").val("");
             $("#id_cidade").val("");
         }

         //Quando o campo cep perde o foco.
         $("#id_cep").blur(function() {

             //Nova variável "cep" somente com dígitos.
             var cep = $(this).val().replace(/\D/g, '');

             //Verifica se campo cep possui valor informado.
             if (cep != "") {

                 //Expressão regular para validar o CEP.
                 var validacep = /^[0-9]{8}$/;

                 //Valida o formato do CEP.
                 if(validacep.test(cep)) {

                     //Preenche os campos com "..." enquanto consulta webservice.
                     $("#id_endereco").val("...");
                     $("#id_cidade").val("...");

                     //Consulta o webservice viacep.com.br/
                     $.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {

                         if (!("erro" in dados)) {
                             //Atualiza os campos com os valores da consulta.
                             $("#id_endereco").val(dados.logradouro);
                             $("#id_cidade").val(dados.localidade);
                         } //end if.
                         else {
                             //CEP pesquisado não foi encontrado.
                             limpa_formulário_cep();
                             alert("CEP não encontrado.");
                         }
                     });
                 } //end if.
                 else {
                     //cep é inválido.
                     limpa_formulário_cep();
                     alert("Formato de CEP inválido.");
                 }
             } //end if.
             else {
                 //cep sem valor, limpa formulário.
                 limpa_formulário_cep();
             }
         });





})

