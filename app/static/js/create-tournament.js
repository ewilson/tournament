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
	    this.$tourneys = $('.tourneys');
	    this.$newTourneys = $('#new-tournaments');
	    this.$activeTourneys = $('#active-tournaments');
	    this.$completedTourneys = $('#completed-tournaments');
	    this.$tournamentTemplate = Handlebars.compile($("#tournament-template").html());
	    this.$newTournamentForm.submit(this.createTournament);
	    this.$tourneys.on('click','.del-link',this.deleteTourney);
	    this.getNewTournaments();
	    this.getActiveTournaments();
	    this.getCompletedTournaments();
        },
	getNewTournaments: function() {
	    TournamentDao.findByStatus({
		status: 0,
		success: function(data) {
		    Page.appendTournaments(data, Page.$newTourneys);
		}
	    });
	},
	getActiveTournaments: function() {
	    TournamentDao.findByStatus({
		status: 1,
		success: function(data) {
		    Page.appendTournaments(data, Page.$activeTourneys);
		}
	    });
	},
	getCompletedTournaments: function() {
	    TournamentDao.findByStatus({
		status: 2,
		success: function(data) {
		    Page.appendTournaments(data, Page.$completedTourneys);
		}
	    });
	},
	deleteTourney: function(e) {
	    e.preventDefault();
	    var that = $(this);
	    bootbox.confirm('Are you sure? There is no undelete!', function(value) {
		if (value) {		
		    var tournament = that.closest('.tourney-item');
		    var tournament_id = tournament.data('tourney_id');
		    TournamentDao.remove({
			tournament_id: tournament_id,
			success: function() {
			    tournament.remove();
			}
		    });
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
	appendTournaments: function(data, div) {
	    $.each(data.tournaments, function(i, tournament) {
		var tourney = Page.$tournamentTemplate(tournament)
		div.append(tourney);
	    });
	}
    };
    Page.init();
});

