var $iPhone = $('.iphone');
// Prepare the date
var weekdays = new Array("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday");
var months = new Array("January","February","March","April","May","June","July","August","September","October", "November", "December");
// Updates the date and time
setInterval(function(){
	// Setting the time
	var d = new Date();
	var h = d.getHours();
	var m = ("0" + d.getMinutes()).slice(-2)
	$('.time').html(h+":"+m);
	// Setting the date
	var day = weekdays[d.getDay()];
	var date = d.getDate();
	var month = months[d.getMonth()];
	$('.date').html(day+' '+date+' '+month);
}, 1000);