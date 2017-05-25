var $search = $('section .busca form')

function showHide(tito){
	tito.preventDefault();
	tito.stopPropagation();
	$search.slideToggle();
}

$('nav button').click( showHide )