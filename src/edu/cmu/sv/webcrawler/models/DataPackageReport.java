package edu.cmu.sv.webcrawler.models;

import java.util.List;

public class DataPackageReport {
	private List<DataPackage> dataPackages;
	private int count;
	public DataPackageReport(List<DataPackage> dataPackages) {
		super();
		this.dataPackages = dataPackages;
		this.count = dataPackages.size();
	}
	public List<DataPackage> getDataPackages() {
		return dataPackages;
	}
	public int getCount() {
		return count;
	}
	public void setDataPackages(List<DataPackage> dataPackages) {
		this.dataPackages = dataPackages;
	}
	public void setCount(int count) {
		this.count = count;
	}
	@Override
	public String toString() {
		return "DataPackageReport [dataPackages=" + dataPackages + ", count="
				+ count + "]";
	}
	

}
