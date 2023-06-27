/* ============================================================================== */
/* JavaScript required for Smooth Scrolling                                       */
/* ============================================================================== */

var menubarOpen = 'Yes';

var parishMusicTypes = [];
var musicPersonalPreference = [];
var altarServers = [];
var lectors = [];
var reasonNoTongue = [];
var reasonNoKneeling = [];
var reasonNoExtraOrdMinister = [];
var confessionDays = [];
var reasonNotConfess = [];

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

	$('.startSurveyButton').click(function() {
		$(".surveySectOne").css('visibility', 'visible').animate({opacity: 1}, 1000);
	});
});

// Show or remove .sSQ002 based on response to .sSQ001
function clickRBSurvey(ele) {
	rBChoice = ele.value;
	if (rBChoice == "Yes") {
		$(".sSQ002").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else if (rBChoice == "No") {
		$(".sSQ002").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	}
};

// Get list of states to be shown in .sSQ004 based on response to .sSQ003
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
};

// Get the value of the state selected as response to .sSQ004
function clickBirthState(ele) {
	var birthState = ele.innerText;
	$('.sSQ004DropdownButton').text(birthState);
}

// Get list of states to be shown in .sSQ006 based on response to .sSQ005
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
};

// Get the value of the state selected as response to .sSQ006
function clickLiveState(ele) {
	var liveState = ele.innerText;
	$('.sSQ006DropdownButton').text(liveState);
}

// Capture the response to .sSQ007
function clickRBLocalParish(ele) {
	var rBLocalParish = ele.value;
}

// Capture the response to .sSQ008
function clickRBVisitParish(ele) {
	var rBVisitParish = ele.value;
}

// Capture the response to .sSQ009
function clickNoOfPriests(ele) {
	var noOfPriests = ele.innerText;
	$('.sSQ009DropdownButton').text(noOfPriests);
}

// Capture the response to .sSQ009
function clickPrayerDropdown(ele) {
	$('.sSQ009DropdownButton').text(noOfPriests);
}


// Capture the response to .sSQ009
function clickPrayerLanguage(ele) {
	var prayerLanguage = ele.innerText;
	$('.prayTabDropdownButton').text(prayerLanguage);
	if (prayerLanguage == "All Languages") {
		$("#prayerHindi").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$("#prayerDeutsch").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$("#prayerEspanol").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$("#prayerFrancais").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$("#prayerGaeilge").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$("#prayerItaliano").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$("#prayerPolskie").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$("#prayerPortugues").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else if (prayerLanguage == "हिन्दी (Hindi)") {
		$("#prayerHindi").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$("#prayerDeutsch").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerEspanol").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerFrancais").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerGaeilge").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerItaliano").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerPolskie").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerPortugues").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	} else if (prayerLanguage == "Deutsch (German)") {
		$("#prayerHindi").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerDeutsch").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$("#prayerEspanol").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerFrancais").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerGaeilge").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerItaliano").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerPolskie").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerPortugues").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	} else if (prayerLanguage == "Español (Spanish)") {
		$("#prayerHindi").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerDeutsch").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerEspanol").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$("#prayerFrancais").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerGaeilge").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerItaliano").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerPolskie").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerPortugues").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	} else if (prayerLanguage == "Français (French)") {
		$("#prayerHindi").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerDeutsch").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerEspanol").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerFrancais").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$("#prayerGaeilge").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerItaliano").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerPolskie").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerPortugues").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	} else if (prayerLanguage == "Gaeilge (Irish)") {
		$("#prayerHindi").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerDeutsch").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerEspanol").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerFrancais").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerGaeilge").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$("#prayerItaliano").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerPolskie").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerPortugues").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	} else if (prayerLanguage == "Italiano (Italian)") {
		$("#prayerHindi").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerDeutsch").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerEspanol").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerFrancais").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerGaeilge").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerItaliano").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$("#prayerPolskie").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerPortugues").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	} else if (prayerLanguage == "Polskie (Polish)") {
		$("#prayerHindi").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerDeutsch").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerEspanol").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerFrancais").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerGaeilge").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerItaliano").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerPolskie").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$("#prayerPortugues").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	} else if (prayerLanguage == "Português (Portuguese)") {
		$("#prayerHindi").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerDeutsch").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerEspanol").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerFrancais").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerGaeilge").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerItaliano").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerPolskie").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$("#prayerPortugues").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	}
}

