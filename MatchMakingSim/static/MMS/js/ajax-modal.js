
//Hide the result panel first
$("#result-panel").collapse('toggle');
$( document ).ready(function() {
//If match completed, this signal will disable the start button.
var matchComplete=false
//Reset the whole page
$("#reset-page").click(function(){
  //Restore the start button
  matchComplete=false;
  $('#LaunchSim').prop("disabled",false)
  $('#LaunchSim').button('reset')
  
  //$("#test").html("page reseted.")
  //reset the inputs
  $("#info-form").trigger("reset");
  $('#form-status').remove()
  $("#gender-text").removeClass();
  $("#exAppearenceBox").removeClass("has-error")
  $("#exPersonalityBox").removeClass("has-error")
  $("#exWealthBox").removeClass("has-error")
  $("#exAppearenceBox").removeClass("has-success")
  $("#exPersonalityBox").removeClass("has-success")
  $("#exWealthBox").removeClass("has-success")
  
  $("#appearenceBox").removeClass("has-success");
  $("#personalityBox").removeClass("has-success");
  $("#wealthBox").removeClass("has-success");
  $("#appearenceBox").removeClass("has-error");
  $("#personalityBox").removeClass("has-error");
  $("#wealthBox").removeClass("has-error");
  //Clear the result panel
  $("#logBox").empty();
  $("#result-panel").collapse('hide');
});

$('#exampleModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  //var recipient = button.data('whatever') // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback)
  //Check the input entries are all filled out
  $('#LaunchSim').click(function(){
    var isFormValid=true;
    $("input").each(function(){
      var temp=$.trim($(this).val());
      if(!temp||temp<0||temp>100){
        $(this).parent().parent().addClass("has-error")
        isFormValid=false;
      }
      else{
        $(this).parent().parent().removeClass("has-error")
        //$(this).parent().addClass("has-success")
      }
    });
    if(!isFormValid){
      alert("Numbers filled in should be in 1~100 and not blank.")
      return
    };
    //Check gender radio button is checked
    var gender=$('input[name="inlineRadioOptions"]:checked', '#info-form').val();
    if(!gender){
      alert("TELL ME YOUR GENDER");
      $("#gender-text").addClass("text-danger");
      return
    }
    else{
      $("#gender-text").removeClass("text-danger");
      $("#gender-text").addClass("text-success");
    };
    var appear=$.trim($("#inputAppearence").val());
    var person=$.trim($("#inputPersonality").val());
    var wealth=$.trim($("#inputWealth").val());
    
    var exAppear=$.trim($("#inputExAppear").val()); 
    var exPerson=$.trim($("#inputExPerson").val()); 
    var exWealth=$.trim($("#inputExWealth").val()); 
    $("#appearenceBox").addClass("has-success");
    $("#personalityBox").addClass("has-success");
    $("#wealthBox").addClass("has-success");
    //Check add up to 100
    if(Number(exAppear)+Number(exPerson)+Number(exWealth)!==100){
      $("#exAppearenceBox").addClass("has-error")
      $("#exPersonalityBox").addClass("has-error")
      $("#exWealthBox").addClass("has-error")
      isFormValid=false;
    }
    else{
      $("#exAppearenceBox").removeClass("has-error")
      $("#exPersonalityBox").removeClass("has-error")
      $("#exWealthBox").removeClass("has-error")
      $("#exAppearenceBox").addClass("has-success")
      $("#exPersonalityBox").addClass("has-success")
      $("#exWealthBox").addClass("has-success")
      
    };
    if(!isFormValid){
      alert("The three expectation should add up to 100.")
      return
     }
    //Start the ajax process:calling the server
     $('#LaunchSim').button('loading')
    //$.getJSON("{% url 'ajax-list' %}",function(ret){
      //返回值 ret 在这里是一个列表
      //for (var i = ret.length - 1; i >= 0; i--) {
        // 把 ret 的每一项显示在网页上
        //$('#list_result').append(' ' + ret[i])
      //};
    //})
    //Update the result panel main anchor
    $('#LaunchSim').button('complete')
    $('#logBox').empty()
    $('#ret-msg').text("Here is your result: Appearence: "+appear+",Personality: "+person+",Wealth "+wealth+" gender: "+gender)
    //Update the log list-group
    $('#logBox').append('<li class="list-group-item">'+ exAppear+ '</li>')
    $('#logBox').append('<li class="list-group-item">'+exPerson+ '</li>')
    $('#logBox').append('<li class="list-group-item">'+ exWealth+ '</li>')
    $("#result-panel").collapse('show');
    //Process complete, disable the button
    matchComplete=true;
    $('#exampleModal').modal('hide');   
  });
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this);
  //Disable the start button from lauching another request
  if(matchComplete){
    $('#LaunchSim').prop("disabled",true)
    $('#form-status').html("You've found your match, click reset for another round")
  };
  
  //modal.find('.modal-title').text('Tell me about you ')
  //modal.find('.modal-body input').val(recipient)
});
    //console.log( "ready!" );
});
