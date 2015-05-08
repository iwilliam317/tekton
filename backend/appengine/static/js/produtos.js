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
	var $listaProdutos = $('#listaProdutos');
	$listaProdutos.hide();

	function obterValoresdeProdutos(){
		return {'nome' : $nomeInput.val() , 'descricao' : $descricaoInput.val(), 'preco': $precoInput.val() , 'categoria' :  $categoriaSelect.val(), 'novidade' : $novidadeSelect.val()}
	}
	
	function limparValores(){
		$('input[type="text"]').val('');
		$('select').val('');
	}

	// $.get('/produtos/admin/rest').success(function(resp){
	// 	console.log(resp);
	// });
	function listarProduto (produto) {
		var msg = '<tr><td>'+produto.responseJSON["id"]+'</td><td>'+produto.responseJSON["nome"]+'</td><td>'+produto.responseJSON["categoria"]+'</td><td>'+produto.responseJSON["descricao"]+'</td><td>'+produto.responseJSON["preco"]+'</td><td>'+(produto.responseJSON["novidade"] == "1" ? 'Sim' : 'Não')+'</td></tr>';
		$listaProdutos.show();
		$listaProdutos.append(msg);
	}

	$btnSalvar.click(function(){
		$('.has-error').removeClass('has-error');
		$('.help-block').empty();
		$btnSalvar.attr('disabled' , 'disabled');

		$carregandoImg.fadeIn('fast');
		var produto = $.post('/produtos/admin/rest/salvar', obterValoresdeProdutos());

		produto.success(function(){

			limparValores();
			$btnFechar.click();
			listarProduto(produto);	
		})
		
		produto.error(function(erros){
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
