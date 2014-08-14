var Dao = (function($) {
    var Tournament = {
	findPlayers: function(options) {
	    $.ajax({
		url: $SCRIPT_ROOT + '/tournament/' + options.tournament_id + 
		    '/player',
		type: 'GET',
		dataType: 'json',
		success: options.success
	    })
	},
	updatePlayer: function(options) {
	    $.ajax({
		url: $SCRIPT_ROOT + '/tournament/' + options.tournament_id +
		     '/player/' + options.player_id,
		type: options.httpVerb,
		dataType: 'json',
		success: options.success,
		error: options.error
	    });
	},
	updateStatus: function(options) {
	    var url = $SCRIPT_ROOT + '/tournament/' + options.tournament_id +
		'/status/' + options.status;
	    $.ajax({
		url: url,
		type: 'POST',
		dataType: 'json',
		success: options.success
	    });
	}
    };

    var Match = {
	add: function(options) {
	    $.ajax({
		url: $SCRIPT_ROOT + '/match/' + options.match_id,
		type: 'POST',
		dataType: 'json',
		data: { player1_id: options.player1_id,
			player2_id: options.player2_id,
			score1: options.score1,
			score2: options.score2 },
		success: options.success
	    });
	},
	remove: function(options) {
	    $.ajax({
		url: $SCRIPT_ROOT + '/match/' + options.match_id,
		type: 'DELETE',
		dataType: 'json',
		success: options.success
	    });
	},
	findByTournament: function(options) {
	    var url = $SCRIPT_ROOT + '/tournament/' + options.tournament_id + '/match'
	    $.ajax({
		url: url,
		type: 'GET',
		dataType: 'json',
		success: options.success
	    });
	}
    };

    var Standings = {
	findByTournament: function(options) {
	    var url = $SCRIPT_ROOT + '/tournament/' + options.tournament_id + '/standings'
	    $.ajax({
		url: url,
		type: 'GET',
		dataType: 'json',
		success: options.success
	    });
	}
    };

    return {
	Tournament: Tournament,
	Match: Match,
	Standings: Standings
    }
}(jQuery));
