  


   (function() {
      angular.module("hotelreservation.angapp",[]).
      controller("HotelReservation", ["$scope",HotelReservation])
      .controller("CustomersController",["$scope",CustomersController]) ;


    function HotelReservation($scope) {

         $scope.hotels = [
         {hotel_name : "Retz Carlton", hotel_city : "Casa"},
         {hotel_name : "Sheraton", hotel_city:"Rabat"},
         ];
         $scope.add_new_hotel = function(new_hotel,hotels) {

            var hotel = { hotel_name : new_hotel, hotel_city :"Any city"} ;
            hotels.push(hotel) ;

         } ;
      }

    
      function CustomersController($scope) {

        $scope.customers =[

            { name : " medo", phone_number : " 9883452"},
            { name : " maria", phone_number : " 32168888"},

        ] ;


        $scope.add_new_customer = function(new_customer,customers) {

            var customer = { name : new_customer, phone_number :"Any phone"} ;
            customers.push(customer) ;

         } ;

      }

    


   })();

