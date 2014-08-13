App.TournamentController = Ember.ObjectController.extend({
    actions: {
        removeTournament: function() {
            console.log('got it');
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