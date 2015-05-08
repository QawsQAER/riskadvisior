
var top_tags = [
	{text: "Consumer Complaint Database", weight:10, link: 'http://catalog.data.gov/dataset/consumer-complaint-database' },
	{text: "American Community Survey", weight:9, link: 'http://catalog.data.gov/dataset/american-community-survey' },
	{text: "American Time Use Survey", weight:8, link: 'http://catalog.data.gov/dataset/american-time-use-survey-54e68' },
	{text: "Consumer Expenditure Survey", weight:7, link: 'http://catalog.data.gov/dataset/consumer-expenditure-survey' },
	{text: "Economic Census", weight:6, link: 'http://catalog.data.gov/dataset/economic-census' },
	{text: "Job Openings and Labor Turnover Survey", weight:5, link: 'http://catalog.data.gov/dataset/job-openings-and-labor-turnover-survey' },
	{text: "Services Annual Survey", weight:4, link: 'http://catalog.data.gov/dataset/services-annual-survey' },
	{text: "Economic Indicator Database Search", weight:3, link: 'http://catalog.data.gov/dataset/economic-indicator-database-search' },
	{text: "American FactFinder II", weight:2, link: 'http://catalog.data.gov/dataset/american-factfinder-ii' },
	{text: "Statistics of U.S. Businesses (SUSB)", weight:1, link: 'http://catalog.data.gov/dataset/statistics-of-us-businesses-susb' }
];

//var gradient = tinygradient.hsv(9);
var url_prefix = './../api';

$(function () {
	var data = $("#tagname").val();
	var geturl = url_prefix+"/tagName/business/topDataset/10";
	console.log(geturl);
	$.ajax({
		url: geturl,
		cache: true,
		success: function (data) {
			console.log('success: '+data);
			var count = data.count;
			$("#totalcount").text(count);
			console.log(data);
			$("#container8").jQCloud("destroy");
			$("#container8").jQCloud(data.content);
		},
		error: function(xhr, status, error) {
			console.log('error: ' + status);
			alert("Resource not found");
        }
	
	});
});

function groupTopTag(groupID) {
	var geturl = "/groupName/"+groupID+"/topTags/20";
	extracted(geturl);
}

function groupTopDataset(groupID) {
	var geturl = "/groupName/"+groupID+"/topDataset/20";
	extracted(geturl);
}

function groupTopHealthTag() {
	var geturl = "/groupName1/health/topTags/20";
	extracted(geturl);
}

function groupTopHealthDataset() {
	var geturl = "/groupName1/health/topDataset/20";
	extracted(geturl);
}

var extracted;

$(function () {

	extracted = function extracted(geturl) {
		geturl = url_prefix+geturl;
		console.log(geturl);
		$.ajax({
			url: geturl,
			cache: true,
			success: function (data) {
				console.log('success: '+data);
				var count = data.count;
				$("#totalcount").text(count);
				console.log(data);
				$("#container8").jQCloud("destroy");
				$("#container8").jQCloud(data.content);
			},
			error: function(xhr, status, error) {
				console.log('error: ' + status);
				alert("Resource not found");
	        }
		});
	}

	//Search top related tags
	$('#toptagSubmit').click(function () {
		var data = $("#tagname").val();
		var geturl = "/tagName/"+data+"/topTags/10";
		extracted(geturl);
	});

	//Search top datasets of a tag
	$('#topdatasetSubmit').click(function () {
		var data = $("#tagname").val();
		var geturl = "/tagName/"+data+"/topDataset/10";
		extracted(geturl);
	});


	//Search all datasets of a tag (too large not recommended)
	$('#datasetSubmit').click(function () {
		var data = $("#tagname").val();
		var geturl = "/tagName/"+data;
		extracted(geturl);
	});


	//Search
	$('#groupDatasetSubmit').click(function () {
		var data = $("#group").val();
		var geturl = "/groupName/"+data+"/topDataset/20";
		extracted(geturl);
	});
	//Search
	$('#groupSubmit').click(function () {
		var data = $("#group").val();
		var geturl = "/groupName/"+data+"/topTags/20";
		extracted(geturl);
	});



});


