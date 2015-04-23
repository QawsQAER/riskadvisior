<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">

<title>Risk Advisor</title>
<%@  include file="./templates/includes.jsp"%></head>
<body>
	<%@  include file="./templates/header.jsp"%>
	<!-- Main part -->
	<div class="container">
		<div>
			<div>
				<label>Please select companies to be analyzed</label>
				<br>
				<select id='company' multiple='multiple'>
					<option value='IBM'>IBM</option>
					<option value='NWSA'>NWSA</option>
					<option value='FUBC'>FUBC</option>
					<option value='VNET'>VNET</option>
					<option value='XXII'>XXII</option>
					<option value='DDD'>DDD</option>
					<option value='MMM'>MMM</option>
					<option value='JOBS'>JOBS</option>
					<option value='WUBA'>WUBA</option>
					<option value='EGHT'>EGHT</option>
					<option value='AIR'>AIR</option>
					<option value='AVHI'>AVHI</option>
				</select>
			</div>
			<br>
			<label>Please choose risk factors to be considered</label>
			<div class="row">
				<div class="col-md-4">
					<div>
						<label>Funding Risks</label>
						<br>
						<select id='fundingRisks' multiple='multiple'>
							<option value='capital'>capital</option>
							<option value='raise capital'>raise capital</option>
							<option value='funding risk'>funding risk</option>
							<option value='capital resource'>capital resource</option>
							<option value='the amount of capital'>the amount of capital</option>
							<option value='capital expenditure'>capital expenditure</option>
							<option value='additional capital'>additional capital</option>
							<option value='sufficient capital'>sufficient capital</option>
							<option value='credit rat'>credit rat</option>
							<option value='borrowing cost'>borrowing cost</option>
							<option value='interest expense'>interest expense</option>
						</select>
					</div>
					<div>
						<label>Concentration on few large customers</label>
						<br>
						<select id='conLargeCustomers' multiple='multiple'>
							<option value='customer'>customer</option>
							<option value='key customer'>key customer</option>
							<option value='large customer'>large customer</option>
						</select>
					</div>
					<div>
						<label>Competition risks</label>
						<br>
						<select id='competitionRisk' multiple='multiple'>
							<option value='competition'>competition</option>
							<option value='highly competitive'>highly competitive</option>
							<option value='less competitive'>less competitive</option>
							<option value='our competitors include'>our competitors include</option>
							<option value='many competitors'>many competitors</option>
							<option value='compete with'>compete with</option>
							<option value='competes with'>competes with</option>
							<option value='competition in existing and new market'>competition in existing and new market</option>
							<option value='changes in competition'>changes in competition</option>
							<option value='change in competition'>change in competition</option>
							<option value='compete against'>compete against</option>
							<option value='competes against'>competes against</option>
							<option value='compete in'>compete in</option>
							<option value='competes in'>competes in</option>
							<option value='significant competition'>significant competition</option>
							<option value='competitor'>competitor</option>
							<option value='intense competition'>intense competition</option>
							<option value='competitive pressure'>competitive pressure</option>
						</select>
					</div>
					<div>
						<label>Downstream risks</label>
						<br>
						<select id='downStreamRisk' multiple='multiple'>
							<option value='distributor'>distributor</option>
							<option value='retailers'>retailers</option>
							<option value='intermediaries'>intermediaries</option>
							<option value='performance of  ...  distributor'>performance of  ...  distributor</option>
							<option value='rely ... distributor'>rely ... distributor</option>
							<option value='dependent upon ... distributor'>dependent upon ... distributor</option>
							<option value='dependent on ... distributor'>dependent on ... distributor</option>
							<option value='based on ... distributor'>based on ... distributor</option>
							<option value='affect  ... distributor'>affect  ... distributor</option>
							<option value='change ... distributor'>change ... distributor</option>
							<option value='change ... retailer'>change ... retailer</option>
							<option value='retain ... intermediar'>retain ... intermediar</option>
							<option value='performance of  ...  retailer'>performance of  ...  retailer</option>
							<option value='rely ... retailer'>rely ... retailer</option>
							<option value='dependent upon ... retailer'>dependent upon ... retailer</option>
							<option value='dependent on ... retailer'>dependent on ... retailer</option>
							<option value='based on ... retailer'>based on ... retailer</option>
							<option value='affect  ... retailer'>affect  ... retailer</option>
							<option value='change ... retailer'>change ... retailer</option>
						</select>
					</div>
					<div>
						<label>Catastrophes</label>
						<br>
						<select id='catastrophes' multiple='multiple'>
							<option value='catastrophe'>catastrophe</option>
							<option value='terrorist'>terrorist</option>
							<option value='uninsurable'>uninsurable</option>
							<option value='hurricane'>hurricane</option>
							<option value='earthquake'>earthquake</option>
							<option value='flood'>flood</option>
							<option value='tsunami'>tsunami</option>
							<option value='war'>war</option>
							<option value='windstorm'>windstorm</option>
							<option value='natural disaster'>natural disaster</option>
							<option value='catastrophic nature'>catastrophic nature</option>
							<option value='not .. insurable'>not .. insurable</option>
						</select>
					</div>
					<div>
						<label>Macroeconomic risks</label>
						<br>
						<select id='macroeconomicRisks' multiple='multiple'>
							<option value='economic'>economic</option>
							<option value='macroeconomic'>macroeconomic</option>
							<option value='recession'>recession</option>
							<option value='economic condition'>economic condition</option>
							<option value='economic situation'>economic situation</option>
							<option value='economic slowdown'>economic slowdown</option>
							<option value='economic climate'>economic climate</option>
							<option value='economic instability'>economic instability</option>
							<option value='economic downturn'>economic downturn</option>
							<option value='economic recovery'>economic recovery</option>
							<option value='interest rate'>interest rate</option>
							<option value='market fluctuation'>market fluctuation</option>
						</select>
					</div>
					<div>
						<label>Input prices risks</label>
						<br>
						<select id='inputPricesRisks' multiple='multiple'>
							<option value='cost'>cost</option>
							<option value='expense'>expense</option>
							<option value='raw materials cost'>raw materials cost</option>
							<option value='raw material cost'>raw material cost</option>
							<option value='cost of raw material'>cost of raw material</option>
							<option value='material remedial cost'>material remedial cost</option>
							<option value='increased cost'>increased cost</option>
							<option value='start-up expense'>start-up expense</option>
							<option value='significant cost'>significant cost</option>
							<option value='significant increase in the cost'>significant increase in the cost</option>
							<option value='compliance cost'>compliance cost</option>
							<option value='incremental cost'>incremental cost</option>
							<option value='greater overall cost'>greater overall cost</option>
							<option value='increase in our cost'>increase in our cost</option>
							<option value='increased cost'>increased cost</option>
							<option value='substantial cost'>substantial cost</option>
							<option value='divert resource'>divert resource</option>
							<option value='additional cost'>additional cost</option>
							<option value='administrative expense'>administrative expense</option>
							<option value='significant expense'>significant expense</option>
							<option value='excessive cost'>excessive cost</option>
							<option value='research and development cost'>research and development cost</option>
						</select>
					</div>
					<div>
						<label>Industry is cyclical</label>
						<br>
						<select id='industryIsCyclical' multiple='multiple'>
							<option value='cyclical'>cyclical</option>
							<option value='market .. cyclical'>market .. cyclical</option>
							<option value='cyclical ï¿½ï¿½ industry'>cyclical ï¿½ï¿½ industry</option>
						</select>
					</div>
				</div>
				<div class = "col-md-4">
					<div>
						<label>Suppliers risks</label>
						<br>
						<select id='suppliersRisks' multiple='multiple'>
							<option value='supplier'>supplier</option>
							<option value='depend on ï¿½ï¿½ supplier'>depend on ï¿½ï¿½ supplier</option>
							<option value='a limited number of suppliers'>a limited number of suppliers</option>
							<option value='sole supplier'>sole supplier</option>
							<option value='single supplier'>single supplier</option>
							<option value='single source supplier'>single source supplier</option>
							<option value='single-source supplier'>single-source supplier</option>
							<option value='alternative supplier'>alternative supplier</option>
						</select>
					</div>
					<div>
						<label>Human resource risks</label>
						<br>
						<select id='humanResourceRisks' multiple='multiple'>
							<option value='personnel'>personnel</option>
							<option value='human resource'>human resource</option>
							<option value='labor cost'>labor cost</option>
							<option value='employee benefits plans'>employee benefits plans</option>
						</select>
					</div>
					<div>
						<label>Potential/Ongoing Lawsuits</label>
						<br>
						<select id='potentialLawsuits' multiple='multiple'>
							<option value='litigation'>litigation</option>
							<option value='claims'>claims</option>
							<option value='legislation'>legislation</option>
							<option value='laws'>laws</option>
							<option value='judgements'>judgements</option>
							<option value='jurisdictions'>jurisdictions</option>
							<option value='litigation expenses'>litigation expenses</option>
							<option value='foreign laws'>foreign laws</option>
						</select>
					</div>
					<div>
						<label>Volatile demand and financial results</label>
						<br>
						<select id='volatileDemandFinancialResults' multiple='multiple'>
							<option value='volatile'>volatile</option>
							<option value='unpredictable'>unpredictable</option>
							<option value='demand'>demand</option>
							<option value='consumer demandï¿½ï¿½differ'>consumer demandï¿½ï¿½differ</option>
							<option value='consumer demandï¿½ï¿½fluctuate'>consumer demandï¿½ï¿½fluctuate</option>
							<option value='fluctuation  ...  demand'>fluctuation  ...  demand</option>
							<option value='spending pattern'>spending pattern</option>
							<option value='demand ... decrease'>demand ... decrease</option>
							<option value='changing customer preference'>changing customer preference</option>
						</select>
					</div>
					<div>
						<label>Volatile stock price risks</label>
						<br>
						<select id='volatileRisks' multiple='multiple'>
							<option value='stock'>stock</option>
							<option value='price of our common stock ï¿½ï¿½ fluctuate'>price of our common stock ï¿½ï¿½ fluctuate</option>
							<option value='price of our common stock ï¿½ï¿½ volatile'>price of our common stock ï¿½ï¿½ volatile</option>
							<option value='stock price ï¿½ï¿½  volatile'>stock price ï¿½ï¿½  volatile</option>
							<option value='stock price ï¿½ï¿½  fluctuate'>stock price ï¿½ï¿½  fluctuate</option>
							<option value='impact ï¿½ï¿½  stock price'>impact ï¿½ï¿½  stock price</option>
							<option value='affect ... price of our common stock'>affect ... price of our common stock</option>
							<option value='affect our stock price'>affect our stock price</option>
							<option value='price ï¿½ï¿½ stock ï¿½ï¿½ decline'>price ï¿½ï¿½ stock ï¿½ï¿½ decline</option>
							<option value='price ï¿½ï¿½ stock ï¿½ï¿½ fall'>price ï¿½ï¿½ stock ï¿½ï¿½ fall</option>
						</select>
					</div>
					<div>
						<label>Poor financial condition risks</label>
						<br>
						<select id='poorConditionRisks' multiple='multiple'>
							<option value='loss'>loss</option>
							<option value='net loss'>net loss</option>
							<option value='loss of business'>loss of business</option>
							<option value='negative cash flow'>negative cash flow</option>
						</select>
					</div>
					<div>
						<label>Merger and Acquisition risks</label>
						<br>
						<select id='mergerRisks' multiple='multiple'>
							<option value='acquisition'>acquisition</option>
							<option value='merger'>merger</option>
							<option value='acquisition strategy'>acquisition strategy</option>
							<option value='combinations and acquisitions'>combinations and acquisitions</option>
							<option value='property acquisition'>property acquisition</option>
							<option value='business acquisition'>business acquisition</option>
						</select>
					</div>
					<div>
						<label>Restructure Risks</label>
						<br>
						<select id='restructureRisks' multiple='multiple'>
							<option value='restructure'>restructure</option>
							<option value='restructuring charge'>restructuring charge</option>
							<option value='bankruptcy protection'>bankruptcy protection</option>
							<option value='restructuring'>restructuring</option>
						</select>
					</div>
				</div>
				<div class = "col-md-4">
					<div>
						<label>Infrastructure risks</label>
						<br>
						<select id='infrastructureRisks' multiple='multiple'>
							<option value='infrastructure'>infrastructure</option>
							<option value='information technology system'>information technology system</option>
							<option value='security system'>security system</option>
							<option value='integrating personnel'>integrating personnel</option>
						</select>
					</div>
					<div>
						<label>New product introduction risks</label>
						<br>
						<select id='newProductRisks' multiple='multiple'>
							<option value='product'>product</option>
							<option value='new product'>new product</option>
							<option value='develop product'>develop product</option>
							<option value='innovative product'>innovative product</option>
							<option value='future product'>future product</option>
							<option value='new commercial product'>new commercial product</option>
						</select>
					</div>
					<div>
						<label>Potential defects in products</label>
						<br>
						<select id='potentialProducts' multiple='multiple'>
							<option value='warranty'>warranty</option>
							<option value='product liabilit'>product liabilit</option>
							<option value='warranty liabilit'>warranty liabilit</option>
							<option value='warranty policy'>warranty policy</option>
						</select>
					</div>
					<div>
						<label>Regulation changes</label>
						<br>
						<select id='regulationChanges' multiple='multiple'>
							<option value='regulation'>regulation</option>
							<option value='environmental regulation'>environmental regulation</option>
							<option value='laws or regulations'>laws or regulations</option>
							<option value='laws and regulations'>laws and regulations</option>
							<option value='regulations and laws'>regulations and laws</option>
							<option value='regulations or laws'>regulations or laws</option>
							<option value='regulations and laws'>regulations and laws</option>
							<option value='regulations or laws'>regulations or laws</option>
							<option value='risk of liabilit'>risk of liabilit</option>
							<option value='potential liabilit'>potential liabilit</option>
							<option value='significant liabilit'>significant liabilit</option>
							<option value='specific requirement'>specific requirement</option>
							<option value='state regulation'>state regulation</option>
							<option value='federal regulation'>federal regulation</option>
							<option value='government regulation'>government regulation</option>
							<option value='legislation or regulation'>legislation or regulation</option>
							<option value='legislation and regulation'>legislation and regulation</option>
							<option value='regulation or legislation'>regulation or legislation</option>
							<option value='regulation and legislation'>regulation and legislation</option>
							<option value='new regulation'>new regulation</option>
							<option value='unknown liabilit'>unknown liabilit</option>
							<option value='liability for'>liability for</option>
							<option value='environmental liabilit'>environmental liabilit</option>
							<option value='general liabilit'>general liabilit</option>
							<option value='future liabilit'>future liabilit</option>
							<option value='tax liabilit'>tax liabilit</option>
						</select>
					</div>
					<div>
						<label>Intellectual Property Risks</label>
						<br>
						<select id='intellectualRisks' multiple='multiple'>
							<option value='intellectual property'>intellectual property</option>
							<option value='registered trademark'>registered trademark</option>
							<option value='important business technology'>important business technology</option>
							<option value='rely on ... patent'>rely on ... patent</option>
							<option value='patent ... issued/application/pending/protect/proprietary'>patent ... issued/application/pending/protect/proprietary</option>
						</select>
					</div>
					<div>
						<label>International risks</label>
						<br>
						<select id='internationalRisks' multiple='multiple'>
							<option value='international'>international</option>
							<option value='international operations'>international operations</option>
							<option value='international sales'>international sales</option>
							<option value='exchange rate'>exchange rate</option>
							<option value='in foreign countries'>in foreign countries</option>
							<option value='emerging markets'>emerging markets</option>
							<option value='international laws'>international laws</option>
							<option value='foreign economies'>foreign economies</option>
							<option value='international financial'>international financial</option>
						</select>
					</div>
				</div>
			</div>
			<h2>Selected Companies</h2>
			<div class="well">
				<ul id="comList">
				</ul>
			</div>
			<input type="hidden" id="companies" value='{}'>
			<input type="hidden" id="preferences" value='{"keywords":[]}'>
		    <br>
			<button type="submit" id="getUserPre" class="btn btn-primary">Analyze</button>
			<div id="taWidgetContainer" class="col-lg-12 col-xs-12"></div>
		</div>
	</div>

	<script type="text/javascript" src="https://ta-cdn.mybluemix.net/TradeoffAnalytics.js"></script>
	<script>
		$(document).ready(function() {
			$('#company').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#company option:selected');
	        		
	        		var newCompanies = {"companies" : []};
	        		selectedOptions.each(function() {
	        			newCompanies.companies.push($(this).val());
	        			$('#comList').append("<li>" + $(this).val() + "</li>")
	        		});
	        		
	        		$('#companies').val(JSON.stringify(newCompanies));
	        	}
	        });
			
	        $('#fundingRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#fundingRisks option:selected');
	        		
	        		var newKeyword = {"category" : "Funding risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Funding risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#conLargeCustomers').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#conLargeCustomers option:selected');
	        		
	        		var newKeyword = {"category" : "Concentration on few large customers", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Concentration on few large customers') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#competitionRisk').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#competitionRisk option:selected');
	        		
	        		var newKeyword = {"category" : "Competition risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Competition risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#downStreamRisk').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#downStreamRisk option:selected');
	        		
	        		var newKeyword = {"category" : "Downstream risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Downstream risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#catastrophes').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#catastrophes option:selected');
	        		
	        		var newKeyword = {"category" : "Catastrophes", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Catastrophes') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#macroeconomicRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#macroeconomicRisks option:selected');
	        		
	        		var newKeyword = {"category" : "Macroeconomic risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Macroeconomic risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#inputPricesRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#inputPricesRisks option:selected');
	        		
	        		var newKeyword = {"category" : "Input prices risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Input prices risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#industryIsCyclical').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#industryIsCyclical option:selected');
	        		
	        		var newKeyword = {"category" : "Industry is cyclical", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Industry is cyclical') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#suppliersRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#suppliersRisks option:selected');
	        		
	        		var newKeyword = {"category" : "Suppliers risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Suppliers risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#humanResourceRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#humanResourceRisks option:selected');
	        		
	        		var newKeyword = {"category" : "Human resource risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Human resource risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#potentialLawsuits').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#potentialLawsuits option:selected');
	        		
	        		var newKeyword = {"category" : "Potential/Ongoing Lawsuits", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Potential/Ongoing Lawsuits') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#volatileDemandFinancialResults').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#volatileDemandFinancialResults option:selected');
	        		
	        		var newKeyword = {"category" : "Volatile demand and financial results", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Volatile demand and financial results') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#volatileRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#volatileRisks option:selected');
	        		
	        		var newKeyword = {"category" : "Volatile stock price risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Volatile stock price risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#poorConditionRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#poorConditionRisks option:selected');
	        		
	        		var newKeyword = {"category" : "Poor financial condition risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Poor financial condition risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#mergerRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#mergerRisks option:selected');
	        		
	        		var newKeyword = {"category" : "Merger and Acquisition risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Merger and Acquisition risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#restructureRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#restructureRisks option:selected');
	        		
	        		var newKeyword = {"category" : "Restructure Risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Restructure Risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#infrastructureRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#infrastructureRisks option:selected');
	        		
	        		var newKeyword = {"category" : "Infrastructure risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Infrastructure risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#newProductRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#newProductRisks option:selected');
	        		
	        		var newKeyword = {"category" : "New product introduction risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'New product introduction risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#potentialProducts').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#potentialProducts option:selected');
	        		
	        		var newKeyword = {"category" : "Potential defects in products", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Potential defects in products') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#regulationChanges').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#regulationChanges option:selected');
	        		
	        		var newKeyword = {"category" : "Regulation changes", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Regulation changes') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#intellectualRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#intellectualRisks option:selected');
	        		
	        		var newKeyword = {"category" : "Intellectual Property Risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'Intellectual Property Risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	        $('#internationalRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		var selectedOptions = $('#internationalRisks option:selected');
	        		
	        		var newKeyword = {"category" : "FInternational risks", "factors" : []};
	        		selectedOptions.each(function () {
	        			newKeyword.factors.push($(this).val());
	        		});
	        		
	        		var json = JSON.parse($('#preferences').val());
					for(cgory in json.keywords) {
						if(json.keywords[cgory].category == 'International risks') {
							json.keywords.splice(cgory, 1);
							break;
						}
					}
					if(selectedOptions.length != 0) {
						json.keywords.push(newKeyword);
					}
					$('#preferences').val(JSON.stringify(json));
	        	}
	        });
	    });

		'use strict';

var taClient = null;
var lastTheme = $("#themes option:first").val();
var lastProfile = 'basic';
//var MIN_BAR_SLIDE_PERIOD = 500;


function getCategory(){

}

function onError() {
  var errorMsg = 'Error processing the request.';
  alert("error!!!")
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

function onResultSelection(){
  
}

function onResultsReady() {
  // $('.analyze').show();
  // $('.loading').hide();

  // showResults();
  // resizeToParent();
  // onPageReady();
  jumpTo('#taWidgetContainer');
}

function hideResults() {
    $('.viz').addClass('result');
}

function destroyTradeoffAnalytcsWidget(callback) {
    taClient.destroy(callback);
}


$('#getUserPre').click(function () {
  var json1 = JSON.parse($('#companies').val());
  var json2 = JSON.parse($('#preferences').val());
  var json = {"companies" : json1.companies, "keywords" : json2.keywords, "year" : "2014"};
  //alert(JSON.stringify(json));
  $.ajax({
    type: "POST",
    beforeSend: function (request) {
      request.setRequestHeader("Content-Type", "text/plain");
    },
    url:"/api/parser/select", 
    data: JSON.stringify(json),
    dataType: "json", 
    success: function(data) {
      //alert(JSON.parse(data));
      alert(data)

      taClient = new TradeoffAnalytics({
        dilemmaServiceUrl: '/demo',
        customCssUrl: 'https://ta-cdn.mybluemix.net/modmt/styles/watson.css',
        profile: 'basic',
        errCallback: onError
      }, 'taWidgetContainer');

      taClient.start(function() {
        showTradeoffAnalytcsWidget(JSON.parse(data));
      });
      //taClient.show(data)
    }
  });
});
	</script>
	
	<%@  include file="./templates/footer.jsp"%>
</body>
</html>