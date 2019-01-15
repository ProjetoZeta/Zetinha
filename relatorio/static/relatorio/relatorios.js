$(document).ready(function () {

	$( "#id_projetos_select" ).change(function(){

		var projetopk = this.value

		if (projetopk != ""){

			$.ajax({
			  url: `/relatorio/projeto/${ projetopk }/participantes_select`,
			  type: "get", //send it through get method
			  success: function(response) {

				document.getElementById("container-atividades").innerHTML = response + '<div class="help-block"></div>'

			  },
			  error: function(xhr) {
				alert('AJAX falhou')
			  }
			});

		} else {

			document.getElementById("container-atividades").innerHTML = '<select name="atividade" class="form-control" id="id_atividade_select" required="" disabled=""><option value="" ></option></select><div class="help-block"></div>'

		}
	});


	var todos_cb = document.getElementById("todos_id")
	todos_cb.addEventListener('click', function(){
		$(".cbox").prop('checked', todos_cb.checked);
	})

})

	