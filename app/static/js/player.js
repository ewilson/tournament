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
    player.appendTo("#players");
};
NewPlayerView.prototype.clearInput = function() {
    $('#fname').val('');
};

$(document).ready(function() {
    var players = new Players();
    new NewPlayerView({ players: players });
});
