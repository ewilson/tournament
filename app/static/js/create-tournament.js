jQuery(function ($) {
    'use strict';

    var TournamentDao = {
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
	}
    };

    var Page = {
        init: function () {
	    this.$page = $('.container');
	    this.$newTournamentForm = $('.form');
	    this.$description = $('#description');
	    this.$newTourneys = $('#new-tournaments');
	    this.$activeTourneys = $('#active-tournaments');
	    this.$tournamentTemplate = Handlebars.compile($("#tournament-template").html());
	    this.$newTournamentForm.submit(this.createTournament);
	    this.$newTourneys.on('click','.del-link',this.deleteTourney);
	    this.getNewTournaments();
	    this.getActiveTournaments();
        },
	getNewTournaments: function() {
	    TournamentDao.findByStatus({
		status: 0,
		success: Page.appendNewTournaments
	    });
	},
	getActiveTournaments: function() {
	    TournamentDao.findByStatus({
		status: 1,
		success: Page.appendActiveTournaments
	    });
	},
	deleteTourney: function(e) {
	    e.preventDefault();
	    var tournament = $(this).closest('.tourney-item');
	    var tournament_id = tournament.data('tourney_id');
	    TournamentDao.remove({
		tournament_id: tournament_id,
		success: function() {
		    tournament.remove();
		}
	    });
        },
	createTournament: function(e) {
	    console.log('createTournament');
	    e.preventDefault();
	    var description = Page.$description.val().trim();
	    if (description) {
		TournamentDao.add({
		    description: description,
		    success: Page.appendNewTournament,
		});
		Page.$description.val('');
	    } else {
		alert('Description field is required.');
	    }
        },
	appendNewTournament: function(data) {
	    var tourney = Page.$tournamentTemplate(data)
	    Page.$newTourneys.append(tourney);
	},
	appendNewTournaments: function(data) {
	    $.each(data.tournaments, function(i, tournament) {
		Page.appendNewTournament(tournament);
	    });
	},
	appendActiveTournaments: function(data) {
	    $.each(data.tournaments, function(i, tournament) {
		var tourney = Page.$tournamentTemplate(tournament)
		Page.$activeTourneys.append(tourney);
	    });
	}
    };
    Page.init();
});

