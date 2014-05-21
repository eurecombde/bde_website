$(document).ready(function() {
    $("#information").tabs({
	heightStyle: "auto",
    });

    $("button").each(function() {
	$(this).button();
    });
});
