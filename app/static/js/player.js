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
		url: $SCRIPT_ROOT + '/player/' + options.player_id,
		type: 'DELETE',
		dataType: 'json',
		success: options.success,
		error: function(jqXHR,textStatus,errorThrown) {
		    console.log(jqXHR.responseText);
//		    var errorAlert = App.errorTemplate(jqXHR.responseText);
		    var errorAlert = App.errorTemplate({'message':'My Message'});
		    App.$errorContainer.append(errorAlert);
		}
	    });
	},
	list: function(options) {
	    $.ajax({
		url: $SCRIPT_ROOT + '/player',
		type: 'GET',
		dataType: 'json',
		success: options.success
	    })
	}
    };

    var App = {
        init: function () {
	    this.playerTemplate = Handlebars.compile($("#player-template").html());
	    this.errorTemplate = Handlebars.compile($("#error-template").html());
	    this.$page = $('.container');
	    this.$errorContainer = $('#errorContainer');
            this.$players = $('#players');
	    this.$fname = $('#fname');
	    this.$players.on('click','.del-link',this.deletePlayer);
	    this.$page.on('click','.glyphicon-remove-circle',this.removeDiv);
	    $('#new-player form').submit(this.addPlayer);
	    this.getPlayers();
        },
	getPlayers: function() {
	    PlayerDao.list({
		success: App.appendPlayers
	    });
	},
	deletePlayer: function(e) {
	    e.preventDefault();
	    var player = $(this).closest('.player-item');
	    var player_id = player.data('player_id');
	    PlayerDao.remove({
		player: player,
		player_id: player_id,
		success: function() {
		    player.remove();
		}
	    });
        },
	addPlayer: function(e) {
	    e.preventDefault();
	    PlayerDao.add({
		fname: App.$fname.val(),
		success: App.appendPlayer
	    });
        },
	appendPlayer: function(data) {
	    var player = App.playerTemplate(data);
	    App.$players.append(player);
	    App.$fname.val('');
	},
	appendPlayers: function(data) {
	    $.each(data.players, function(i, player) {
		App.appendPlayer(player);
	    });
	},
	removeDiv: function(data) {
	    $(this).closest('div').remove();
	}
    };
    App.init();
});

