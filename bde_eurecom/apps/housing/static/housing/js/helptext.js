$(document).ready(function() {
    
    $(document).tooltip({
	items: "input, textarea, select, checkbox",
	content: function() {
	    var element = $(this);
	    if($(this).next(".helptext")) {
		return $(this).siblings(".helptext").first().text();
	    }
	    return "No info";
	},
	track: true,
    });
    
    /*
      $("span.helptext").each(function() {
      console.log($(this).prev());
      
      });
    */
});
