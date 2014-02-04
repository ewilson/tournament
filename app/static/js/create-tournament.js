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

    var Page = {
        init: function () {
	    this.$page = $('.container');
	    this.$newTournamentForm = $('.form');
	    this.$description = $('#description');
	    this.$newTourneys = $('#New');
	    this.$newTournamentForm.submit(this.createTournament);
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
	    Page.$newTourneys.append('Hello');
	}
    };
    Page.init();
});

