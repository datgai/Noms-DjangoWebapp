var weight = document.getElementById('weight');
var height = document.getElementById('height');
var output = document.getElementById("bmiValue")

weight.addEventListener('input',CalculateBMI);
height.addEventListener('input',CalculateBMI);

function CalculateBMI(event) {
    let w = document.getElementById('weight').value;
    let h = document.getElementById('height').value;
    var bmi = w / (Math.pow(h,2));
    output.innerHTML = bmi.toFixed(1);
};
