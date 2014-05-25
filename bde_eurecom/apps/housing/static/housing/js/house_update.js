$(document).ready(function() {
    
    $("button").each(function() {
	$(this).button();
    });

    //
    // Photo multiupload
    //
    
    $('#id_img').fileupload({
        url: add_photo_url,
	dataType: 'json',
        sequentialUploads: true,
        add: function (e, data) {

	    var jqXHR = data.submit()
		.success(function (result, textStatus, jqXHR) {
		    
		}).error(function (jqXHR, textStatus, errorThrown) {
		    console.log(jqXHR);
		}).complete(function (result, textStatus, jqXHR) {

		    $("#sortable").append(
			['<li data-id="',result.id,'" data-pos="',result.pos,'">',
			 '<div class="photo" data-id="',result.id,'">',
			 '<img src="',result.thumbnail,'" alt="',result.descr,'"/>',
			 '<label for="descr">Description</label><input id="descr" name="descr" data-type="set_photo_descr" data-id="',result.id,'" value="',result.descr,'" />',
			 '<button data-type="delete_photo" data-id="',result.id,'">X</button>',
			 '</div>',
			 '</li>'
			].join('')
		    );
		    $("#sortable").find("li[data-id=" + data.id + "]").find("button").button();
		    
		    var overallProgress = $('#id_img').fileupload('progress');
		    per = Math.round(100*overallProgress.loaded/overallProgress.total);
		    if(per == 100) {
			$("#info").dialog("destroy");
			$("#info").remove();
		    }
		    else {
			$("#info").html(['<h3 style="text-align:center">Uploading: ',per,'%</h3>'].join(''));
		    }
		    

		});
        },
    }).bind('fileuploadstart', function(e, data) {
	console.log('start');
	$("body").append('<div id="info"></div>');
	$("#info").html('<h3 style="text-align:center">Uploading: 0%</h3>').dialog({
	    modal: true,
	    autoOpen: false,
	}).dialog("open");
	
    });
    
    //
    // Photo delete
    //
    
    $('body').on('click', "button[data-type=delete_photo]", function() {
	var id = $(this).data('id');
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        $.post(delete_photo_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, id:id}, function(data) {
            $("div").remove(".photo[data-id="+id+"]");
	    
	    // dialog box to validate deletion
	    /*
	      $("body").append('<div id="info"></div>');
              $("#info").html(data.content).dialog({
              modal: true,
              buttons: {
              Ok: function() {
              if(data.valid) {
              $("div").remove(".photo[data-id="+id+"]");
              }
              $(this).dialog("destroy");
              }
              }
              });*/
        }, 'json');
        return false;
    });
    
    $('body').on('change', "input[data-type=set_photo_descr]", function() {
        var id = $(this).data('id');
        var descr = $(this).val();
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        $.post(set_photo_descr_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, id:id, descr:descr});
        return false;
    });
    
    $("#sortable").sortable({
        'axis':'y',
        'update': function(event, ui) {
            var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
            var sort = $.extend({'csrfmiddlewaretoken':csrfmiddlewaretoken}, $("#sortable").sortable("toArray", {attribute:"data-id"}));
            
            $.post(sort_photo_url, sort, function(data) {
                
            });
        },
    });
    
    $('body').on('click', "button[data-type=add_room]", function() {
	var room_type = $("#id_room_type").val();
	var other_type = $("#id_other_type").val();
	var room_surface = $("#id_room_surface").val();
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
	
	callWhenPostValid(add_room_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, room_type:room_type, other_type:other_type, room_surface:room_surface}, function(data) {
	    
	    var html;

            html = '<li data-type="room" data-id="'+ data.id + '">' + data.name;
            if (data.other) {
                html += ' (' + data.other + ')';
            }

            if (data.surface) {
                html += ' : ' + data.surface + ' m² ';
            }

            html += '<button data-type="delete_room">X</button></li>';
	    
	    $("#rooms").append(html);
	    $("#rooms").find("li[data-id=" + data.id + "]").find("button").button();
            
	});
	
	return false;
    });

    $('body').on('click', "button[data-type=delete_room]", function() {
	var room = $(this).parent().data('id');
	var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
	
	callWhenPostValid(delete_room_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, room:room}, function(data) {
	    $("li[data-id=" + room + "]").remove();
	});

	return false;
    });

    /********************************/
    /* CONTRIBUTORS                 */
    /********************************/
    
    /**
     * Delete a contributor
     *
     *
     */
    
    $('body').on('click', "button[data-type=add_contributor]", function() {
	
	var user = $("#id_user").val();
	var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
	
	callWhenPostValid(add_contributor_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, user:user}, function(data) {
	    $("#contributor").find("ul").append(
		['<li>',data.user,'<button data-type="delete_contributor" data-user="',data.id_user,'">X</button>','</li>'].join("")
	    );
	});
	
	return false;
    });
    
    /**
     * Delete a contributor
     *
     *
     */
    
    
    $('body').on('click', "button[data-type=delete_contributor]", function() {

	var $button = $(this);
	var user = $button.data('user');
	var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
	
	callWhenPostValid(delete_contributor_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, user:user}, function(data) {
	    $button.parent().remove();
	});
	
	return false;
    });

    /*
	$("body").append('<div id="info"></div>');
	var $info = $("#info");
	$info.html('<div id="loading"><div class="progress-label">Loading</div></div>');
	$("#loading").progressbar({
	    value:false,
	});
	$info.dialog({
            modal: true,
            width: 400,
        });

	$.post(delete_contributor_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, user:user}, function(data) {
	    
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
		$button.parent().remove();
	    }
	});
    */

    /********************************/
    /* END CONTRIBUTORS             */
    /********************************/



    $("#accordion > div").accordion({
        header: "h3",
        heightStyle: "content",
	collapsible: true,
        active: false,
    });
    
    /*
    //piece of code to ensure that the user doesn't have to scroll after changing acordion
    $('#accordion h3').bind('click',function(){
    var self = this;
    setTimeout(function() {
    theOffset = $(self).offset();
    $('body,html').animate({ scrollTop: theOffset.top - 100 });
    }, 500); // ensure the collapse animation is done
    });*/

    $('body').on('click', "button[data-type=update]", function() {
	
	var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
	var model = $(this).parent().attr("id");
	var form = $("#form").serializeArray();
	$("body").append('<div id="info"></div>');
	var $info = $("#info");
	// form.push({name:'model', value:model});
	// form.push({name:'csrfmiddlewaretoken', value:csrfmiddlewaretoken});

	$info.html('<div id="info_loading"><div class="progress-label">Loading</div></div>');

	$("#loading").progressbar({
	    value:false,
	});

	$info.dialog({
            modal: true,
            width: 400,
	});
	
	
	$.post(house_update_url, form, function(data) {
	    
	    $(".error").each(function() {
		console.log($(this));
		$(this).prev().removeClass("error_input");
		$(this).remove();
		
	    });
	    if(data != "VALID") {
		var $div;
		var text = ['<h3>There are errors in the form!<h3/>'];
		$.each(data, function(i, item) {
		    $div = $("#id_" + i);
		    console.log($div);
		    $div.addClass("error_input");
		    $div.after(
			['<span class="error">',item,'</span>'].join("")
		    );
		    text.push("<p>");
		    text.push(i);
		    text.push(" : ");
		    text.push(item);
		    text.push("</p>");
		});
		$info.html(text.join(""));
                $info.dialog({
                    modal: true,
                    buttons: {
                        "OK": function() {
                            $(this).dialog("destroy");
                        }
                    },
                    width: 400,
                });
		
	    }
	    else {
		$info.html("The house has just been updated!");		
                $info.dialog({
                    modal: true,
                    buttons: {
                        "Continue to edit": function() {
                            $(this).dialog("destroy");
                        },
                        "See Result": function() {
                            window.onbeforeunload = null;
                            window.location.href = house_url.replace('0', house_id);
                        }
                    },
                    width: 400,
                });
	    }
	});
	
	return false;
    });

    $otherFormField = $("#id_other_type").parent();
    $otherFormField.hide();

    $("#id_room_type").change(function(){
        if ($(this).val()==10){
            $otherFormField.show();
        }
        else {
            $otherFormField.hide();
        }
    });

    $(".required > label").append("<span class='asterisk'> *</span>")

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


    function callWhenPostValid(url, postData, callbackWhenValid, dialogId = "info") {

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

});

window.onbeforeunload = function() {
    return "You're leaving the update page, make sure that you clicked on the Updtate button.";
};

