var categoriaModulo = angular.module('categoriaModulo', ['rest']);

categoriaModulo.directive('categoriaform', function(){
	return{
		restrict: 'E',
		replace: true,
		templateUrl: '/static/categoria/html/categoria.html',
		scope: {
			category:'=',
			nomeLabel: '@',
			categoriaPaiLabel: '@'
		},
		controller: function($scope, CategoriaApi){
			$scope.salvando = false;
			$scope.erros={};

			$scope.salvar = function(){
				$scope.salvando = true;
				CategoriaApi.salvar($scope.category).success(function(category){
					console.log('saved: ' +category);
					$scope.salvando = false;
					$scope.category="";
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
			category:'='
		},
		controller: function($scope, CategoriaApi){
	
		
		}
	};

});



