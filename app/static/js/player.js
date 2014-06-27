var Player = Backbone.Model.extend({
    urlRoot: '/api/player',
    validate: function( attributes ) {
        if (attributes.fname === '') {
            bootbox.alert('Name field is required.');
            return 'Invalid';
        }
    }
});
var PlayerView = Backbone.View.extend({
    initialize: function() {
        this.render();
    },
    template: _.template("#player-templateU"),
    render: function() {
        console.log('rendering', this.model.attributes);
//        this.$el.html(this.template(this.model.attributes));
        var template = _.template( $("#player-templateU").html(), this.model.attributes);
        this.$el.html(template)
        console.log(this.el);
        return this;
    }
});

jQuery(function ($) {
    'use strict';

    var App = {
        init: function () {
	    this.playerTemplate = Handlebars.compile($("#player-template").html());
        this.playerTemplateU = Handlebars.compile($("#player-template").html());
        this.$players = $('#players');
	    this.$newPlayerForm = $('#new-player form');
	    this.$fname = $('#fname');
	    this.$players.on('click','.glyphicon-trash',this.deletePlayer);
	    this.$players.on('click',function(e) { e.preventDefault(); });
	    this.$newPlayerForm.submit(this.addPlayer);
	    this.$newPlayerForm.on('focus','input',this.removeError);
	    this.getPlayers();
        },
	getPlayers: function() {
	    Dao.Player.list({
		success: App.appendPlayers
	    });
	},
	deletePlayer: function(e) {
	    e.preventDefault();
	    e.stopPropagation();
	    var player = $(this).closest('.player-item');
	    var player_id = player.data('player_id');
	    Dao.Player.remove({
		player: player,
		player_id: player_id,
		success: function() {
		    player.remove();
		},
		error: App.displayError
	    });
        },
	addPlayer: function(e) {
	    e.preventDefault();
	    var name = App.$fname.val().trim();
        new Player({ fname: name}).save(null, {
            success: App.appendPlayerBB,
            error: App.displayError
        });
    },
	appendPlayer: function(data) {
	    var player = App.playerTemplate(data);
	    App.$players.append(player);
	},
    appendPlayerBB: function(player) {
        var playerView = new PlayerView({ model: player });
        App.$players.append(playerView.$el);
    },
	appendPlayers: function(data) {
	    $.each(data.players, function(i, player) {
		App.appendPlayer(player);
	    });
	},
	removeError: function() {
	    $("#errorMsg").fadeOut(function() {
		$(this).remove(); // need to remove after fadeOut
	    });
	},
	displayError: function(jqXHR) {
	    var responseObj = $.parseJSON(jqXHR.responseText);
	    bootbox.alert(responseObj.message);
	}
    };
    App.init();
});

