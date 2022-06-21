const previous = document.querySelector('#prev');
const next = document.querySelector('#next');
let api_url = "https://swapi.py4e.com/api/planets/";
let next_url = "";
let previous_url = "";

async function getData(url) {
    const response = await fetch(url);
    let data = await response.json();
    next_url = data['next']
    previous_url = data['previous']
    insertData(data);
}

getData(api_url).then();

next.addEventListener('click', () => {
    if (next_url){
        getData(next_url).then();
    }
});
previous.addEventListener('click', () => {
    if (previous_url) {
        getData(previous_url).then();
    }
});

function insertData(data) {
    let tab = '';
    for (const item of data.results) {
        if (isNaN(item.surface_water)) {
            item.surface_water = 'unknown'
        } else {
            item.surface_water += '%'
        }
        if (isNaN(item.population)) {
            item.population = 'unknown'
        } else {
            item.population = parseFloat(item.population).toLocaleString('en') + ' people'
        }
        if (isNaN(item.diameter)) {
            item.diameter = 'unknown'
        } else {
            item.diameter = parseFloat(item.diameter).toLocaleString('en') + ' km'
        }
        if (item.residents.length <= 0) {
            item.residents = 'No known residents'
        } else {
            item.residents = item.residents.length + " resident(s)"
        }
        tab += "<tr>";
        tab += "<td>" + item.name + "</td>";
        tab += "<td>" + item.diameter +"</td>";
        tab += "<td>" + item.climate + "</td>";
        tab += "<td>" + item.terrain + "</td>";
        tab += "<td>" + item.surface_water + "</td>";
        tab += "<td>" + item.population +"</td>";
        tab += "<td>" + item.residents + "</td>";
}
    document.querySelector('#data').innerHTML = tab;
}
