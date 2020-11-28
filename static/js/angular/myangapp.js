  


   (function() {
      angular.module("hotelreservation.angapp",[]).
      controller("HotelReservation", ["$scope","$http", HotelReservation])
      .controller("CustomersController",["$scope",CustomersController]) ;


    function HotelReservation($scope,$http) {

         $scope.hotels = [];

        $http.get("/reservation/hotelsapi")
        .then(function(response) {
            $scope.hotels = response.data;
        }) ;

         $scope.add_new_hotel = function(new_hotel,hotels) {

            var hotel = { 
                hotel_name : new_hotel,
                 hotel_city :"Any city",
                 total_rooms :"230",
                 empty_rooms :"23"
                
                } ;
            $http.post("/reservation/hotelsapi/",hotel)
            .then(function(response) {

            hotels.push(response.data) ;

            
            },
            function() { 
                alert("an error happened while adding new hotel");

            } );


           

         } ;
      }

    
      function CustomersController($scope) {

        $scope.customers =[

            { name : " medo", phone_number : " 9883452"},
            { name : " maria", phone_number : " 32168888"},

        ] ;


        $scope.add_new_customer = function(new_customer,customers) {

            var customer = { name : new_customer, phone_number :"78888444231"} ;
            customers.push(customer) ;

         } ;

      }

    


   })();

