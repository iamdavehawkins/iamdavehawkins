$(document).ready(function() {
	$('ul.nav li a').click(function() {	
		$('ul.nav li a').filter(function() {
    		return this.href == url;
		}).parent().addClass('active');
	})
})