function addPlayer(options) {
    $.ajax({
        url: $SCRIPT_ROOT + '/_add-player',
        type: 'POST',
        dataType: 'json',
        data: { fname: options.fname },
        success: options.success
    });
}

$(document).ready(function() {
    $('#new-player form').submit(function(e) {
        e.preventDefault();

	addPlayer({
	    fname: $('#fname').val(),
            success: function(data) {
		$('#players').append('<li>' + data.fname + '</li>');
		$('#fname').val('');
            }
        });
    });
});
