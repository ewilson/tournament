App.Player = DS.Model.extend({
    fname: DS.attr('string')
});

App.Player.FIXTURES = [
    {"id": 1, "fname": "Abraham"},
    {"id": 2, "fname": "Barnabas"},
    {"id": 3, "fname": "Caiphas"},
    {"id": 4, "fname": "Dionysius"},
    {"id": 5, "fname": "Ezekiel"}
];
