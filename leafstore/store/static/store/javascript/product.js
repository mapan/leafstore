const color_id_to_stock = JSON.parse(
  document.getElementById('color_id_to_stock').textContent);
const color_id_to_pictures = JSON.parse(
  document.getElementById('color_id_to_pictures').textContent);


function setQuantityOptions() {
  var color_id = document.getElementById("color").value;
  if (!(color_id in color_id_to_stock)) {
    document.getElementById("quantity").innerHTML = (
      "<option selected>0</option>");
    document.getElementById('submit').disabled = true;
    return
  }
  var stock = color_id_to_stock[color_id];
  var options = "";
  for (var i = 1; i <= stock; i++) {
    options += "<option>" + i + "</option>"
  }
  document.getElementById("quantity").innerHTML = options;
  document.getElementById('submit').disabled = false;
}

// function verifySelections() {
//   var color_id = document.getElementById("color").value;
//   var quantity = document.getElementById("quantity").value;
//   if (color_id != 'placeholder' && quantity != '0') {
//     document.getElementById('submit').disabled = false;
//   } else {
//     document.getElementById('submit').disabled = true;
//   }
// }


document.getElementById("color").addEventListener(
  "change", () => {
    setQuantityOptions();
    // verifySelections();
  });