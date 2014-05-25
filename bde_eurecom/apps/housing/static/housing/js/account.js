$(document).ready(function() {
    
    $("button").each(function() {
	$(this).button();
    });

    $("#profile_update").on('click', function() {
	var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
	var form = $("#profile_form").serializeArray();    
	form.push({name:'csrfmiddlewaretoken', value:csrfmiddlewaretoken});
	callWhenPostValid(account_update_url, form, function(data) {
	    
	});
	return false;
    });

});
