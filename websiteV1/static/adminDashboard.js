$("#updateInput").on("click", function() {
  var ddid = document.getElementById("updateDD").innerText;

  $("#sensorValue").remove();
  $("#mcValue").remove();

  if (ddid === "Microcontroller") {
    // Add microcontroller name inside a tag bellow
    $("#ddmenu").append(
      '<div id="mcValue">' +
        '<a class="dropdown-item updateInput ddmenu" href="#">Arduino</a>' +
        '<a class="dropdown-item updateInput ddmenu" href="#">Raspberry Pi</a>' +
        "</div>"
    );
  } else {
    // Add sensor name inside a tag bellow
    $("#ddmenu").append(
      '<div id="sensorValue">' +
        '<a class="dropdown-item updateInput ddmenu" href="#">1</a>' +
        '<a class="dropdown-item updateInput ddmenu" href="#">2</a>' +
        '<a class="dropdown-item updateInput ddmenu" href="#">3</a>' +
        '<a class="dropdown-item updateInput ddmenu" href="#">4</a>' +
        "</div>"
    );
  }
  $(".ddmenu").on("click", function() {
    $("#" + this.className.split(" ")[1]).text(this.text);
  });
});

$(".updateDD").on("click", function() {
  $("#updateInputDD").attr("value", this.text);
});

$("#ddmenu").click(function() {
  $("#updateInputValue").attr("value", document.getElementById("updateInput").innerText);
});

$(".dropdown-item").on("click", function() {
  $("#" + this.className.split(" ")[1]).text(this.text);
  $("#"+this.className.split(" ")[2]).val(this.text);
});

$(".apInput").on("click", function() {
  var value = $("#apInput").attr("value");

  if (value == "True") {
    $("#apInput").attr("value", "False");
  } else {
    $("#apInput").attr("value", "True");
  }
});

$(".apuInput").on("click", function() {
  var value = $("#apuInput").attr("value");

  if (value == "True") {
    $("#apuInput").attr("value", "False");
  } else {
    $("#apuInput").attr("value", "True");
  }
});

$(".node-info-table").on("click", function() {
  var nodeID = this.id;
  var nodeData = document.getElementById(nodeID);

  var state = nodeData.cells[3].innerHTML;
  
  if (state == "Active") {
    $("#inState").text(state);
    $("#inState").css("color", "#a1ea11")
  } else {
    $("#inState").text(state);
    $("#inState").css("color", "red")
  }

  $("#inName").text(nodeData.cells[0].innerText);
  $("#inid").text(nodeID);
  $("#inmc").text(nodeData.cells[2].innerText);
  $("#ins1").text(nodeData.cells[4].innerText);
  $("#ins2").text(nodeData.cells[5].innerText);
  $("#ins3").text(nodeData.cells[6].innerText);
  $("#ins4").text(nodeData.cells[7].innerText);
  $("#ins5").text(nodeData.cells[8].innerText);
});
