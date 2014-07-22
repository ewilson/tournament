app.PlayersView = Backbone.View.extend({

    initialize: function() {
        this.template = '#players';
        var allPlayers = new app.AllPlayers();
        var self = this;
        allPlayers.fetch({success: function(collection, response, options) {
            console.log('IN VIEW');
            console.log('collection', collection);
            console.log('response', response.players);
            console.log('options', options);
            self.models = response.players;
            self.render();

            console.log('sr')
        }, error: function() {
            console.log('oops')
        }});
        console.log('DUN INIT');
    },

    /*
     * Get the template content and render it into a new div-element
     */
    render: function() {
        console.log('MODEL?',this.models);
        var content = $(this.template).html();
        $(this.el).html(content);

        return this;
    }

});
