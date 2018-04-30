$(document).ready(function () {

    function lock() {
        if ($("#id_tipo_conta").val() == "1") {
            $("#id_banco").val("104").change();

            $('#id_banco option[value=104]').attr('selected','selected');

            //$('#id_banco').attr('disabled', true);

        } else {
             //$('#id_banco').attr('disabled', false);
        }
    }

    $("#id_tipo_conta").change(function () {
        lock();
    });
    
});




