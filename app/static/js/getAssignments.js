

$("#getAssignBtn").click(function(){
    $.getJSON("'https://canvas.instructure.com/api/v1/'")
    .done(function(data){
        console.log(data);
    })
    .fail(function(){
        console.log("Problem. Can't get the data.")
    })
});