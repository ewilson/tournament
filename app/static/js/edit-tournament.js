jQuery(function ($) {
    'use strict';

    var Page = {
        init: function () {
	    this.$page = $('.container');
	    this.$playerList = $('.player-list');
	    this.$addPlayerTemplate = Handlebars.compile($("#add-player-template").html());
	    this.$addForm = $('.form');
	    this.$playerList.on('click','.list-group-item',this.togglePlayer);
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
	},
	togglePlayer: function(e) {
	    e.preventDefault();
	    $(this).toggleClass('active');
	}
    };
    Page.init();
});

