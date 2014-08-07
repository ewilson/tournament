App.PlayerController = Ember.ObjectController.extend({
    actions: {
        removePlayer: function() {
            var player = this.get('model');
            player.deleteRecord();
            player.save();
        }
    }
});