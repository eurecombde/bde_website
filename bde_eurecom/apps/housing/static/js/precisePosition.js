$(document).ready(function() {

    map = null; 
    geocoder = new google.maps.Geocoder();
    latitude_field = $('#id_latitude');
    longitude_field = $('#id_longitude');
    distance_field = $('#id_distance_eurecom'); 
    map_canvas = $('#map_canvas');

    $("#ui-accordion-6-header-0").click(function(){
        initializeMap();
        if (latitude_field.val()!='' && longitude_field.val()!=''){
            var location = new google.maps.LatLng(Number(latitude_field.val()), Number(longitude_field.val()));
            map.setCenter(location);
            map_canvas.gmap('option', 'zoom', 19);
            map_canvas.gmap('option', 'mapTypeId', google.maps.MapTypeId.SATELLITE);
            map_canvas.gmap('addMarker', { 'position': location });
        }
    });


    $('#center_button').click(function(){
        geocoder.geocode( { 'address': $('#id_address').val()+', '+ $('#id_city').val()}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
                map_canvas.gmap('option', 'zoom', 19);
                map_canvas.gmap('option', 'mapTypeId', google.maps.MapTypeId.SATELLITE);
                //map_canvas.gmap('addMarker', { 'position': results[0].geometry.location });
            }
        });
    });
});

function initializeMap(){
    if (!map){
        map = map_canvas.gmap('get', 'map');
        google.maps.event.addListener(map, "click", function(event) {
            var lat = event.latLng.lat();
            var lng = event.latLng.lng();
            latitude_field.val(lat.toFixed(6));
            longitude_field.val(lng.toFixed(6));
            var location = new google.maps.LatLng(lat, lng);
            map_canvas.gmap('clear', 'markers');
            map_canvas.gmap('addMarker', { 
                'position': location
            });
            calculateDistance(location);
        });
    }
}

function calculateDistance(origin_location) {
    var destinationEurecom = "Eurecom, Biot, France";
    var service = new google.maps.DistanceMatrixService();

    service.getDistanceMatrix(
            {
                origins: [origin_location],
        destinations: [destinationEurecom],
        travelMode: google.maps.TravelMode.DRIVING,
        unitSystem: google.maps.UnitSystem.METRIC,
        avoidHighways: false,
        avoidTolls: false
            }, callback);
}

function callback(response, status) {
    if (status == google.maps.DistanceMatrixStatus.OK) {
        distance_field.val(parseFloat(response.rows[0].elements[0].distance.text).toFixed(1));
            }
}
