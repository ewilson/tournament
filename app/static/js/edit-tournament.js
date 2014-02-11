jQuery(function ($) {
    'use strict';

    var Page = {
        init: function () {
	    this.$page = $('.container');
	    this.$playerList = $('.player-list');
	    this.$addPlayerTemplate = Handlebars.compile($("#add-player-template").html());
	    this.$addPlayerForm = $('.form');
	    this.getPlayers();
        },
	getPlayers: function() {
	    Dao.Player.list({
		success: function(data) {
		    Page.appendPlayers(data);
		}
	    });
	},
	appendPlayers: function(data) {
	    $.each(data.players, function(i, player) {
		var playerHtml = Page.$addPlayerTemplate(player)
		Page.$playerList.append(playerHtml);
	    });
	}
    };
    Page.init();
});

