var AllPlayers = Backbone.Collection.extend({

    model: Player,
    url: '/api/player'

});

var allPlayers = new AllPlayers();
allPlayers.fetch({success: function(collection, response, options) {
    console.log('collection', collection);
    console.log('response', response.players);
    console.log('options', options);
}, error: function() {
    console.log('oops')
}});
