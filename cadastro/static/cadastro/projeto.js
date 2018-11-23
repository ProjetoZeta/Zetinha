
$(document).ready(function () {

	function bind_atividade_on_change_select_event(){
		$( "#id_atividade_select" ).change(function() {

			var atividade_pk = this.value
			  	
			$.ajax({
			  url: '/cadastro/atividade/' + atividade_pk + '/participantes_select',
			  type: "get", //send it through get method
			  success: function(response) {
			    $( "#container-participantes" ).html(response)
			  },
			  error: function(xhr) {
			  	alert('AJAX falhou')
			  }
			});			

		});
	}

	$( "#id_vinculo_atividade_meta" ).change(function() {
	  	
	  	var meta_pk = this.value

		$.ajax({
		  url: '/cadastro/meta/' + meta_pk + '/atividades_select',
		  type: "get", //send it through get method
		  success: function(response) {
		    $( "#container-atividades" ).html(response)
		    bind_atividade_on_change_select_event()
		  },
		  error: function(xhr) {
		  	alert('AJAX falhou')
		  }
		});

	});

	$(".countries a").click(function(e) {
	  e.preventDefault();
	  $("[href='#first']").tab('show');
	  $("[href='#second']").tab('show');
	});


	// Javascript to enable link to tab
	var url = document.location.toString();
	if (url.match('#')) {
	    $('.nav-tabs a[href="#' + url.split('#')[1] + '"]').tab('show');
	} 

	// Change hash for page-reload
	/*$('.nav-tabs a').on('shown.bs.tab', function (e) {
	    window.location.hash = e.target.hash;
	})*/


	function prepare_detalhes_form() {
		var button_confirm = $('#confirm-button')
		button_confirm.text('Salvar Detalhes')
		button_confirm.click(function(){
			$('#form-detalhes').submit()
		})
	}

	function monitor_tabs(atab){
		var buttons = $('#form-buttons')
		if ($(atab).attr('class') == 'detalhes'){
			prepare_detalhes_form()
			buttons.show()
		} else {
			buttons.hide()
		}
	}

	$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {

	  var target = $(e.target).attr("class") // activated tab
	  
	  monitor_tabs(e.target)

	});

	monitor_tabs($('a[data-toggle="tab"]').parent('li.active').children('a')[0])

})

	