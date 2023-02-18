var weight = document.getElementById('weight');
var activity = document.getElementById('activitySelect');
var time = document.getElementById("time-input");
var energyHour =document.getElementById("energyHour-input"); 
var energyTotal =document.getElementById("energyTotal-input"); 
var metValue = document.getElementById("metValue");
var loseHalfFat = document.getElementById("loseHalfFat");
var loseFullFat = document.getElementById("loseFullFat");

weight.addEventListener('input',CalculateCalorie);
activity.addEventListener('input',CalculateCalorie);
time.addEventListener('input',CalculateCalorie);
energyHour.addEventListener('input',CalculateCalorie);
energyTotal.addEventListener('input',CalculateCalorie);

function CalculateCalorie(event) {
    // get input
    let w = document.getElementById('weight').value;
    let met = document.getElementById('activitySelect').value;
    let t = document.getElementById("time-input").value;
    let et = document.getElementById("energyTotal-input").value;
    let eh = document.getElementById('energyHour-input').value;

    metValue.innerHTML = "MET : " + met ;

    let calories = (t * 60 * 60) * met * 3.5 * w / (200 * 60);
    energyHour.value = calories;
    energyTotal.value = calories * t;

    let fatHalf = (3500 / calories);
    let fatFull =  (7000 / calories);

    loseHalfFat.innerHTML = "➡️ To lose 0.5 kg of fat, you should perform this activity for " + fatHalf.toFixed(1) + " hours.";
    loseFullFat.innerHTML =  "➡️ To lose 1.0 kg of fat, you should perform this activity for " + fatFull.toFixed(1) + " hours!";

};
