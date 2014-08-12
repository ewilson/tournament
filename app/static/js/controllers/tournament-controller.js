App.TournamentController = Ember.ObjectController.extend({
    actions: {
        removeTournament: function() {
            var tournament = this.get('model');

            var onFail = function(response) {
                alert(response.responseText);
                tournament.rollback();
            };

            tournament.deleteRecord();
            tournament.save().then(function() {}, onFail);
        }
    }
});