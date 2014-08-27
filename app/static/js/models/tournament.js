App.Tournament = DS.Model.extend({
    group: DS.attr('string'),
    event: DS.attr('string'),
    description: DS.attr('string')
});

App.Tournament.FIXTURES = [
    {
        id: 1,
        group: "New Year's party Men",
        event: "Ping-Pong",
        description: "Adults play games while the children roam free"
    },
    {
        id: 2,
        group: "LEBC",
        event: "Cornhole",
        description: "Summer Social -- eatin' melons and throwing cornbags"
    },
    {
        id: 3,
        group: "Manta",
        event: "Foosball",
        description: "Mantamurals FTW!"
    }
];