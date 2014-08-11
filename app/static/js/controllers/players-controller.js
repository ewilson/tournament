App.PlayersController = Ember.ArrayController.extend({
    actions: {
        createPlayer: function() {
            var fname = this.get('newFname');
            if (!fname || !fname.trim()) { return false; }

            var player = this.store.createRecord('player', {
                fname: fname
            });

            var onFail = function(response) {
                alert(response.responseText);
                player.rollback();
            };

            this.set('newFname', '');
            player.save().then(function() {}, onFail);
        }
    }
});
