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
    player = $(".player-item").first().clone();
    player.find('.fname').text(data.fname);
    player.attr('id',"player_" + data.id);
    player.find('a').attr('player_id',data.id);
    player.appendTo("#players");
};
NewPlayerView.prototype.clearInput = function() {
    $('#fname').val('');
};


$(document).ready(function() {
    var players = new Players();
    new NewPlayerView({ players: players });

    $('.player-item a').click(function() {
	player_id = $(this).attr('player_id')
        $.ajax({
            url: $SCRIPT_ROOT + '/player-del/' + player_id,
            type: 'DELETE',
            dataType: 'json',  
            success: function(data) {
		$('#player_' + data.id).remove()
            }
        });
    });

});
