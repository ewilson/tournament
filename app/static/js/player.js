jQuery(function ($) {
    'use strict';

    var PlayerDao = {
	add: function(options) {
	    $.ajax({
		url: $SCRIPT_ROOT + '/player',
		type: 'POST',
		dataType: 'json',
		data: { fname: options.fname },
		success: options.success
	    });
	},
	remove: function(options) {
	    $.ajax({
		url: $SCRIPT_ROOT + '/player',
		type: 'DELETE',
		dataType: 'json',
		data: { id: options.id },
		success: options.success
	    });
	}
    };

    var App = {
        init: function () {
	    this.playerTemplate = Handlebars.compile($("#player-template").html());
	    this.$newPlayerForm = $('#new-player form');
            this.$players = $('#players');
	    this.$fname = this.$newPlayerForm.find('#fname');
	    this.$players.on('click','.del-link',this.removePlayer)
        },
	removePlayer: function(e) {
	    e.preventDefault();
	    var player_id = $(this).closest('.player-item').data('player_id');
	    console.log('ID:',player_id)
	    $(this).closest('.player-item').remove();
        }
    };
    App.init();
});

