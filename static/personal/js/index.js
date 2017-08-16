
//scrollspy
//$('body').scrollspy({ target: '#sidebar' })
$( document ).ready(function() {
    
    $('body').scrollspy({ target: '#sidebar',offset:80 });
    //$("#tar2").addClass("active");
   // $('#sidebar-wrapper').css('background-color','black');
    console.log( "ready!" );
});