// Capture the response to .sSQ010
function clickNoOfParishioners(ele) {
	var noOfParishioners = ele.innerText;
	$('.sSQ010DropdownButton').text(noOfParishioners);
}

// Hide or show .sSQ012, .sSQ013, .sSQ014 and .sSQ015 based on response to .sSQ011
function clickRBBaptism(ele) {
	var rBBaptism = ele.value;
	if (rBBaptism == "Cradle") {
		$(".sSQ012").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ013").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ014").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ015").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	} else if (rBBaptism == "Convert") {
		$(".sSQ012").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ013").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ014").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ015").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	}
	else if (rBBaptism == "Revert") {
		$(".sSQ012").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ013").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ014").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ015").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	}
}

// Capture response for .sSQ013
function clickReligion(ele) {
	var religion = ele.innerText;
	$('.sSQ013DropdownButton').text(religion);
}

// Capture response for .sSQ016
function clickRite(ele) {
	var rite = ele.innerText;
	$('.sSQ016DropdownButton').text(rite);
}

// Capture response for .sSQ017
function clickNoOfMassDays(ele) {
	var noOfMassDays = ele.innerText;
	$('.sSQ017DropdownButton').text(noOfMassDays);
}

// Capture response for .sSQ018 - first language and enable second language
// dropdown
function clickLanguage_a(ele) {
	var languageA = ele.innerText;
	$('.sSQ018DropdownButton_a').text(languageA);
	$('.sSQ018DropdownButton_b').removeAttr("disabled");
}

// Capture response for .sSQ018 - second language and enable or disable third
// language dropdown based on response
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

// Capture response .sSQ019 - third language
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

// Capture the response to .sSQ019
function clickMassNativeTongue(ele) {
	var rBMassNativeTonuge = ele.value;
}

// Capture the response to .sSQ020
function clickMassBefore0900(ele) {
	var rBMassBeforeNine = ele.value;
}

// Capture the response to .sSQ021
function clickMassAfter1700(ele) {
	var rBMassAfterFive = ele.value;
}

// Capture the response to .sSQ022
function clickDailyMassFrequency(ele) {
	var noOfMassesPerDay = ele.innerText;
	$('.sSQ022DropdownButton').text(noOfMassesPerDay);
}

// Capture the response to .sSQ023
function clickTLMAwareness(ele) {
	var rBTLMAwareness = ele.value;
	if (rBTLMAwareness == "Yes") {
		$(".sSQ026").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ024").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ030").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ025").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ027").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ028").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ029").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else if (rBTLMAwareness == "No") {
		$(".sSQ026").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ024").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ030").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ025").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ027").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ028").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ029").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	}
}

// Capture the response to .sSQ026
function clickTLMIntro(ele) {
	var tlmIntroduction = ele.innerText;
	$('.sSQ026DropdownButton').text(tlmIntroduction);
}

// Capture the response to .sSQ024
function cliclParishesTLM(ele) {
	var rBParishesTLM = ele.value;
}

// Capture the response to .sSQ030
function clickTLMFrequency(ele) {
	var tlmFrequency = ele.innerText;
	$('.sSQ030DropdownButton').text(tlmFrequency);
}

// Capture the response to .sSQ025
function clickSungLatinMass(ele) {
	var rBSungLatinMass = ele.value;
}

// Capture the response to .sSQ027
function clickTLMAttendFrequency(ele) {
	var tlmAttendFrequency = ele.innerText;
	$('.sSQ027DropdownButton').text(tlmAttendFrequency);
}

// Capture the response to .sSQ028
function clickRBOwnLatinMissal(ele) {
	var rBOwnLatinMissal = ele.value;
}

// Capture the response to .sSQ029
function clickRBLatinTranslation(ele) {
	var rBLatinTranslation = ele.value;
}

