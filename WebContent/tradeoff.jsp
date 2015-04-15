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

			<div class="row">
				<div >
				<div>
					<label>Company</label>
					<select id='fundingRisks' multiple='multiple'>
						<option value=capital>capital</option>
						<option value=raise capital>raise capital</option>
						<option value=funding risk>funding risk</option>
						<option value=capital resource>capital resource</option>
						<option value=the amount of capital>the amount of capital</option>
						<option value=capital expenditure>capital expenditure</option>
						<option value=additional capital>additional capital</option>
						<option value=sufficient capital>sufficient capital</option>
						<option value=credit rat>credit rat</option>
						<option value=borrowing cost>borrowing cost</option>
						<option value=interest expense>interest expense</option>
					</select>
				</div>

				<div>
					<label>Funding Risks</label>
					<select id='fundingRisks' multiple='multiple'>
						<option value=capital>capital</option>
						<option value=raise capital>raise capital</option>
						<option value=funding risk>funding risk</option>
						<option value=capital resource>capital resource</option>
						<option value=the amount of capital>the amount of capital</option>
						<option value=capital expenditure>capital expenditure</option>
						<option value=additional capital>additional capital</option>
						<option value=sufficient capital>sufficient capital</option>
						<option value=credit rat>credit rat</option>
						<option value=borrowing cost>borrowing cost</option>
						<option value=interest expense>interest expense</option>
					</select>
				</div>
				<div>
					<label>Concentration on few large customers</label>
					<select id='conLargeCustomers' multiple='multiple'>
						<option value=customer>customer</option>
						<option value=key customer>key customer</option>
						<option value=large customer>large customer</option>
					</select>
				</div>
				<div>
					<label>Competition risks</label>
					<select id='competitionRisk' multiple='multiple'>
						<option value=competition>competition</option>
						<option value=highly competitive>highly competitive</option>
						<option value=less competitive>less competitive</option>
						<option value=our competitors include>our competitors include</option>
						<option value=many competitors>many competitors</option>
						<option value=compete with>compete with</option>
						<option value=competes with>competes with</option>
						<option value=competition in existing and new market>competition in existing and new market</option>
						<option value=changes in competition>changes in competition</option>
						<option value=change in competition>change in competition</option>
						<option value=compete against>compete against</option>
						<option value=competes against>competes against</option>
						<option value=compete in>compete in</option>
						<option value=competes in>competes in</option>
						<option value=significant competition>significant competition</option>
						<option value=competitor>competitor</option>
						<option value=intense competition>intense competition</option>
						<option value=competitive pressure>competitive pressure</option>
					</select>
				</div>
				<div>
					<label>Downstream risks</label>
					<select id='DownStreamRisk' multiple='multiple'>
						<option value=distributor>distributor</option>
						<option value=retailers>retailers</option>
						<option value=intermediaries>intermediaries</option>
						<option value=performance of  ...  distributor>performance of  ...  distributor</option>
						<option value=rely ... distributor>rely ... distributor</option>
						<option value=dependent upon ... distributor>dependent upon ... distributor</option>
						<option value=dependent on ... distributor>dependent on ... distributor</option>
						<option value=based on ... distributor>based on ... distributor</option>
						<option value=affect  ... distributor>affect  ... distributor</option>
						<option value=change ... distributor>change ... distributor</option>
						<option value=change ... retailer>change ... retailer</option>
						<option value=retain ... intermediar>retain ... intermediar</option>
						<option value=performance of  ...  retailer>performance of  ...  retailer</option>
						<option value=rely ... retailer>rely ... retailer</option>
						<option value=dependent upon ... retailer>dependent upon ... retailer</option>
						<option value=dependent on ... retailer>dependent on ... retailer</option>
						<option value=based on ... retailer>based on ... retailer</option>
						<option value=affect  ... retailer>affect  ... retailer</option>
						<option value=change ... retailer>change ... retailer</option>
					</select>
				</div>
				<div>
					<label>Catastrophes</label>
					<select id='catastrophes' multiple='multiple'>
						<option value=catastrophe>catastrophe</option>
						<option value=terrorist>terrorist</option>
						<option value=uninsurable>uninsurable</option>
						<option value=hurricane>hurricane</option>
						<option value=earthquake>earthquake</option>
						<option value=flood>flood</option>
						<option value=tsunami>tsunami</option>
						<option value=war>war</option>
						<option value=windstorm>windstorm</option>
						<option value=natural disaster>natural disaster</option>
						<option value=catastrophic nature>catastrophic nature</option>
						<option value=not .. insurable>not .. insurable</option>
					</select>
				</div>
				<div>
					<label>Macroeconomic risks</label>
					<select id='macroeconomicRisks' multiple='multiple'>
						<option value=economic>economic</option>
						<option value=macroeconomic>macroeconomic</option>
						<option value=recession>recession</option>
						<option value=economic condition>economic condition</option>
						<option value=economic situation>economic situation</option>
						<option value=economic slowdown>economic slowdown</option>
						<option value=economic climate>economic climate</option>
						<option value=economic instability>economic instability</option>
						<option value=economic downturn>economic downturn</option>
						<option value=economic recovery>economic recovery</option>
						<option value=interest rate>interest rate</option>
						<option value=market fluctuation>market fluctuation</option>
					</select>
				</div>
				<div>
					<label>Input prices risks</label>
					<select id='inputPricesRisks' multiple='multiple'>
						<option value=cost>cost</option>
						<option value=expense>expense</option>
						<option value=raw materials cost>raw materials cost</option>
						<option value=raw material cost>raw material cost</option>
						<option value=cost of raw material>cost of raw material</option>
						<option value=material remedial cost>material remedial cost</option>
						<option value=increased cost>increased cost</option>
						<option value=start-up expense>start-up expense</option>
						<option value=significant cost>significant cost</option>
						<option value=significant increase in the cost>significant increase in the cost</option>
						<option value=compliance cost>compliance cost</option>
						<option value=incremental cost>incremental cost</option>
						<option value=greater overall cost>greater overall cost</option>
						<option value=increase in our cost>increase in our cost</option>
						<option value=increased cost>increased cost</option>
						<option value=substantial cost>substantial cost</option>
						<option value=divert resource>divert resource</option>
						<option value=additional cost>additional cost</option>
						<option value=administrative expense>administrative expense</option>
						<option value=significant expense>significant expense</option>
						<option value=excessive cost>excessive cost</option>
						<option value=research and development cost>research and development cost</option>
					</select>
				</div>
				</div>

				<div>
				<div>
					<label>Industry is cyclical</label>
					<select id='industryIsCyclical' multiple='multiple'>
						<option value=cyclical>cyclical</option>
						<option value=market .. cyclical>market .. cyclical</option>
						<option value=cyclical �� industry>cyclical �� industry</option>
					</select>
				</div>
				<div>
					<label>Suppliers risks</label>
					<select id='suppliersRisks' multiple='multiple'>
						<option value=supplier>supplier</option>
						<option value=depend on �� supplier>depend on �� supplier</option>
						<option value=a limited number of suppliers>a limited number of suppliers</option>
						<option value=sole supplier>sole supplier</option>
						<option value=single supplier>single supplier</option>
						<option value=single source supplier>single source supplier</option>
						<option value=single-source supplier>single-source supplier</option>
						<option value=alternative supplier>alternative supplier</option>
					</select>
				</div>
				<div>
					<label>Human resource risks</label>
					<select id='humanResourceRisks' multiple='multiple'>
						<option value=personnel>personnel</option>
						<option value=human resource>human resource</option>
						<option value=labor cost>labor cost</option>
						<option value=employee benefits plans>employee benefits plans</option>
					</select>
				</div>
				<div>
					<label>Potential/Ongoing Lawsuits</label>
					<select id='potentialLawsuits' multiple='multiple'>
						<option value=litigation>litigation</option>
						<option value=claims>claims</option>
						<option value=legislation>legislation</option>
						<option value=laws>laws</option>
						<option value=judgements>judgements</option>
						<option value=jurisdictions>jurisdictions</option>
						<option value=litigation expenses>litigation expenses</option>
						<option value=foreign laws>foreign laws</option>
					</select>
				</div>
				<div>
					<label>Volatile demand and financial results</label>
					<select id='volatileDemandFinancialResults' multiple='multiple'>
						<option value=volatile>volatile</option>
						<option value=unpredictable>unpredictable</option>
						<option value=demand>demand</option>
						<option value=consumer demand��differ>consumer demand��differ</option>
						<option value=consumer demand��fluctuate>consumer demand��fluctuate</option>
						<option value=fluctuation  ...  demand>fluctuation  ...  demand</option>
						<option value=spending pattern>spending pattern</option>
						<option value=demand ... decrease>demand ... decrease</option>
						<option value=changing customer preference>changing customer preference</option>
					</select>
				</div>
				<div>
					<label>Volatile stock price risks</label>
					<select id='volatileRisks' multiple='multiple'>
						<option value=stock>stock</option>
						<option value=price of our common stock �� fluctuate>price of our common stock �� fluctuate</option>
						<option value=price of our common stock �� volatile>price of our common stock �� volatile</option>
						<option value=stock price ��  volatile>stock price ��  volatile</option>
						<option value=stock price ��  fluctuate>stock price ��  fluctuate</option>
						<option value=impact ��  stock price>impact ��  stock price</option>
						<option value=affect ... price of our common stock>affect ... price of our common stock</option>
						<option value=affect our stock price>affect our stock price</option>
						<option value=price �� stock �� decline>price �� stock �� decline</option>
						<option value=price �� stock �� fall>price �� stock �� fall</option>
					</select>
				</div>
				<div>
					<label>Poor financial condition risks</label>
					<select id='poorConditionRisks' multiple='multiple'>
						<option value=loss>loss</option>
						<option value=net loss>net loss</option>
						<option value=loss of business>loss of business</option>
						<option value=negative cash flow>negative cash flow</option>
					</select>
				</div>
				<div>
					<label>Merger and Acquisition risks</label>
					<select id='mergerRisks' multiple='multiple'>
						<option value=acquisition>acquisition</option>
						<option value=merger>merger</option>
						<option value=acquisition strategy>acquisition strategy</option>
						<option value=combinations and acquisitions>combinations and acquisitions</option>
						<option value=property acquisition>property acquisition</option>
						<option value=business acquisition>business acquisition</option>
					</select>
				</div>
				</div>

				<div>
				<div>
					<label>Restructure Risks</label>
					<select id='restructureRisks' multiple='multiple'>
						<option value=restructure>restructure</option>
						<option value=restructuring charge>restructuring charge</option>
						<option value=bankruptcy protection>bankruptcy protection</option>
						<option value=restructuring>restructuring</option>
					</select>
				</div>
				<div>
					<label>Infrastructure risks</label>
					<select id='infrastructureRisks' multiple='multiple'>
						<option value=infrastructure>infrastructure</option>
						<option value=information technology system>information technology system</option>
						<option value=security system>security system</option>
						<option value=integrating personnel>integrating personnel</option>
					</select>
				</div>
				<div>
					<label>New product introduction risks</label>
					<select id='newProductRisks' multiple='multiple'>
						<option value=product>product</option>
						<option value=new product>new product</option>
						<option value=develop product>develop product</option>
						<option value=innovative product>innovative product</option>
						<option value=future product>future product</option>
						<option value=new commercial product>new commercial product</option>
					</select>
				</div>
				<div>
					<label>Potential defects in products</label>
					<select id='potentialProducts' multiple='multiple'>
						<option value=warranty>warranty</option>
						<option value=product liabilit>product liabilit</option>
						<option value=warranty liabilit>warranty liabilit</option>
						<option value=warranty policy>warranty policy</option>
					</select>
				</div>
				<div>
					<label>Regulation changes</label>
					<select id='regulationChanges' multiple='multiple'>
						<option value=regulation>regulation</option>
						<option value=environmental regulation>environmental regulation</option>
						<option value=laws or regulations>laws or regulations</option>
						<option value=laws and regulations>laws and regulations</option>
						<option value=regulations and laws>regulations and laws</option>
						<option value=regulations or laws>regulations or laws</option>
						<option value=regulations and laws>regulations and laws</option>
						<option value=regulations or laws>regulations or laws</option>
						<option value=risk of liabilit>risk of liabilit</option>
						<option value=potential liabilit>potential liabilit</option>
						<option value=significant liabilit>significant liabilit</option>
						<option value=specific requirement>specific requirement</option>
						<option value=state regulation>state regulation</option>
						<option value=federal regulation>federal regulation</option>
						<option value=government regulation>government regulation</option>
						<option value=legislation or regulation>legislation or regulation</option>
						<option value=legislation and regulation>legislation and regulation</option>
						<option value=regulation or legislation>regulation or legislation</option>
						<option value=regulation and legislation>regulation and legislation</option>
						<option value=new regulation>new regulation</option>
						<option value=unknown liabilit>unknown liabilit</option>
						<option value=liability for>liability for</option>
						<option value=environmental liabilit>environmental liabilit</option>
						<option value=general liabilit>general liabilit</option>
						<option value=future liabilit>future liabilit</option>
						<option value=tax liabilit>tax liabilit</option>
					</select>
				</div>
				<div>
					<label>Intellectual Property Risks</label>
					<select id='intellectualRisks' multiple='multiple'>
						<option value=intellectual property>intellectual property</option>
						<option value=registered trademark>registered trademark</option>
						<option value=important business technology>important business technology</option>
						<option value=rely on ... patent>rely on ... patent</option>
						<option value=patent ... issued/application/pending/protect/proprietary>patent ... issued/application/pending/protect/proprietary</option>
					</select>
				</div>
				<div>
					<label>International risks</label>
					<select id='internationalRisks' multiple='multiple'>
						<option value=international>international</option>
						<option value=international operations>international operations</option>
						<option value=international sales>international sales</option>
						<option value=exchange rate>exchange rate</option>
						<option value=in foreign countries>in foreign countries</option>
						<option value=emerging markets>emerging markets</option>
						<option value=international laws>international laws</option>
						<option value=foreign economies>foreign economies</option>
						<option value=international financial>international financial</option>
					</select>
				</div>
				</div>
			</div>
			<h2>Selected Companies</h2>
			<div class="well">
				<ul id="comList">
				</ul>
			</div>
			<input type="text" class="form-control" id="inputCompany" placeholder="Company Name">
			<input type="hidden" id="companys" value='{"companys":[]}'>
			<input type="hidden" id="preferences" value='{"keywords":[{
		            "category": "Funding risks",
		            "factors": [
		            ]
	        	},
		        {
		            "category": "Concentration on few large customers",
		            "factors": [  
		            ]
		        },
		        {
		            "category": "Competition risks",
		            "factors": [  
		            ]
		        }
		        ]
		    }'>
		    <br>
			<button type="submit" id="appendComp" class="btn btn-success">Add</button>
			<button type="submit" id="getUserPre" class="btn btn-primary">Analyze</button>
		</div>
	</div>
	<script>
		$(document).ready(function() {
	        $('#fundingRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true,
	        	onDropdownHide: function (options, select) {
	        		options.each(function(data) {
	        			alert(data);
	        		});
	        	}
	        });
	        $('#conLargeCustomers').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#competitionRisk').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#DownStreamRisk').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#catastrophes').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#macroeconomicRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#inputPricesRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#industryIsCyclical').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#suppliersRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#humanResourceRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#potentialLawsuits').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#volatileDemandFinancialResults').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#volatileRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#poorConditionRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#mergerRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#restructureRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#infrastructureRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#newProductRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#potentialProducts').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#regulationChanges').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#intellectualRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	        $('#internationalRisks').multiselect({
	        	includeSelectAllOption: true,
	        	enableFiltering: true
	        });
	    });
		
		$('.check').change(function () {
			if($(this).is(":checked")==true) {
				var json = JSON.parse($('#preferences').val());
				for(cgory in json.keywords) {
					if(json.keywords[cgory].category == 'Funding risks') {
						json.keywords[cgory].factors.push($(this).val());
					}
				}
				$('#preferences').val(JSON.stringify(json));
			} else {
				var json = JSON.parse($('#preferences').val());
				for(cgory in json.keywords) {
					if(json.keywords[cgory].category == 'Funding risks') {
						for(ckeys in json.keywords[cgory].factors)
							if(json.keywords[cgory].factors[ckeys] == $(this).val())
							json.keywords[cgory].factors.splice(ckeys,1);
					}
				}
				$('#preferences').val(JSON.stringify(json));
			}
		});
		$('.check1').change(function () {
			if($(this).is(":checked")==true) {
				var json = JSON.parse($('#preferences').val());
				for(cgory in json.keywords) {
					if(json.keywords[cgory].category == 'Concentration on few large customers') {
						json.keywords[cgory].factors.push($(this).val());
					}
				}
				$('#preferences').val(JSON.stringify(json));
			} else {
				var json = JSON.parse($('#preferences').val());
				for(cgory in json.keywords) {
					if(json.keywords[cgory].category == 'Concentration on few large customers') {
						for(ckeys in json.keywords[cgory].factors)
							if(json.keywords[cgory].factors[ckeys] == $(this).val())
							json.keywords[cgory].factors.splice(ckeys,1);
					}
				}
				$('#preferences').val(JSON.stringify(json));
			}
		});
		$('.check2').change(function () {
			if($(this).is(":checked")==true) {
				var json = JSON.parse($('#preferences').val());
				for(cgory in json.keywords) {
					if(json.keywords[cgory].category == 'Competition risks') {
						json.keywords[cgory].factors.push($(this).val());
					}
				}
				$('#preferences').val(JSON.stringify(json));
			} else {
				var json = JSON.parse($('#preferences').val());
				for(cgory in json.keywords) {
					if(json.keywords[cgory].category == 'Competition risks') {
						for(ckeys in json.keywords[cgory].factors)
							if(json.keywords[cgory].factors[ckeys] == $(this).val())
							json.keywords[cgory].factors.splice(ckeys,1);
					}
				}
				$('#preferences').val(JSON.stringify(json));
			}
		});
		
		$('#appendComp').click(function () {
			var json = JSON.parse($('#companys').val());
			json.companys.push($('#inputCompany').val());
			$('#companys').val(JSON.stringify(json));
			$('#comList').append("<li>" + $('#inputCompany').val() + "</li>")
		});
	
		$('#getUserPre').click(function () {
			var json1 = JSON.parse($('#companys').val());
			var json2 = JSON.parse($('#preferences').val());
			var json = {"companies" : json1.companys, "keywords" : json2.keywords, "year" : "2014"};
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
				}
			});
		});
	</script>

	<%@  include file="./templates/footer.jsp"%>
</body>
</html>