const color_id_to_quantity = JSON.parse(
  document.getElementById('color_id_to_quantity').textContent);
const color_id_to_pictures = JSON.parse(
  document.getElementById('color_id_to_pictures').textContent);
console.log(color_id_to_pictures)

function setQuantityOptions() {
  var color_id = document.getElementById("color").value;
  if (!(color_id in color_id_to_quantity)) {
    document.getElementById("quantity").innerHTML = (
      "<option selected>0</option>")
    return
  }
  var quantity = color_id_to_quantity[color_id];
  var options = "";
  for (var i = 1; i <= new Array(quantity).length; i++) {
    options += "<option>" + i + "</option>"
  }
  document.getElementById("quantity").innerHTML = options;
}


setQuantityOptions();
document.getElementById("color").addEventListener(
  "change", setQuantityOptions);