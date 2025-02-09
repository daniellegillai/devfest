function getAllBodyParts(){
    fetch('http://localhost:7777/body_parts/', {method: 'GET'})
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error: ', error));
}


function addHistoryEntry() {
    const bodyPartId = document.getElementById('addHistoryPartId').value;
    const eventDescription = document.getElementById('addHistoryPartId').value;
    const historyDetails = {
        date: date,
        event: eventDescription
    };

    fetch(`http://localhost:7777/body_parts/history/add/${bodyPartId}`, { 
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(historyDetails)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            console.log('History added successfully:', data);
            alert('History added successfully: ' + data.message);
        } else {
            throw new Error('Failed to add history: ' + (data.error || 'Unknown error'));
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error adding history: ' + error.message);
    });
}



function updateHistoryEntry() {
    const bodyPartId = document.getElementById('updateHistoryPartId').value;
    const index = document.getElementById('historyIndex').value;
    const newHistoryData = {
        notes: document.getElementById('updateHistoryNote').value
    };

    fetch(`http://localhost:7777/body_parts/history/update/${bodyPartId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ index: index, new_data: newHistoryData })
    })
    .then(response => {
        if (response.ok) {
            return response.json();  // Only parse JSON if the response is OK.
        } else {
            throw new Error('Failed to update history. Status: ' + response.status);
        }
    })
    .then(data => {
        console.log('History updated successfully:', data);  // Detailed log for debugging
        alert('History updated successfully: ' + JSON.stringify(data));
    })
    .catch(error => {
        console.error('Error updating history:', error);  // Detailed error logging
        alert('Error updating history: ' + error.message);
    });
}


function removeHistoryEntry() {
    const bodyPartId = document.getElementById('removeHistoryPartId').value;  // Corrected typo in ID
    const historyDate = document.getElementById('removeHistoryDate').value;

    const entryCriteria = {
        date: historyDate
    };

    fetch(`http://localhost:7777/body_parts/history/remove/${bodyPartId}`, {  // Corrected the template literal
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(entryCriteria)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if(data.message) {
            alert('History entry removed successfully');
        } else {
            throw new Error('Failed to remove history entry');
        }
    })
    .catch(error => console.error('Error:', error));
}



