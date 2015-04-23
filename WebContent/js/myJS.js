'use strict';

var taClient = null;
var lastTheme = $("#themes option:first").val();
var lastProfile = 'basic';
//var MIN_BAR_SLIDE_PERIOD = 500;


function getCategory(){

}

function getJsonFromElement(element) {
    var elementJson = null;
    try{
      elementJson = JSON.parse(element.val());
    } catch(e) {
      element.css('border','1px solid red');
      onError({error: 'JSON is malformed.'});
      return elementJson;
    }
    element.css('border','1px solid grey');
    $('.errorArea').hide();
    return elementJson;
}


function onAnalyzeClick() {
	$('.analyze').hide();
	$('.loading').show();
	$('.decisionArea').hide();

	$('.errorArea').hide();
	hideResults();

	var problemJson = getJsonFromElement($('.problemText'));
	if (!problemJson)
	  return;

	var featuresJson = getJsonFromElement($('.featuresText'));
	if (!featuresJson)
	  return;

	recreateWidgetIfNeeded(function() {
	  showTradeoffAnalytcsWidget(problemJson);
	});
}

function recreateWidgetIfNeeded(showWidget) {
	var showAdvanced = $('.showAdvance').val() === 'yes';
	var selectedProfile = showAdvanced ?  $('.profiles').val() : 'basic';
    var selectedTheme =  showAdvanced ?  $('#themes').val() : $("#themes option:first").val();
	var profile = showAdvanced && selectedProfile === 'custom' ? JSON.parse($('#featuresText').val()) : selectedProfile;
    
    if (selectedTheme !== lastTheme || JSON.stringify(profile) !== JSON.stringify(lastProfile))  {
	  destroyTradeoffAnalytcsWidget(function() {
		loadTradeoffAnalytics(profile, selectedTheme, showWidget, onError);
	  });
    } else {
    	showWidget();
    }
    
    lastProfile = profile;
    lastTheme = selectedTheme;
}

function showTradeoffAnalytcsWidget(problem) {
    taClient.show(problem, onResultsReady, onResultSelection);
}

function hideResults() {
    $('.viz').addClass('result');
}

function destroyTradeoffAnalytcsWidget(callback) {
    taClient.destroy(callback);
}

function loadTradeoffAnalytics(profile, themeName, callback, errCallback) {
    taClient = new TradeoffAnalytics({
      dilemmaServiceUrl: 'demo',
      customCssUrl: 'https://ta-cdn.mybluemix.net/modmt/styles/' + themeName + '.css',
      profile: profile,
      errCallback: errCallback
    }, 'taWidgetContainer');

    taClient.start(callback);
}

$('#getUserPre').click(function () {
  var json1 = JSON.parse($('#companies').val());
  var json2 = JSON.parse($('#preferences').val());
  var json = {"companies" : json1.companies, "keywords" : json2.keywords, "year" : "2014"};
  alert(JSON.stringify(json));
  $.ajax({
    type: "POST",
    beforeSend: function (request) {
      request.setRequestHeader("Content-Type", "text/plain");
    },
    url:"http://localhost:8080/webStarterApp/api/parser/select", 
    data: JSON.stringify(json),
    dataType: "json", 
    success: function(data) {
      alert(JSON.parse(data));

      taClient = new TradeoffAnalytics({
        dilemmaServiceUrl: 'demo',
        customCssUrl: 'https://ta-cdn.mybluemix.net/modmt/styles/watson.css',
        profile: profile,
        errCallback: errCallback
      }, 'taWidgetContainer');

      //taClient.start(callback);
      taClient.show(data)
    }
  });
});