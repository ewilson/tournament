jQuery(function ($) {
    'use strict';

    var Page = {
        init: function () {
	    this.$page = $('.container');
	    this.$playerList = $('.player-list');
	    this.$addPlayerTemplate = Handlebars.compile($("#add-player-template").html());
	    this.$addForm = $('form');
	    this.$playerList.on('click','.list-group-item',this.togglePlayer);
	    this.getPlayers();
	    this.$addForm.submit(this.addPlayers);
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
	},
	addPlayers: function(e) {
	    e.preventDefault();
	    var players = $('.active')
	    var ids = players.map(function() {
		return $(this).data("player_id");
	    });
	    console.log(JSON.stringify(ids.get()));
	    var id = $('h1').data('tournament_id');
	    console.log(id);
	}
    };
    Page.init();
});

