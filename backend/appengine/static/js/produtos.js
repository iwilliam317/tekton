$(document).ready(function(){

	var $nomeInput = $('#nomeInput');
	var $descricaoInput = $('#descricaoInput');
	var $precoInput = $('#precoInput');
	var $categoriaSelect = $('#categoriaSelect');
	var $novidadeSelect = $('#novidadeSelect');
	var $carregandoImg = $('#carregandoImg');
	$carregandoImg.hide();
	var $btnSalvar = $('#salvar');
	var $btnFechar = $('#fechar');

	function obterValoresdeProdutos(){
		return {'nome' : $nomeInput.val() , 'descricao' : $descricaoInput.val(), 'preco': $precoInput.val() , 'categoria' :  $categoriaSelect.val(), 'novidade' : $novidadeSelect.val()}
	}
	
	function limparValores(){
		$('input[type="text"]').val('');
		$categoriaSelect.val("");
		$novidadeSelect.val("");
	}

	$btnSalvar.click(function(){
		$('.has-error').removeClass('has-error');
		$('.help-block').empty();
		$btnSalvar.attr('disabled' , 'disabled');

		$carregandoImg.fadeIn('fast');
		$.post('/produtos/admin/rest/salvar', obterValoresdeProdutos(),
		function(produto)
		{
			limparValores();
			$btnFechar.click();
			window.location.reload();	
		}).error(

		function(erros){
			for(campos in erros.responseJSON)
			{
				$('#'+campos+'Div').addClass('has-error');
				$('#'+campos+'Span').text(erros.responseJSON[campos]);
			}
		}).always(function(){
			$btnSalvar.removeAttr('disabled','disabled');
			$carregandoImg.hide();
		});
	});
});
