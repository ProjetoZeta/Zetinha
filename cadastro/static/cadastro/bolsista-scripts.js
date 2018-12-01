
        $(document).ready(function () {
                 
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