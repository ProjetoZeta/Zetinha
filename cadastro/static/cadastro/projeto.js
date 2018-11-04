
$(document).ready(function () {

	$(".countries a").click(function(e) {
	  e.preventDefault();
	  $("[href='#first']").tab('show');
	  $("[href='#second']").tab('show');
	});

})

	