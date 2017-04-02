var employees = [];
var total = {
  employees: 0,
  hours: 0,
  pay: 0
};

function addEmployee() {

  // Get the elements we need
  var tableRef = document.getElementById('employeeTable');
  var totalHoursCell = document.getElementById('totalHoursCell');
  var totalPayCell = document.getElementById('totalPayCell');
  var hoursField = document.getElementById('hoursField');

  // Get the value from the text box and calculate the pay
  var hours = parseInt(hoursField.value, 10);
  var pay;
  if (hours > 40) {
    pay = ((hours - 40) * (15 * 1.5)) + (40 * 15);
  } else {
    pay = hours * 15
  }

  // Calculate the new totals and update the totals row
  total.employees++;
  total.hours += hours;
  total.pay += pay;
  totalHoursCell.innerHTML = total.hours;
  totalPayCell.innerHTML = total.pay;

  // Add a new row to the table with this employee's info
  var newRow = tableRef.insertRow(total.employees);
  var newNumberCell = newRow.insertCell(0);
  var newNumberText = document.createTextNode(total.employees);
  newNumberCell.appendChild(newNumberText);

  var newHoursCell = newRow.insertCell(1);
  var newHoursText = document.createTextNode(hours);
  newHoursCell.appendChild(newHoursText);

  var newPayCell = newRow.insertCell(2);
  var newPayText = document.createTextNode(pay);
  newPayCell.appendChild(newPayText);




}
