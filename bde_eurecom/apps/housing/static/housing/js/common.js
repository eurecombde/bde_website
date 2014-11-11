/**
 *
 * This function POST data postData to url and wait for a response 
 * from the server with two parameters : 
 *  - valid : if the action is valid
 *  - content : feedback to the user
 * A dialog is created with a loading bar,
 * when POST returns, content is shown to the user in the dialog,
 * if valid is set to true, callbackWhenValid function is called
 * callbackWhenValid can access to data return by POST
 *
 */


function callWhenPostValid(url, postData, callbackWhenValid, dialogId) {
    if(typeof(dialogId)==='undefined') dialogId = "info";

    $("body").append('<div id="' + dialogId + '"></div>');

    var $info = $("#" + dialogId);

    $info.html('<div id="' + dialogId + '_loading"><div class="progress-label">Loading</div></div>');

    $("#loading").progressbar({
	value:false,
    });

    $info.dialog({
        modal: true,
        width: 400,
    });
    
    $.post(url, postData, function(data) {
	
	$info.text(data.content);
	$info.dialog({
	    modal: true,
	    buttons: {
                "OK": function() {
		    $(this).dialog("destroy");
                }
	    },
	    width: 400,
        });
	
	if(data.valid) {
	    callbackWhenValid(data);
	}
    });
}
