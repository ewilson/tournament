function addPlayer(options) {
    $.ajax({
        url: $SCRIPT_ROOT + '/_add-player',
        type: 'POST',
        dataType: 'json',
        data: { fname: $('#fname').val() },
        success: function(data) {
            $('#players').append('<li>' + data.fname + '</li>');
            $('#fname').val('');
        }
    });
}

$(document).ready(function() {
    $('#new-player form').submit(function(e) {
        e.preventDefault();

	addPlayer();
    });
});
