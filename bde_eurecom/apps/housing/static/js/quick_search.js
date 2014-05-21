$(document).ready(function() {
    var $quick_search = $("#quick_search");
    $quick_search.val('');

    $quick_search.autocomplete({
	source: quick_search_url,
	minLength: 2,
	focus: function( event, ui ) {
	    $quick_search.val(ui.item.label);
	    return false;
	},
	select: function(event, ui) {
	    $quick_search.val(ui.item.label);
	    window.location = house_url.replace('0', ui.item.value);
	    return false;
	}
    });
});