// Capture responses to .sSQ031
function clickParishMusicType(ele) {
	if (parishMusicTypes.includes(ele.value)) {
		parishMusicTypes.splice(parishMusicTypes.indexOf(ele.value), 1)
		alert(parishMusicTypes);
	} else {
		parishMusicTypes.push(ele.value);
		alert(parishMusicTypes);
	}
	if (parishMusicTypes.includes("Modern_Voices")
		|| parishMusicTypes.includes("Modern_Electronic")
		|| parishMusicTypes.includes("Modern_Wind")) {
		$(".sSQ032").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ039").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else {
		$(".sSQ032").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ039").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	}
}

// Capture the response to .sSQ032
function clickRBParishMusicPreference(ele) {
	var rBParishMusicPreference = ele.value;
}

// Capture the response to .sSQ039
function clickRBIsMusicAppropriate(ele) {
	var rBIsMusicAppropriate = ele.value;
}

// Capture the response to .sSQ033
function clickIsMusicDistracting(ele) {
	var isMusicDistracting = ele.innerText;
	$('.sSQ033DropdownButton').text(isMusicDistracting);
}

// Capture responses to .sSQ034
function clickMusicPersonalPreference(ele) {
	if (musicPersonalPreference.includes(ele.value)) {
		musicPersonalPreference.splice(musicPersonalPreference.indexOf(ele.value), 1)
		alert(musicPersonalPreference);
	} else {
		musicPersonalPreference.push(ele.value);
		alert(musicPersonalPreference);
	}
}

// Capture the response to .sSQ035
function clickRBParishHasChoir(ele) {
	var rBParishHasChoir = ele.value;
	if (rBParishHasChoir == "Yes") {
		$(".sSQ036").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else if (rBParishHasChoir == "No") {
		$(".sSQ036").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	}
}

// Capture the response to .sSQ036
function clickRBChoirAllSundays(ele) {
	var rBChoirOnAllSundays = ele.value;
}

// Capture the response to .sSQ037
function clickRBParishHasCantor(ele) {
	var rBParishHasCantor = ele.value;
	if (rBParishHasCantor == "Yes") {
		$(".sSQ038").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else if (rBParishHasCantor == "No") {
		$(".sSQ038").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	}
}

// Capture the response to .sSQ038
function clickRBCantorAllMasses(ele) {
	var rBCantorAtAllMasses = ele.value;
}

// Capture the response to .sSQ040
function clickRBMinorOrderAwareness(ele) {
	var rBMinorOrderAwareness = ele.value;
}

// Capture the response to .sSQ041
function clickRBAltarServersSunday(ele) {
	var rBAltarServersSunday = ele.value;
	if (rBAltarServersSunday == "Yes") {
		$(".sSQ042").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		altarServers.push("altarServersSunday");
	} else if (rBAltarServersSunday == "No") {
		$(".sSQ042").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		if (altarServers.includes("altarServersSunday")) {
			altarServers.splice(altarServers.indexOf("altarServersSunday"), 1);
		}
	}
	if (altarServers.length == 0) {
		$(".sSQ045").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	} else {
		$(".sSQ045").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	}
}

// Capture the response to .sSQ042
function clickRBAltarServersSundayAll(ele) {
	var rBAltarServersSundayAll = ele.value;
}

// Capture the response to .sSQ043
function clickRBAltarServersWeekdays(ele) {
	var rBAltarServersWeekday = ele.value;
	if (rBAltarServersWeekday == "Yes") {
		$(".sSQ044").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		altarServers.push("altarServersWeekday");
	} else if (rBAltarServersWeekday == "No") {
		$(".sSQ044").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		if (altarServers.includes("altarServersWeekday")) {
			altarServers.splice(altarServers.indexOf("altarServersWeekday"), 1);
		}
	}
	if (altarServers.length == 0) {
		$(".sSQ045").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	} else {
		$(".sSQ045").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	}
}

// Capture the response to .sSQ044
function clickRBAltarServersWeekdaysAll(ele) {
	var rBAltarServersSundayAll = ele.value;
}

// Capture the response to .sSQ045
function clickRBAltarServerGirls(ele) {
	var rBAltarServerGirls = ele.value;
}

// Capture the response to .sSQ046
function clickRBLectorsSundays(ele) {
	var rBLectorsSundays = ele.value;
	if (rBLectorsSundays == "Yes") {
		$(".sSQ047").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		lectors.push("lectorsSunday");
	} else if (rBLectorsSundays == "No") {
		$(".sSQ047").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		if (lectors.includes("lectorsSunday")) {
			lectors.splice(lectors.indexOf("lectorsSunday"), 1);
		}
	}
	if (lectors.length == 0) {
		$(".sSQ050").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	} else {
		$(".sSQ050").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	}
}

// Capture the response to .sSQ047
function clickRBLectorsAllSundays(ele) {
	var rBLectorsAllSundays = ele.value;
}

// Capture the response to .sSQ048
function clickRBLectorsWeekdays(ele) {
	var rBLectorsWeekdays = ele.value;
	if (rBLectorsWeekdays == "Yes") {
		$(".sSQ049").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		lectors.push("lectorsWeekday");
	} else if (rBLectorsWeekdays == "No") {
		$(".sSQ049").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		if (lectors.includes("lectorsWeekday")) {
			lectors.splice(lectors.indexOf("lectorsWeekday"), 1);
		}
	}
	if (lectors.length == 0) {
		$(".sSQ050").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	} else {
		$(".sSQ050").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	}
}

// Capture the response to .sSQ049
function clickRBLectorsAllWeekdays(ele) {
	var rBLectorsAllWeekdays = ele.value;
}

// Capture the response to .sSQ050
function clickRBLectorsWomen(ele) {
	var rBLectorsWomen = ele.value;
}

// Capture the response to .sSQ051
function clickRBCommunionOnTongue(ele) {
	var rBCommunionOnTongue = ele.value;
	if (rBCommunionOnTongue == "No") {
		$(".sSQ053").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else if (rBCommunionOnTongue == "Yes") {
		$(".sSQ053").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	}
}

// Capture the response to .sSQ052
function clickRBCommunionKneeling(ele) {
	var rBCommunionKneeling = ele.value;
	if (rBCommunionKneeling == "No") {
		$(".sSQ054").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else if (rBCommunionKneeling == "Yes") {
		$(".sSQ054").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	}
}

// Capture the response to .sSQ053
function clickReasonNoTongue(ele) {
	if (reasonNoTongue.includes(ele.value)) {
		reasonNoTongue.splice(reasonNoTongue.indexOf(ele.value), 1)
		alert(reasonNoTongue);
	} else {
		reasonNoTongue.push(ele.value);
		alert(reasonNoTongue);
	}
}

// Capture the response to .sSQ054
function clickReasonNoKneeling(ele) {
	if (reasonNoKneeling.includes(ele.value)) {
		reasonNoKneeling.splice(reasonNoKneeling.indexOf(ele.value), 1)
		alert(reasonNoKneeling);
	} else {
		reasonNoKneeling.push(ele.value);
		alert(reasonNoKneeling);
	}
}

// Capture the response to .sSQ055
function clickRBEncourageOnTongue(ele) {
	var rBEncourageOnTongue = ele.value;
}

// Capture the response to .sSQ056
function clickRBDiscourageOnTongue(ele) {
	var rBDiscourageOnTongue = ele.value;
}

// Capture the response to .sSQ057
function clickRBEncourageKneeling(ele) {
	var rBEncourageKneeling = ele.value;
}

// Capture the response to .sSQ058
function clickRBDiscourageKneeling(ele) {
	var rBDiscourageKneeling = ele.value;
}

// Capture the response to .sSQ060
function clickRBParishExtaordinaryMin(ele) {
	var rBParishExtaordinaryMin = ele.value;
	if (rBParishExtaordinaryMin == "Yes") {
		$(".sSQ061").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else if (rBParishExtaordinaryMin == "No") {
		$(".sSQ061").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ062").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	}
}

// Capture the response to .sSQ061
function clickRBReceiveFromExtaordinaryMin(ele) {
	var rBReceiveFromExtaordinaryMin = ele.value;
	if (rBReceiveFromExtaordinaryMin == "No") {
		$(".sSQ062").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else if (rBReceiveFromExtaordinaryMin == "Yes") {
		$(".sSQ062").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	}
}

// Capture the response to .sSQ062
function clickReasonNoKneeling(ele) {
	if (reasonNoExtraOrdMinister.includes(ele.value)) {
		reasonNoExtraOrdMinister.splice(reasonNoExtraOrdMinister.indexOf(ele.value), 1)
		alert(reasonNoExtraOrdMinister);
	} else {
		reasonNoExtraOrdMinister.push(ele.value);
		alert(reasonNoExtraOrdMinister);
	}
}

// Capture the response to .sSQ063
function clickRBReconciliationAware(ele) {
	var rBReconcilationAware = ele.value;
}

// Capture the response to .sSQ073
function clickRBVenialMortalAware(ele) {
	var rBVenialMortalAware = ele.value;
}

// Capture the response to .sSQ064
function clickParishConfessFrequency(ele) {
	var parishConfessFrequency = ele.innerText;
	$('.sSQ064DropdownButton').text(parishConfessFrequency);
	if ((parishConfessFrequency != "Less than once a month")
		&& (parishConfessFrequency != "At least once a month")
		&& (parishConfessFrequency != "At least once a day")) {
		$(".sSQ065").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ066").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ067").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ068").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ069").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else if (parishConfessFrequency == "At least once a month") {
		$(".sSQ065").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ065").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ067").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ068").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ069").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else if (parishConfessFrequency == "At least once a day") {
		$(".sSQ065").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ066").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ067").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ068").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ069").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else {
		$(".sSQ065").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ066").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ067").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ068").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ069").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
	}
}

// Capture the response to .sSQ065
function clickConfessionOnDays(ele) {
	if (confessionDays.includes(ele.value)) {
		confessionDays.splice(confessionDays.indexOf(ele.value), 1)
		alert(confessionDays);
	} else {
		confessionDays.push(ele.value);
		alert(confessionDays);
	}
}

// Capture the response to .sSQ066
function clickRBConfessOnRequest(ele) {
	var rBConfessOnRequest = ele.value;
}

// Capture the response to .sSQ067
function clickRBConfessBeforeMass(ele) {
	var rBConfessBeforeMass = ele.value;
}

// Capture the response to .sSQ068
function clickRBConfessOutsideWork(ele) {
	var rBConfessOutsideWork = ele.value;
}

// Capture the response to .sSQ069
function clickRBConfessionInSecret(ele) {
	var rBConfessInSecret = ele.value;
}

// Capture the response to .sSQ070
function clickConfessionFrequency(ele) {
	var confessionFrequency = ele.innerText;
	$('.sSQ070DropdownButton').text(confessionFrequency);
	if ((confessionFrequency == "Never been after baptism")) {
		$(".sSQ059").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ071").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		$(".sSQ072").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else if ((confessionFrequency == "Haven't been for more than a year")
		|| (confessionFrequency == "Only before Easter and Christmas")) {
		$(".sSQ059").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ072").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		$(".sSQ071").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
	} else if ((confessionFrequency != "Never been after baptism")) {
		if ((confessionFrequency == "Haven't been for more than a year")) {
			$(".sSQ059").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		}
		$(".sSQ071").css('display', 'block').css('visibility', 'visible').animate({opacity: 1}, 1000);
		if ((confessionFrequency != "Haven't been for more than a year")
			&& (confessionFrequency != "Only before Easter and Christmas")) {
			// $(".sSQ059").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
			$(".sSQ072").css('visibility', 'hidden').css('display', 'none').animate({opacity: 0}, 1000);
		}
	}
}

// Capture the response to .sSQ059
function clickRBCommunionMortalSin(ele) {
	var rBCommunionMortalSin = ele.value;
}

// Capture the response to .sSQ071
function clickRBConfessAtParishesVisited(ele) {
	var rBConfessAtParishesVisited = ele.value;
}

// Capture the response to .sSQ072
function clickReasonNotConfess(ele) {
	if (reasonNotConfess.includes(ele.value)) {
		reasonNotConfess.splice(reasonNotConfess.indexOf(ele.value), 1)
		alert(reasonNotConfess);
	} else {
		reasonNotConfess.push(ele.value);
		alert(reasonNotConfess);
	}
}

// Capture the response to .sSQ074
function clickRBChoirGroupParticipation(ele) {
	var rBChoirGroupParticipation = ele.value;
}

// Capture the response to .sSQ075
function clickRBCantorParticipation(ele) {
	var rBCantorParticipation = ele.value;
}

// Capture the response to .sSQ075
function clickRBAcolyteParticipation(ele) {
	var rBAcolyteParticipation = ele.value;
}
