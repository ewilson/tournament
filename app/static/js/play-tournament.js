jQuery(function ($) {
    'use strict';

    var Page = {
        init: function () {
	    this.$matches = $('#matches');
	    this.$matchForms = $('form');
	    this.$matchForms.submit(this.addMatch);
	    this.$matches.on('click','.glyphicon-remove',this.undoMatch);
	    this.$completeMatchTemplate = Handlebars.compile($("#complete-match-template").html());
        },
	addMatch: function(e) {
	    e.preventDefault();
	    var $matchForm = $(this).closest('form');
	    var $matchWell = $(this).closest('.well');
	    var options = {
		'match_id': $matchWell.data('match_id'),
		'player1_id': $matchForm.find('#player1_id').val().trim(),
		'player2_id': $matchForm.find('#player2_id').val().trim(),
		'score1': $matchForm.find('#score1').val().trim(),
		'score2': $matchForm.find('#score2').val().trim(),
		'success': function(data) {
		    Page.displayAddedMatch(data,$matchWell);
		}
	    };
	    Dao.Match.add(options);
        },
	displayAddedMatch: function(data, matchDiv) {
	    var completedMatchHtml = Page.$completeMatchTemplate(data.match);
	    matchDiv.html(completedMatchHtml);
	},
	undoMatch: function(e) {
	    e.preventDefault();
	    var match_id = $(this).closest('.well').data('match_id');
	    Dao.Match.remove({
		'match_id': match_id,
		'success': function() {
		    console.log('success');
		}
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

