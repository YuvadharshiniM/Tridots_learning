const api = "https://jsonplaceholder.typicode.com/users";
async function getStudents(){
    try{
        const resposne = await fetch(api);
        if(!resposne.ok){
            throw new Error("Failed to ftech students");
        }
        const students = await resposne.json();
        console.log("Students List");
        studens.forEach(student =>{
            console.log("ID: ",student.id);
            console.log("Name: ",student.name);
            console.log("Email: ",student.email);
            console.log("--------------------------");
        });

    }catch(error){
        console.log(error.message);
    }
}


async function addStudent(){
    try{
        const newStudent = {
            name: "Yuvadharshini",
            email: "yuva@gamil.com",
            department: "IT"
        };
        const response = await fetch(api, {
            method:"POST",
            headers:{
                "content-Type" : "application/json"
            } ,
            body: JSON.stringify(newStudent)
        });
        if(!response.ok){
            throw new Error("Failed to add student");
        }
        const student  = await response.json();
        console.log("New Student Added");
        console.log(student);
    }catch(error){
        console.log(error.message);
    }
}


async function updateStudent(){
    try{
        const updateStudent={
            id:1,
            name : "Yuva",
            email: "yuva2005@gmail.com",
            department: "CSE"
        };
        const response = await fetch(`${api}/1`, {
            method:"PUT",
            headers: {
                "content-Type" : "application/json"
            } ,
            body : JSON.stringify(upadateStudent)
        });
        if(!response.ok){
            throw new Error("Failed to upadte student");
        }
    }catch(error){
        console.log(error.message);
    }
}