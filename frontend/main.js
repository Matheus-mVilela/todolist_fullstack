const listOfTasksURL = "http://0.0.0.0:8000/api/listsoftasks/"

// const newListofTask = {
//     title: "Matheus",
//     start_date: "2021-12-04T18:04:00-03:00",
//     end_date: "2021-12-05T18:35:00-03:00",
//     description: "Test axios",
//     status: "START"
// }

// function postListsOfTasks() {
//     axios.post(url_listsoftasks, newListofTask)
//         .then(response => {
//             const data = response.data
//             console.log(data)
//         })
// }


function feathNavBar() {
    fetch('./navbar.html')
      .then(response => response.text())
      .then(data => {
        document.getElementById('navbar-placeholder').innerHTML = data;
      });
}


function getListsOfTasks() {
    axios.get(listOfTasksURL, {
        headers: {
            'Authorization': 'Token 8189c4a6ce6212c8ac4b653fae48aa47862e818a'
        }
    })
    .then(response => {
        // Get data from endpoint
        const tasks = response.data;

        console.log(response)
        // Select ul on html file
        const taskList = document.getElementById('task-list');

        // Clean the old data on ul
        taskList.innerHTML = '';

        // Iterate over each element of list 
        tasks.forEach(task => {
            const listItem = document.createElement('li');

            // Making a element for list 
            listItem.className = 'list-group-item d-flex justify-content-between align-items-center';
            listItem.textContent = `ID: ${task.id} | Title: ${task.title} | Status:${task.status}`;
            
            // Create the trash icon
            const trashIcon = document.createElement('i');
            trashIcon.className = 'bi bi-trash trash-icon';  // Add custom class for styling

            // Add click event listener to the trash icon
            trashIcon.addEventListener('click', () => {
                // Remove the list item when the icon is clicked
                taskList.removeChild(listItem);
            });

            // Append the trash icon to the list item
            listItem.appendChild(trashIcon);
            
            // Add to list
            taskList.appendChild(listItem);
        });
    })
    .catch(error => {
        // Show error message
        const errorMessage = 'Build lists of task failed'
        console.error(errorMessage, error);
        const errorElement = document.getElementById('error');
        errorElement.textContent = errorMessage;
    });
}

// Called method when page it's loaded
document.addEventListener('DOMContentLoaded', feathNavBar);
document.addEventListener('DOMContentLoaded', getListsOfTasks);
