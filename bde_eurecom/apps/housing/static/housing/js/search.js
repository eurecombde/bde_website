$(document).ready(function() {

    $('#map_canvas').gmap({ 'center': '43.614252,7.072984' }).gmap('option', 'zoom', 11);
    $('#map_canvas').gmap('addMarker', {
        'position': new google.maps.LatLng(43.614252,7.072984),
        'icon': new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=E|239CD3|000000")
    }).click(function() {
        $('#map_canvas').gmap('openInfoWindow', {'content': "Eurecom"}, this);
    });

    var $accomodation_type = $("#id_accomodation_type");
    var $accomodation_type_other_input = $("#id_accomodation_type_other");
    var $accomodation_type_other_label = $("label[for=id_accomodation_type_other]");


    $accomodation_type_other_input.hide();
    $accomodation_type_other_label.hide();

    $accomodation_type.on('change', function() {
        console.log($accomodation_type.val());
        if($accomodation_type.val()==0) {
            $accomodation_type_other_input.show();
            $accomodation_type_other_label.show();
        }
        else {
            $accomodation_type_other_input.hide();
            $accomodation_type_other_label.hide();
        }
    });



    $('#search').on('click', function() {

        var get_string = search_url;
        var name, value, fields;
        first = true;
        // Construction of the GET request string
        $("#criteria_search input").each(function() {
            name = this.name;
            value = this.value;
            if(this.type=="checkbox") {
                if(this.checked) {
                    value = "True";
                }
                else {
                    value = false;
                }
            }

            if(value) {
                if(first) {
                    get_string += '?'+name+'='+value;
                    first = false;
                }
                else {
                    get_string += '&'+name+'='+value;
                }
            }
        });

        $("select").each(function() {
            name = this.name;
            value = $(this).val();

            if(value) {
                if(first) {
                    get_string += '?'+name+'='+value;
                    first = false;
                }
                else {
                    get_string += '&'+name+'='+value;
                }
            }
        });

        $('#map_canvas').gmap('clear', 'markers');

        $('#map_canvas').gmap('addMarker', {
            'position': new google.maps.LatLng(43.614252,7.072984),
            'icon': new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=E|239CD3|000000")
        }).click(function() {
            $('#map_canvas').gmap('openInfoWindow', {'content': "Eurecom"}, this);
        });

        $.getJSON(get_string, function(data) {
            $("#house_list table tbody").html("");
            $.each(data, function(i, item) {
                $("#house_list table tbody").append([
                    '<tr>',
                    '<td>',item.result_rank,'</td>',
                    '<td>','<img src="',item.thumbnail,'"/>','</td>',
                    '<td><a href="',house_url.replace('0', item.id),'"><b>',item.name,'</b></a></td>',
                    '<td>',item.number_persons,'</td>',
                    '<td>',item.surface,' m²</td>',
                    '<td>',item.city,'</td>',
                    '<td>',item.distance,' km</td>',
                    '<td><b>',item.price,' €</b></td>',
                    '</tr>'
                    ].join(''));

                $('#map_canvas').gmap('addMarker', { 
                    'position': new google.maps.LatLng(item.latitude, item.longitude),
                    'icon': new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld="+ item.result_rank +"|F85850|000000")
                }).click(function() {
                    $('#map_canvas').gmap('openInfoWindow', { 'content': item.name }, this);
                });
            });

        });
        return false;
    });
});
