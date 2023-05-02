// let _datos = {
//   titulo: "foo",
//   principal: "bar", 
//   Id:1
// }

fetch('http://localhost:3000/customers/10' 
//       {
//   method: "POST",
//   body: JSON.stringify(_datos),
//   headers: {"Content-type": "application/json; charset=UTF-8"}
// }
     )
.then(res => console.log(res.arrayBuffer))
.catch(err => console.log(err));