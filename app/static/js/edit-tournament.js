jQuery(function ($) {
    'use strict';

    var Page = {
        init: function () {
	    this.$page = $('.container');
	    this.$omittedPlayers = $('.omitted-players');
	    this.$addedPlayers = $('.added-players');
	    this.$playerTemplate = Handlebars.compile($("#player-template").html());
	    this.$addForm = $('form');
	    this.$omittedPlayers.on('click','.list-group-item',this.enter);
	    this.getPlayers();
	    this.tournament_id = $('h1').data('tournament_id');
	    this.getPlayersInTournament();
	    this.$addForm.submit(this.addPlayers);
        },
	getPlayers: function() {
	    Dao.Player.list({
		success: function(data) {
		    Page.appendPlayers(data);
		}
	    });
        },
	getPlayersInTournament: function() {
	    Dao.Tournament.findPlayers({
		tournament_id: Page.tournament_id,
		success: function(data) {
		    Page.appendAddedPlayers(data);
		}
	    });
	},
	enter: function(e) {
	    e.preventDefault();
	    var player = $(this);
	    Dao.Tournament.updatePlayer({
		tournament_id: Page.tournament_id,
		player_id: player.data('player_id'),
		player: player,
		httpVerb: 'POST',
		success: function(data) {
		    Page.toRightList(data,player);
		}
	    });
	},
	toRightList: function(data,player) {
	    var playerHtml = Page.$playerTemplate(data.player);
	    Page.$addedPlayers.append(playerHtml);
	    player.remove();
	},
	appendPlayers: function(data) {
	    $.each(data.players, function(i, player) {
		var playerHtml = Page.$playerTemplate(player);
		Page.$omittedPlayers.append(playerHtml);
	    });
	},
	addPlayers: function(e) {
	    e.preventDefault();
	    var players = $('.active');
	    var ids = players.map(function() {
		return $(this).data("player_id");
	    });
	    console.log(JSON.stringify(ids.get()));
	    console.log(Page.tournament_id);
	}
    };
    Page.init();
});

