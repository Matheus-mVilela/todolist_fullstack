const url_listsoftasks = "http://0.0.0.0:8000/api/listsoftasks/"

const newListofTask = {
    title: "Matheus",
    start_date: "2021-12-04T18:04:00-03:00",
    end_date: "2021-12-05T18:35:00-03:00",
    description: "Test axios",
    status: "START"
}

function getListsOfTasks() {
    axios.get(url_listsoftasks)
        .then(response => {
            const data = response.data
            console.log(data)
            renderResults.textContent = JSON.stringify(data)
        })
}

function postListsOfTasks() {
    axios.post(url_listsoftasks, newListofTask)
        .then(response => {
            const data = response.data
            console.log(data)
        })
}


