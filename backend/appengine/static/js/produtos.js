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
			$novidadeSelect.val('');
		}

		$.get('/produtos/admin/rest/listar').success(function(produtos){
			$.each(produtos,function(index, p){
				adicionarProduto(p);
			})
			
		});
			
		function adicionarProduto (produto) {
			var msg = '<tr id="tr-produto_'+produto.id+'"><td>'+produto.id+'</td><td>'+produto.nome+'</td><td>'+produto.categoria+'</td><td>'+produto.descricao+'</td><td>'+produto.preco+'</td><td>'+(produto.novidade == "1" ? 'Sim' : 'Não')+'</td><td><a href="/produtos/admin/editar/'+produto.id+'" class="btn btn-warning glyphicon glyphicon-pencil"></a></td><td><button id="btn-deletar_'+produto.id+'" class="btn btn-danger"><i class="glyphicon glyphicon-trash"></i></button></td></tr>';
			$listaProdutos.show();
			$listaProdutos.append(msg);

			$('#btn-deletar_'+produto.id).click(function(){
				if (confirm("Deseja apagar esse registro? "))
				{
					var resp = $.post('/produtos/admin/rest/deletar' , {produto_id : produto.id});

					resp.success(function(){
					$('#tr-produto_'+produto.id).remove()
				});
				}
				
			});
		}



		$btnSalvar.click(function(){
			$('.has-error').removeClass('has-error');
			$('.help-block').empty();
			$btnSalvar.attr('disabled' , 'disabled');

			$carregandoImg.fadeIn('fast');
			var resp = $.post('/produtos/admin/rest/salvar', obterValoresdeProdutos());

			resp.success(function(produto){

				limparValores();
				$btnFechar.click();
				adicionarProduto(produto);	
			})
			
			resp.error(function(erros){
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
