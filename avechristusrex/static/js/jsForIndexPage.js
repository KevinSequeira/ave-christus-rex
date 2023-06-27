/* ============================================================================== */
/* JavaScript required for Smooth Scrolling                                       */
/* ============================================================================== */

var menubarOpen = 'Yes';
$(document).ready(function () {
    // Add smooth scrolling to all links
	var navBarHeight = $('.navbarTop').height();
	var navBarHeaderHeight = $('.navbar-header').height();
	$("a").on('click', function (event) {

		// Make sure this.hash has a value before overriding default behavior
		if (this.hash !== "") {
			// Prevent default anchor click behavior
			event.preventDefault();

			// Store hash
			var hash = this.hash;

			// Using jQuery's animate() method to add smooth page scroll
			// The optional number (600) specifies the number of milliseconds it takes to scroll to the specified area
			$('html, body').animate({
				 scrollTop: ($(hash).offset().top) - navBarHeight - 2
				}, 600, function () {
				 // Add hash (#) to URL when done scrolling (default click behavior)
				 return window.history.pushState(null, null, hash);
			});
		} // End if
	});

	$('.navbar-background').css('min-height', navBarHeight + 'px');
});

$(window).resize(function(event) {
	// var navBarHeight = $('.navbar-header').height();
	var navbarHeight = $('.navbar-header').outerHeight();
	$('.navbar-background').css('min-height', navbarHeight + 'px');
});

$(function() {
	$('#changeToggle').click(function() {
		$('#navbar-hamburger').toggleClass('hidden');
		$('#navbar-close').toggleClass('hidden');
	});

	var navBarHeight = $('.navbarTop').height();
	document.addEventListener("click", function (event) {
		if (event.target.id == '#dataAnalytics') {
			$('#changeToggle').trigger('click');
			return false;
		};
	});
});
