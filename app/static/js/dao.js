var Dao = (function($) {
    var Player = {
	add: function(options) {
	    $.ajax({
		url: $SCRIPT_ROOT + '/player',
		type: 'POST',
		dataType: 'json',
		data: { fname: options.fname },
		success: options.success,
		error: options.error
	    });
	},
	remove: function(options) {
	    $.ajax({
		url: $SCRIPT_ROOT + '/player/' + options.player_id,
		type: 'DELETE',
		dataType: 'json',
		success: options.success,
		error: options.error
	    });
	},
	list: function(options) {
	    $.ajax({
		url: $SCRIPT_ROOT + '/player',
		type: 'GET',
		dataType: 'json',
		success: options.success
	    })
	}
    };

    var Tournament = {
	add: function(options) {
	    $.ajax({
		url: $SCRIPT_ROOT + '/tournament',
		type: 'POST',
		dataType: 'json',
		data: { description: options.description },
		success: options.success
	    });
	},
	remove: function(options) {
	    $.ajax({
		url: $SCRIPT_ROOT + '/tournament/' + options.tournament_id,
		type: 'DELETE',
		dataType: 'json',
		success: options.success
	    });
	},
	findByStatus: function(options) {
	    $.ajax({
		url: $SCRIPT_ROOT + '/tournament/status/' + options.status,
		type: 'GET',
		dataType: 'json',
		success: options.success
	    })
	},
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
	    console.log('URL',url);
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
	    })
	}
    };

    return {
	Player: Player,
	Tournament: Tournament,
	Match: Match
    }
}(jQuery));
