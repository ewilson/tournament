jQuery(function ($) {
    'use strict';

    var Page = {
        init: function () {
	    this.$matchForms = $('form');
	    this.$matchForms.submit(this.addMatch);
        },
	addMatch: function(e) {
	    console.log('addMatch');
	    e.preventDefault();
/*	    var description = Page.$description.val().trim();
	    if (description) {
		Dao.Tournament.add({
		    description: description,
		    success: Page.appendNewTournament,
		});
		Page.$description.val('');
	    } else {
		alert('Description field is required.');
	    }*/
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

