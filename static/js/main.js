function updateDate() {
  var date = new Date();
  var day = date.getDate();
  var month = date.getMonth() + 1;
  var year = date.getFullYear();
  var displayDate = day + "-" + month + "-" + year;
  var dateDiv = document.getElementById("dateDiv");
  dateDiv.innerText = displayDate;
  return displayDate;
}
updateDate();

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function round(value, precision) {
  var multiplier = Math.pow(10, precision || 0);
  return Math.round(value * multiplier) / multiplier;
}

async function runMeter(n) {
  let i = 0.0;
  let readingDiv = document.getElementById("readingDiv");
  setInterval(() => (readingDiv.style.display = ""), 1000);
  let reading = document.getElementById("reading");
  time = 1000;
  while (i < n) {
    // console.log(i);
    await sleep(time);
    reading.innerText = i + " L";
    i += 0.4;
    i = round(i, 1);
    // time-=50;
  }
  reading.innerText = n + " L";
}

// var submitBtn = document.getElementById("submit");

function ajaxSend(data) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      console.log("Succesfully Sent!");
    }
  };
  xhttp.open("POST", "/recieve_data", true);
  //   console.log(data);
  xhttp.send(data);
}
function setDataSum(){
  var totalDiv = document.getElementById("totalDiv");
  var totalEntered = document.getElementById("inputAmount").value;

  var totalActual = totalDiv.innerText;
  var date = new Date();
  var day = date.getDate();
  var month = date.getMonth() + 1;
  var year = date.getFullYear();
  var displayDate = day + "-" + month + "-" + year;

  $.ajax({
    url:'/get_sum',
    type:"POST",
    async:false,
    headers:{
      "Content-Type":"application/json"
    },
    data:JSON.stringify({date:displayDate}),
    success:function(r){
      console.log(r);

      totalDiv.innerText=r;
    },error:function(e){
      console.log(e);
    }
  });
}
async function submit() {
//  setDataSum();
  var totalEntered = document.getElementById("inputAmount").value;
var email = document.getElementById("email").value;

  // if (totalActual == "") {
  //   totalDiv.innerText = totalEntered;
  // } else {
  //   totalActual = parseFloat(totalActual);
  //   totalEntered = parseFloat(totalEntered);
  //   n = ((totalActual + totalEntered)/72.5);
  //   totalDiv.innerText = n.toFixed(2);
  // }
  var curPrice = parseFloat(document.getElementById("curPrice").innerText);
  // console.log(curPrice);
  var petrol = round(parseFloat(totalEntered) / curPrice, 2);
  // console.log(petrol);
  //   var data = { date: updateDate(), entered_amount: petrol };
  var data = new FormData();
  data.append("date", updateDate());
  data.append("entered_amount", petrol);
data.append("email",email);
  ajaxSend(data);
 await runMeter(petrol);

}

// let n = prompt("Enter the Reading!");
// display(parseFloat(n));
