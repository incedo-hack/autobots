$('.mytr').click(function(){
   var a = $(this).children('td:first').text();
   window.location = "dashboard.html?id=" + a +"&lt_1mth_check=on";
 });