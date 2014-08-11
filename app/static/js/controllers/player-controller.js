App.PlayerController = Ember.ObjectController.extend({
    actions: {
        removePlayer: function() {
            var player = this.get('model');

            var onFail = function(response) {
                alert(response.responseText);
                player.rollback();
            };

            player.deleteRecord();
            player.save().then(function() {}, onFail);
        }
    }
});