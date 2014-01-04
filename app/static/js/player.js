var Players = function() {
};
Players.prototype.add = function(options) {
    $.ajax({
        url: $SCRIPT_ROOT + '/_add-player',
        type: 'POST',
        dataType: 'json',
        data: { fname: options.fname },
        success: options.success
    });
};

var NewPlayerView = function(options) {
    var players = options.players;

    $('#new-player form').submit(function(e) {
        e.preventDefault();
	
	players.add({
	    fname: $('#fname').val(),
            success: function(data) {
		$('#players').append('<li>' + data.fname + '</li>');
		$('#fname').val('');
            }
        });
    });
};

$(document).ready(function() {
    var players = new Players();

    new NewPlayerView({ players: players });
});
