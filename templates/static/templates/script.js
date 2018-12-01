$(document).ready(function () {

    $(".date-input").mask("00/00/0000", {placeholder: "__/__/____"});

    $(".cpf-input").mask("000.000.000-00", {placeholder: "___.___.___-__"});

    $(".cnpj-input").mask("00.000.000/0000-00", {placeholder: "__.___.___/____-__"});

    $(".cep-input").mask("00000-000", {placeholder: "_____-___"});

    $(".telefone-input").mask("(00) 0000-0000", {placeholder: "(__) ____-____"});

    $(".celular-input").mask("(00) 0 0000-0000", {placeholder: "(__) 9 ____-____"});

})

