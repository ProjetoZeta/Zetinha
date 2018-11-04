
$(document).ready(function () {

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

	