App.TournamentsController = Ember.ArrayController.extend({
    actions: {
        createTournament: function(params) {
            var participants = this.get('participants');
            var game = this.get('game');
            var description = this.get('description');
            var tournament = this.store.createRecord('tournament', {
                participants: participants,
                game: game,
                description: description
            });

            tournament.save();

//  TODO Validation & clear fields
//            var onFail = function(response) {
//                alert(response.responseText);
//                tournament.rollback();
//            };
//
//            tournament.save().then(function() {}, onFail);
        }
    }
});
