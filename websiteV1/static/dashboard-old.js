
// insert django in .append()
// text inside .append() is a HTML line


$(".updateAge").click(function(){
    $(".dropdown-toggle").text("Age");
    $(".updateInput").remove();
    $(".update-form-group").append('<input type="text" class="form-control updateInput" id="updateAge" placeholder="Update Age" name="age">');
});

$(".updateBG").click(function(){
    $(".dropdown-toggle").text("Blood Group");
    $(".updateInput").remove();
    $(".update-form-group").append('<input type="text" class="form-control updateInput" id="updateBG" placeholder="Update Blood Group" name="bg">');
});

$(".updateDescription").click(function(){
    $(".dropdown-toggle").text("Description");
    $(".updateInput").remove();
    $(".update-form-group").append('<input type="text" class="form-control updateInput" id="updateDescription" placeholder="Update Description" name="desc">');
});

// $(".updateFoot").click(function(){
   // $(".dropdown-toggle").text("Select");
    // $(".updateInput").remove();
// });

// Patient Info Modal

$(".patient-info-table").on("click", function() {
    var patientID = this.id;
    var patientData = document.getElementById(patientID);

    $("#patientID").text(patientID);
    $("#name").text(patientData.cells[1].innerText);
    $("#age").text(patientData.cells[2].innerText);
    $("#bloodGroup").text(patientData.cells[3].innerText);
    // Insert description via django below inside quotation marks
    var description = 'default';
    for (patient in patientData.cells[4])
        if(patient.id === patientID)
            description = patient.desc;

    $("desc").text(description.toString);
});