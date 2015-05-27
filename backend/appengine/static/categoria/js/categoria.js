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
					console.log(erros.nome);
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
			// $scope.ajaxFlag = false;
			$scope.deletar = function(){
				// $scope.ajaxFlag = true;
				CategoriaApi.deletar($scope.category.id).success(function(){
					console.log('deletou');
					$scope.deletarConcluido({'categoria': $scope.category});
				}).error(function(){
					console.log('deu ruim');
				});
			}
		
		}
	};

});



