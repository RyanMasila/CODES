// async function getCustomers(){
//     const response = await fetch("http://localhost:5000/app/api/v1.0/Customers");
//     return await response.json();
// }
const api = document.getElementById("api");
fetch("http://localhost:5000/app/api/v1.0/Customers")
     .then(response => response.json())
     .then(data => {
        // for(let i = 1; i <= data.length; i++){
        //     console.log(data[i]);
        const [id, name, address] = data[6];
        api.textContent = name;
        }
        
    )

// console.log(getCustomers()[0])