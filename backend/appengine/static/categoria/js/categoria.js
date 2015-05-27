var categoriaModulo = angular.module('categoriaModulo', ['rest']);

categoriaModulo.directive('categoriaform', function(){
	return{
		restrict: 'E',
		replace: true,
		templateUrl: '/static/categoria/html/categoria.html',
		scope: {
			category:'=',
			nomeLabel: '@',
			categoriaPaiLabel: '@',
			salvarConcluido: '&'
		},
		controller: function($scope, CategoriaApi){
			$scope.salvando = false;
			$scope.erros={};

			$scope.salvar = function(){
				$scope.salvando = true;
				CategoriaApi.salvar($scope.category).success(function(category){
					// console.log('saved: ' +category);
					if ($scope.salvarConcluido != undefined)
					{
						$scope.salvarConcluido({'categoria':category});
					}
					
					$scope.salvando = false;
					// $scope.category="";
					$scope.erros={};
					
				}).error(function(erros){
					// console.log(erros.nome);
					$scope.salvando = false;
					$scope.erros = erros;
				});
				
			}
		
		}
	}

});


categoriaModulo.directive('categorialinha', function(){
	return{
		restrict: 'A',
		replace: true,
		templateUrl: '/static/categoria/html/categoria_linha.html',
		scope: {
			category:'=',
			deletarConcluido: '&'
		},
		controller: function($scope, CategoriaApi){
			$scope.erros={};
			$scope.deletando = false;
			$scope.categoriaEdicao={};
			$scope.editando=false;

			$scope.deletar = function(){
			
			if (confirm('Deseja apagar esse registro'))
			{	
				$scope.deletando = true;
				CategoriaApi.deletar($scope.category.id).success(function(){
					$scope.deletarConcluido({'categoria': $scope.category});
				}).error(function(){
					
				});
			}
				
			}

			$scope.editar=function(){
				$scope.editando=true;
				$scope.categoriaEdicao.id = $scope.category.id;
				$scope.categoriaEdicao.nome = $scope.category.nome;
				$scope.categoriaEdicao.categoria_pai = $scope.category.categoria_pai;
			}

			$scope.cancelar = function(){
				$scope.editando=false;
				$scope.erros={};
			}

			$scope.completarEdicao=function(){
				CategoriaApi.editar($scope.categoriaEdicao).success(function(categoria){
					$scope.category = categoria;
					$scope.editando=false;
					$scope.erros={};
				}).error(function(erros){
					$scope.erros = erros;
				});
			}
		
		}
	};

});



