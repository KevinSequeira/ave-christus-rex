/* ============================================================================== */
/* JavaScript required for Smooth Scrolling                                       */
/* ============================================================================== */

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

// Capture the response to .sSQ009
function clickPrayerLanguage(ele) {
	var prayerLanguage = ele.innerText;
	var prayerValue = "#" + ele.getAttribute("value");
	// alert(prayerValue);
	$('.prayTabDropdownButton').text(prayerLanguage);
	if (prayerLanguage == "All Languages") {
		$('.prayTabBodyTranslation').each(function(i, obj) {
			$(obj).css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		});

	} else {
		$('.prayTabBodyTranslation').each(function(i, obj) {
			$(obj).css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 0);
		});
		$(prayerValue).css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	}
}
