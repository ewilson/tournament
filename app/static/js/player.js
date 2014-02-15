jQuery(function ($) {
    'use strict';

    var App = {
        init: function () {
	    this.playerTemplate = Handlebars.compile($("#player-template").html());
	    this.$page = $('.container');
            this.$players = $('#players');
	    this.$newPlayerForm = $('#new-player form');
	    this.$fname = $('#fname');
	    this.$players.on('click','.del-link',this.deletePlayer);
	    this.$page.on('click','.glyphicon-remove',this.removeError);
	    this.$newPlayerForm.submit(this.addPlayer);
	    this.$newPlayerForm.on('focus','input',this.removeError);
	    this.getPlayers();
        },
	getPlayers: function() {
	    Dao.Player.list({
		success: App.appendPlayers
	    });
	},
	deletePlayer: function(e) {
	    e.preventDefault();
	    var player = $(this).closest('.player-item');
	    var player_id = player.data('player_id');
	    Dao.Player.remove({
		player: player,
		player_id: player_id,
		success: function() {
		    player.remove();
		},
		error: App.displayError
	    });
        },
	addPlayer: function(e) {
	    e.preventDefault();
	    var name = App.$fname.val().trim();
	    if (name) {
		Dao.Player.add({
		    fname: name,
		    success: App.appendPlayer,
		    error: App.displayError
		});
		App.$fname.val('');
	    } else {
		bootbox.alert('Name field is required.');
	    }
        },
	appendPlayer: function(data) {
	    var player = App.playerTemplate(data);
	    App.$players.append(player);
	},
	appendPlayers: function(data) {
	    $.each(data.players, function(i, player) {
		App.appendPlayer(player);
	    });
	},
	removeError: function() {
	    $("#errorMsg").fadeOut(function() {
		$(this).remove(); // need to remove after fadeOut
	    });
	},
	displayError: function(jqXHR) {
	    var responseObj = $.parseJSON(jqXHR.responseText);
	    bootbox.alert(responseObj.message);
	}
    };
    App.init();
});

