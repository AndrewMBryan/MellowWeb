


// function data(){
// fetch("https://api.apispreadsheets.com/data/11326/").then(res=>{
// 	if (res.status === 200){
// 		// SUCCESS
//     console.log('succ')
// 		res.json().then(data=>{
// 			const yourData = data
//       //return yourData;
// 		}).catch(err => console.log(err))
// 	}
// 	else{
// 		// ERROR
// 	}
// })
// };
//AIzaSyB1sKD7DKwC9Kg3pMZwhlBenRYVqjDGHtI
var theData = {};
async function data(){
  const response = await fetch("https://api.apispreadsheets.com/data/11326/").then(function(response) {
    response.text().then(function(text) {
      console.log("This is " + text);
      theData = text;
    })
  })
  return response;
}
 theData = data();

function check(){
    //data().then(text => {text;});
    console.log(theData[0]);
}
