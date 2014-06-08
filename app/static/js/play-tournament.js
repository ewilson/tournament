jQuery(function ($) {
    'use strict';

    var Page = {
        init: function () {
	    this.$matches = $('#matches');
	    this.$matchForms = $('form');
	    this.$completeButton = $('#complete');
	    this.$completeButton.hide();
	    this.$head = $('#head');
	    this.$matches.on('submit', '.match-form', this.addMatch);
	    this.$matches.on('click','.glyphicon-remove',this.undoMatch);
	    this.$completeButton.click(this.completeTournament);
	    this.$completeMatchTemplate = Handlebars.compile($("#complete-match-template").html());
	    this.$matchFormTemplate = Handlebars.compile($("#match-form-template").html());
	    this.$matchWellTemplate = Handlebars.compile($("#match-well-template").html());
	    this.$congratsTemplate = Handlebars.compile($("#congrats-template").html());
	    this.$headTemplate = Handlebars.compile($("#head-template").html());
	    this.$standingsBody = $('#standings');
	    this.$standingRowsTemplate = Handlebars.compile($("#standing-rows-template").html());
	    this.tournament_id = this.$head.data('tournament_id');
	    this.tournament_name = '';
	    this.getMatches();
	    this.displayStandings();
	    this.getHeader();
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
		    Page.displayAddedMatch(data, $matchWell);
		    Page.displayStandings();
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
	    var $matchWell = $(this).closest('.well');
	    var match_id = $matchWell.data('match_id');
	    Dao.Match.remove({
		'match_id': match_id,
		'success': function(data) {
		    Page.displayMatchForm(data, $matchWell);
		    Page.displayStandings();
		}
	    });
        },
	displayMatchForm: function(data, matchDiv) {
	    var matchFormHtml = Page.$matchFormTemplate(data.match);
	    matchDiv.html(matchFormHtml);
	},
	displayStandings: function() {
	    Dao.Standings.findByTournament({
		tournament_id: Page.tournament_id,
		'success': function(data) {
		    var standingsHtml = Page.$standingRowsTemplate(data);
		    Page.$standingsBody.html(standingsHtml);
		}
	    });
	},
	getMatches: function() {
	    Dao.Match.findByTournament({
		tournament_id: Page.tournament_id,
		success: Page.displayAllMatches
	    });
	},
	displayAllMatches: function(data) {
	    $.each(data.matches, function(i, match) {
		var matchTemplate = $(Page.$matchWellTemplate({'match_id':match.match_id}));
		if (match.entered_time) {
		    var matchHtml = Page.$completeMatchTemplate(match);
		} else {
		    var matchHtml = Page.$matchFormTemplate(match);
		}
		matchTemplate.html(matchHtml);
		Page.$matches.append(matchTemplate);
	    });
	},
	completeTournament: function() {
	    Dao.Tournament.updateStatus({
		tournament_id: Page.tournament_id,
		status: 2,
		type: 'POST',
		success: Page.renderCompletePage
	    });
	},
	renderCompletePage: function() {
	    Page.$completeButton.remove();
	    var winner = Page.findWinner();
	    var congratsHtml = Page.$congratsTemplate({'description':Page.tournament_name, 'winner':winner}); 
	    Page.$head.html(congratsHtml);
	    Page.removeUplayedGames();
	    Page.removeUndo();
	},
	removeUplayedGames: function() {
	    $('.match-form').closest('div').remove();
	},
	removeUndo: function() {
	    $('.glyphicon-remove').closest('a').remove();
	},
	findWinner: function() {
	    return Page.$standingsBody.find('.name').first().text();
	},
	getHeader: function() {
	    Dao.Tournament.find({
		tournament_id: Page.tournament_id,
		success: function(data) {
		    Page.tournament_name = data.tournament.description;
		    Page.renderHeader(data);
		}
	    });
	},
	renderHeader: function(data) {
	    if (data.tournament.status == 1) {
		var head = Page.$headTemplate(data.tournament);
		Page.$completeButton.show();
	    } else {
		Page.renderCompletePage();
	    }
	    Page.$head.html(head);
	},
	
    };
    Page.init();
});

