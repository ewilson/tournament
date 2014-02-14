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
	    this.$addForm.submit(this.addPlayers);
        },
	getPlayers: function() {
	    Dao.Player.list({
		success: Page.getAddedPlayers
	    });
        },
	getAddedPlayers: function(allPlayers) {
	    Dao.Tournament.findPlayers({
		tournament_id: Page.tournament_id,
		success: function(data) {
		    var all = allPlayers.players;
		    var added = data.players;
		    var added_ids = $.map(added, function(player, i) {
			return player.id;
		    });
		    var omitted = $.grep(all, function(player, i){
			return $.inArray(player.id, added_ids) == -1
		    });
		    Page.appendPlayers(added,Page.$addedPlayers);
		    Page.appendPlayers(omitted,Page.$omittedPlayers);
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
	appendPlayers: function(data,list) {
	    $.each(data, function(i, player) {
		var playerHtml = Page.$playerTemplate(player);
		list.append(playerHtml);
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

