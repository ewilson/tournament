jQuery(function ($) {
    'use strict';

    var Page = {
        init: function () {
	    this.$omittedPlayers = $('.omitted-players');
	    this.$addedPlayers = $('.added-players');
	    this.$playerTemplate = Handlebars.compile($("#player-template").html());
	    this.$addForm = $('form');
	    this.$omittedPlayers.on('click','.list-group-item',this.enterT);
	    this.$addedPlayers.on('click','.list-group-item',this.exitT);
	    this.getPlayers();
	    this.tournament_id = $('h1').data('tournament_id');
	    this.$addForm.submit(this.startTourney);
	    this.$button = $('button');
        },
	getPlayers: function() {
	    Dao.Player.list({
		success: Page.getAddedPlayers
	    });
        },
	resetPlayers: function() {
	    Page.$addedPlayers.find('a').remove();
	    Page.$omittedPlayers.find('a').remove();
	    Page.getPlayers();
	},
	getAddedPlayers: function(allPlayers) {
	    Dao.Tournament.findPlayers({
		tournament_id: Page.tournament_id,
		success: function(data) {
		    var all = allPlayers.players;
		    var added = data.players;
		    var added_ids = $.map(added, function(player, i) {
			return player.player_id;
		    });
		    var omitted = $.grep(all, function(player, i){
			return $.inArray(player.player_id, added_ids) == -1
		    });
		    Page.appendPlayers(added,Page.$addedPlayers);
		    Page.appendPlayers(omitted,Page.$omittedPlayers);
		}
	    });
	},
	toggleButton: function() {
	    Page.$button.prop('disabled', 
			      Page.$addedPlayers.find('a').length < 3);
	},
	enterT: function(e) {
	    e.preventDefault();
	    Page.toggleEntry($(this),'POST',Page.$addedPlayers);
	},
	exitT: function(e) {
	    e.preventDefault();
	    Page.toggleEntry($(this),'DELETE',Page.$omittedPlayers);
	},
	toggleEntry: function(player,verb,target) {
	    Dao.Tournament.updatePlayer({
		tournament_id: Page.tournament_id,
		player_id: player.data('player_id'),
		player: player,
		httpVerb: verb,
		success: function(data) {
		    Page.movePlayer(data,player,target);
		},
		error: Page.resetPlayers
	    });
	},
	movePlayer: function(data,player,target) {
	    var playerHtml = Page.$playerTemplate(data.player);
	    target.append(playerHtml);
	    player.remove();
	    Page.toggleButton();
	},
	appendPlayers: function(data,list) {
	    $.each(data, function(i, player) {
		var playerHtml = Page.$playerTemplate(player);
		list.append(playerHtml);
	    });
	    Page.toggleButton();
	},
	startTourney: function(e) {
	    e.preventDefault();
	    Dao.Tournament.updateStatus({
		tournament_id: Page.tournament_id,
		status: 1,
		success: function(data) {
		    window.location.href = $APP_ROOT + "/tournament/" +
			Page.tournament_id;
		}
	    });
	}
    };
    Page.init();
});

