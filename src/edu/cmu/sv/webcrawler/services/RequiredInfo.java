package edu.cmu.sv.webcrawler.services;

import java.util.HashMap;



public class RequiredInfo {

	String documentType = "";
	String url = "";
	String riskFactor = "";
	String companyName = "";
	String year = "";
	String symbo = "";
	String SIC = "";
	String SICName = "";
	int wordCount = 0;
	HashMap<String, Integer> keywords = new HashMap<String, Integer>();
	
	public HashMap<String, Integer> getKeywords() {
		return keywords;
	}
	public void setKeywords(HashMap<String, Integer> keywords) {
		this.keywords = keywords;
	}
	public String getDocumentType() {
		return documentType;
	}
	public void setDocumentType(String documentType) {
		this.documentType = documentType;
	}
	public String getUrl() {
		return url;
	}
	public void setUrl(String url) {
		this.url = url;
	}
	public String getRiskFactor() {
		return riskFactor;
	}
	public void setRiskFactor(String riskFactor) {
		this.riskFactor = riskFactor;
	}
	public String getCompanyName() {
		return companyName;
	}
	public void setCompanyName(String companyName) {
		this.companyName = companyName;
	}
	public String getYear() {
		return year;
	}
	public void setYear(String year) {
		this.year = year;
	}
	public String getSymbo() {
		return symbo;
	}
	public void setSymbo(String symbo) {
		this.symbo = symbo;
	}
	public String getSIC() {
		return SIC;
	}
	public void setSIC(String sIC) {
		SIC = sIC;
	}
	public String getSICName() {
		return SICName;
	}
	public void setSICName(String sICName) {
		SICName = sICName;
	}
	public int getWordCount() {
		return wordCount;
	}
	public void setWordCount(int wordCount) {
		this.wordCount = wordCount;
	}
	
	public String toString(){
		StringBuilder s = new StringBuilder();
		s.append("CompanyName:" + getCompanyName());
		s.append("\tdocType:" + getDocumentType());
		s.append("\triskFactor:" + getRiskFactor());
		return s.toString();
	}
}
