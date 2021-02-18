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

	$('.navbar-background').css('min-height', navBarHeight + 2 + 'px');
});

$(window).resize(function(event) {
	// var navBarHeight = $('.navbar-header').height();
	var navbarHeight = $('.navbar-header').outerHeight();
	$('.navbar-background').css('min-height', navbarHeight + 2 + 'px');
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

	$('.startSurveyButton').click(function() {
		$(".surveySectOne").css('visibility', 'visible').animate({opacity: 1}, 1000);
	});
});

function clickRBSurvey(ele) {
	var rBChoice = ele.value;
	if (rBChoice == "Yes") {
		$(".sSQ002").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else if (rBChoice == "No") {
		$(".sSQ002").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	}
};

function clickBirthCountry(ele) {
	var birthCountry = ele.innerText;
	$('.sSQ003DropdownButton').text(birthCountry);
	$('.sSQ004DropdownButton').text("Select state" + '   ▾');

	$.ajax({
		url: '/surveys/countryFrom/'+ birthCountry,
		type: 'GET',
		cache: true,
		success: function (data) {
			console.log(data)
			$("#sSQ004DropdownOption").html(data);
		},
		error: function (data) {
			console.log('Error: ' + data.responseText);
		}
	});
}

function clickBirthState(ele) {
	var birthState = ele.innerText;
	$('.sSQ004DropdownButton').text(birthState);
}

function clickLiveCountry(ele) {
	var liveCountry = ele.innerText;
	$('.sSQ005DropdownButton').text(liveCountry);
	$('.sSQ006DropdownButton').text("Select state" + '  ▾');

	$.ajax({
		url: '/surveys/countryIn/'+ liveCountry,
		type: 'GET',
		cache: true,
		success: function (data) {
			console.log(data)
			$("#sSQ006DropdownOption").html(data);
		},
		error: function (data) {
			console.log('Error: ' + data.responseText);
		}
	});
}

function clickLiveState(ele) {
	var liveState = ele.innerText;
	$('.sSQ006DropdownButton').text(liveState);
}

function clickRBLocalParish(ele) {
	var rBLocalParish = ele.value;
};

function clickRBVisitParish(ele) {
	var rBVisitParish = ele.value;
};

function clickNoOfPriests(ele) {
	var noOfPriests = ele.innerText;
	$('.sSQ009DropdownButton').text(noOfPriests);
}

function clickNoOfParishioners(ele) {
	var noOfParishioners = ele.innerText;
	$('.sSQ010DropdownButton').text(noOfParishioners);
}

function clickRBBaptism(ele) {
	var rBBaptism = ele.value;
	if (rBBaptism == "Cradle") {
		$(".sSQ012").css('display', 'none').css('visibility', 'hidden').animate({opacity: 1}, 1000);
		$(".sSQ013").css('display', 'none').css('visibility', 'hidden').animate({opacity: 1}, 1000);
		$(".sSQ014").css('display', 'none').css('visibility', 'hidden').animate({opacity: 1}, 1000);
		$(".sSQ015").css('display', 'none').css('visibility', 'hidden').animate({opacity: 1}, 1000);
	} else if (rBBaptism == "Convert") {
		$(".sSQ012").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ013").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ014").css('display', 'none').css('visibility', 'hidden').animate({opacity: 1}, 1000);
		$(".sSQ015").css('display', 'none').css('visibility', 'hidden').animate({opacity: 1}, 1000);
	}
	else if (rBBaptism == "Revert") {
		$(".sSQ012").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ013").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ014").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ015").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	}
};

function clickReligion(ele) {
	var religion = ele.innerText;
	$('.sSQ013DropdownButton').text(religion);
}

function clickRite(ele) {
	var rite = ele.innerText;
	$('.sSQ016DropdownButton').text(rite);
}

function clickNoOfMassDays(ele) {
	var noOfMassDays = ele.innerText;
	$('.sSQ017DropdownButton').text(noOfMassDays);
}

function clickLanguage_a(ele) {
	var languageA = ele.innerText;
	$('.sSQ018DropdownButton_a').text(languageA);
	$('.sSQ018DropdownButton_b').removeAttr("disabled");
}

function clickLanguage_b(ele) {
	var languageB = ele.innerText;
	if (languageB != "No second language") {
		$('.sSQ018DropdownButton_b').text(languageB);
		$('.sSQ018DropdownButton_c').removeAttr("disabled");
	} else if (languageB == "No second language") {
		$('.sSQ018DropdownButton_b').text("Second language  ▾");
		$('.sSQ018DropdownButton_c').attr("disabled", "true");
	}
}

function clickLanguage_c(ele) {
	var languageC = ele.innerText;
	if (languageC != "No third language") {
		$('.sSQ018DropdownButton_c').text(languageC);
		// $('.sSQ018DropdownButton_c').removeAttr("disabled");
	} else if (languageC == "No third language") {
		$('.sSQ018DropdownButton_c').text("Third language  ▾");
		// $('.sSQ018DropdownButton_c').attr("disabled", "true");
	}
}

function clickTLMFrequency (ele) {
	var noOfTLM = ele.innerText;
	$('.sSQ021DropdownButton').text(noOfTLM);
}

function clickTLMIntro (ele) {
	var tlmIntro = ele.innerText;
	$('.sSQ023DropdownButton').text(tlmIntro);
}
