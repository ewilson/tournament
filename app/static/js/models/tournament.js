App.Tournament = DS.Model.extend({
    participants: DS.attr('string'),
    game: DS.attr('string'),
    description: DS.attr('string')
});

App.Tournament.FIXTURES = [
    {
        id: 1,
        participants: "New Year's party Men",
        game: "Ping-Pong",
        description: "Adults play games while the children roam free"
    },
    {
        id: 2,
        participants: "LEBC",
        game: "Cornhole",
        description: "Summer Social -- eatin' melons and throwing cornbags"
    },
    {
        id: 3,
        participants: "Manta",
        game: "Foosball",
        description: "Mantamurals FTW!"
    }
];