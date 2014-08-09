App.PlayersController = Ember.ArrayController.extend({
    actions: {
        createPlayer: function() {
            var fname = this.get('newFname');
            if (!fname || !fname.trim()) { return false; }

            var onFail = function(response) {
                alert(response.responseText);
            };

            var player = this.store.createRecord('player', {
                fname: fname
            });

            this.set('newFname', '');
            player.save().then(function() {}, onFail);
        }
    }
});
