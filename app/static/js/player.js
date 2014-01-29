var Players = function() {
};
Players.prototype.add = function(options) {
    $.ajax({
        url: $SCRIPT_ROOT + '/player',
        type: 'POST',
        dataType: 'json',
        data: { fname: options.fname },
        success: options.success
    });
};
Players.prototype.delete = function(options) {
    $.ajax({
        url: $SCRIPT_ROOT + '/player',
        type: 'DELETE',
        dataType: 'json',
        data: { id: options.id },
        success: options.success
    });
};

var NewPlayerView = function(options) {
    this.players = options.players;
    var add = $.proxy(this.addPlayer, this)
    $('#new-player form').submit(add);
};
NewPlayerView.prototype.addPlayer = function(e) {
    e.preventDefault();

    var that = this;

    this.players.add({
        fname: $('#fname').val(),
        success: function(data) {
	    that.appendPlayer(data);
	    that.clearInput();
        }
    });
};
NewPlayerView.prototype.appendPlayer = function(data) {
    var playerTemplate = Handlebars.compile($("#player-template").html());
    var playerData = {id: data.id, fname: data.fname}
    var player = playerTemplate(playerData);
    $('#players').append(player);
};
NewPlayerView.prototype.clearInput = function() {
    $('#fname').val('');
};


$(document).ready(function() {
    var players = new Players();
    new NewPlayerView({ players: players });

    $('#players').on('click', '.del-link', function(e) {
	e.preventDefault();
	player_id = $(this).closest('.player-item').data('player_id');
        $.ajax({
            url: $SCRIPT_ROOT + '/player/' + player_id,
            type: 'DELETE',
            dataType: 'json',  
            success: function(data) {
		var data_select = 'div[data-player_id=' + data.id + ']';
		$('.player-item').filter(data_select).remove();
            }
        });
    });

});
