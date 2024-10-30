// const api = document.getElementById("api");

async function getCustomers(){
    // try {
        const response = await fetch("http://localhost:5000/app/api/v1.0/Customers")
    
        // if(!response.ok){
        //     throw new Error("Could not fetch Customers")
        // }
        // else {
            console.log("Fetched Successfully")
            return await response.json();
        // }
    // } catch (error) {
    //     console.error(error)
    // }
}

// const {"Customers": [[id, name, address]]} = getCustomers()
// console.log(getCustomers())
// console.log(Customer[0][0])

// api.textContent = getCustomers();
console.log(getCustomers()[0])

// fetch("http://localhost:5000/app/api/v1.0/Customers")
//      .then(response => {
//         if(!response.ok){
//             throw new Error("Customers not fetched")
//         }
//         return response.json()})
//     //  .then(data => console.log(data))
//      .catch(error => console.error(error))
// console.log("wetY")

