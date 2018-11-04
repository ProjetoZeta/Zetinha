
        $(document).ready(function () {
            $('#modal-file').modal({% if formf.errors %}'show'{% else %}''{% endif %});
        });

        $(document).ready(function () {
            $('#modal-emprestimo').modal({% if forme.errors %}'show'{% else %}''{% endif %});
        });

        $(document).ready(function () {

            $("#id_cpf").mask('000.000.000-00', {reverse: true});
            $("#id_dt_nascimento").mask('00/00/0000', {reverse: true});
            $("#id_inicio_vigencia").mask('00/00/0000', {reverse: true});
            $("#id_termino_vigencia").mask('00/00/0000', {reverse: true});
            $('#id_telefone').mask('(00) 0000-0000');
            $('#id_celular').mask('(00) 0 0000-0000');
            $('#id_cep').mask('00.000-000');
            $('#id_valor_mensal')
            
     
            $("#id_periodo_total").on("click", function (event) {
                event.preventDefault();
                var inicio = $('#id_inicio_vigencia').val()
                var fim = $("#id_termino_vigencia").val()
                var dt_inicio = new Date(inicio.toDate('dd/mm/yyyy'));
                var dt_fim = new Date(fim.toDate('dd/mm/yyyy'));
                var timeDiff = Math.abs(dt_fim.getTime() - dt_inicio.getTime());
                var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24)); 
                var months = Math.trunc(diffDays / 30); 
                $("#id_periodo_total").val(months)

            });

            


        });


    $(document).ready(function() {

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
     });