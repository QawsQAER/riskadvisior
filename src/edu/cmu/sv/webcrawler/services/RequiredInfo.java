package edu.cmu.sv.webcrawler.services;

import java.util.HashMap;

public class RequiredInfo {
	String documentType = "";
	HashMap<String,String> riskfactor = new HashMap<String,String>();
	
	public void setDocType(String type){
		this.documentType = type;
	}
	public String getDocType(){
		return this.documentType;
	}
	
	public void addRiskFactor(String url, String rf){
		this.riskfactor.put(url, rf);
	}
	public HashMap<String,String> getRiskFactor(){
		return this.riskfactor;
	}
}
