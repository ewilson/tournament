app.AllPlayers = Backbone.Collection.extend({

    model: Player,
    url: '/api/player',
    initialize: function() {
        console.log('AllPlayers collection init');
    }

});
