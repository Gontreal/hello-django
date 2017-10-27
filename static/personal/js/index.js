  /**
   * This object controls the nav bar. Implement the add and remove
   * action over the elements of the nav bar that we want to change.
   *
   * @type {{flagAdd: boolean, elements: string[], add: Function, remove: Function}}
   */
var myNavBar = {
  flagAdd: true,
  elements: [],
  init: function (elements) {
      this.elements = elements;
  },
  add : function() {
    if(this.flagAdd) {
      for(var i=0; i < this.elements.length; i++) {
        document.getElementById(this.elements[i]).className += " fixed-theme";
      }
      this.flagAdd = false;
    }
  },
  remove: function() {
    for(var i=0; i < this.elements.length; i++) {
      document.getElementById(this.elements[i]).className =
        document.getElementById(this.elements[i]).className.replace( /(?:^|\s)fixed-theme(?!\S)/g , '' );
    }
    this.flagAdd = true;
  }
};
/**
 * Function that manage the direction
 * of the scroll
 */
function offSetManager(){
  var yOffset = 0;
  var currYOffSet = window.pageYOffset;

  if(yOffset < currYOffSet) {
    myNavBar.add();
  }
  else if(currYOffSet == yOffset){
    myNavBar.remove();
  }
}
//For django csrf key
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
//$('body').scrollspy({ target: '#sidebar' })
$( document ).ready(function() {
  // Side bar control
  $('body').scrollspy({ target: '#sidebar',offset:200 });
  console.log( "this is personal!" );
  // Contact form ajax 
  $("#contact-form").submit(function(event){
    console.log("email begin")
    var addr = $.trim($("#InputEmail").val());
    var sender = $.trim($("#sender-name").val());
    var tel = $.trim($("#telephone").val());
    var des = $.trim($("#description").val());
    
    //ajax setup
    var frm = $('#contact-form');
    $.ajaxSetup({
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        //contentType: 'application/json'
				}
    });
    $.ajax({
      type: "POST",
      url: frm.attr('action'),
      data: {
        "EmailAddr": addr,
        "senderName": sender,
        "telephone" : tel,
        "Msg" : des
      },
      dataType: 'json',

      success: function(ret){
        console.log("email sent.")
        if(ret.err){
          $('#status-line').text(ret.msg)
        }
        else{
          $('#status-line').text(ret.msg)
        }
      },
      error: function(){
        console.log("email error.")
        $('#status-line').text("Something's wrong sorry")
        
      }
    });
    return false;
  });

  /**
   * Init the object. Pass the object the array of elements
   * that we want to change when the scroll goes down
   */
  myNavBar.init(  [
    "header",
    "header-container",
    "brand"
  ]);
  /**
   * bind to the document scroll detection
   */
  window.onscroll = function(e) {
    offSetManager();
  }
  /**
   * We have to do a first detectation of offset because the page
   * could be load with scroll down set.
   */
  offSetManager();
});
