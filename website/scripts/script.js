function getAllBodyParts(){
    fetch('http://localhost:7777/body_parts/', {method: 'GET'})
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error: ', error));
}


function addHistoryEntry(){
    const bodyPartId = document.getElementById('addHistoryPartId').value;
    const historyDetails = {
        date: new Date().toISOString.split('T')[0],
        notes:document.getElementById('historyNote').value
    };

    fetch('http://localhost:7777/body_parts/history/add/${bodyPartId}', {
        method: 'POST', 
        headers: {'Content-Type' : 'application/json' }, 
        body: JSON.stringify(historyDetails)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert('History added: ' + JSON.stringify(data));
    })
        
    .catch(error => console.error('Error:', error));
}

function updateHistoryEntry(){
    const bodyPartId = document.getElementById('updateHistoryPartId').value;
    const index = document.getElementById('HistoryIndex').value;
    const newHistoryData = {
        notes: document.getElementById('updateHistoryNote').value
    }; 

    fetch('http://localhost:7777/body_parts/history/update/${bodyPartId}',{
        method: 'PUT', 
        headers: { 'Content-Type': 'application/json'},
        body: JSON.stringify({index : index, new_data: newHistoryData})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert('History updated: ' + JSON.stringify(data));
    })
    .catch(error => console.error('Error: ', error));
}

function removeHistoryEntry(){
    const bodyPartId = document.getElementById('removeHisotryPartId').value; 
    const historyDate = document.getElementById('removeHistoryDate').value;

    const entryCriteria = {
        date: historyDate
    };

    fetch('http://localhost:7777/body_parts/history/remove/${bodyPartId}',{
        method: 'POST', 
        headers: { 'Content-Type': 'application/json'},
        body: JSON.stringify(entryCriteria)
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error: ', error));
}


