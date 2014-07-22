app.AllPlayers = Backbone.Collection.extend({

    model: app.Player,
    url: '/api/player',
    initialize: function() {
        console.log('AllPlayers collection init');
    }

});
