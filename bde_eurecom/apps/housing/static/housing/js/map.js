/*      $('#map_canvas').gmap().bind('init', function() { 
              // This URL won't work on your localhost, so you need to change it
              // see http://en.wikipedia.org/wiki/Same_origin_policy
              $.getJSON( STATIC_URL+'js/demo.json', function(data) { 
                  $.each( data.markers, function(i, marker) {
                      $('#map_canvas').gmap('addMarker', { 
                          'position': new google.maps.LatLng(marker.latitude, marker.longitude), 
                          'bounds': true 
                          }).click(function() {
                              $('#map_canvas').gmap('openInfoWindow', { 'content': marker.content }, this);
                              });
                      });
                  });
              });*/
$(document).ready(function() {

    $('#map_canvas').gmap({ 'center': '43.614252,7.072984' }).gmap('option', 'zoom', 11);
    $('#map_canvas').gmap('addMarker', {
        'position': new google.maps.LatLng(43.614252,7.072984),
        'icon': new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=E|239CD3|000000")
    }).click(function() {
        $('#map_canvas').gmap('openInfoWindow', {'content': "Eurecom"}, this);
    });


    $('#triggerButton').click(function(){
        // $.getJSON( STATIC_URL+'js/demo.json', function(data) { 
        $.getJSON( 'map/all', function(data) { 
            $.each( data.markers, function(i, marker) {
                $('#result').append("<br>" + marker.rank + " : " + marker.latitude + ", " + marker.longitude + ", " + marker.content);
                $('#map_canvas').gmap('addMarker', { 
                    'position': new google.maps.LatLng(marker.latitude, marker.longitude),
                    'icon': new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld="+ marker.rank +"|F85850|000000")
                }).click(function() {
                    $('#map_canvas').gmap('openInfoWindow', { 'content': marker.content }, this);
                });
            });
        });
    });

    });
    // https://developers.google.com/chart/image/docs/gallery/dynamic_icons#pins to design pins

