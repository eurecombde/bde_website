$(document).ready(function() {
    initialized = false;
    $("#ui-id-7").click(function(){
        if(!initialized) {
            initialized = true;
            $('#map_canvas').gmap({ 'center': latitude+','+longitude }).gmap('option', 'zoom', 13);
            $('#map_canvas').gmap('addMarker', {'position': new google.maps.LatLng(latitude,longitude)});
            $('#map_canvas').gmap('addMarker', {
                'position': new google.maps.LatLng(43.614252,7.072984),
                'icon': new google.maps.MarkerImage(STATIC_URL+"housing/img/pinE.png")
                //'icon': new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=E|239CD3|000000")
            }).click(function() {
                $('#map_canvas').gmap('openInfoWindow', {'content': "Eurecom"}, this);
            });
        }
    }); 
}); 
