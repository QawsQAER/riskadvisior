package edu.cmu.sv.webcrawler.models;

public class Tag {
	private String name;
	private int hotDegree;
	public Tag(String name) {
		super();
		this.name = name;
		this.hotDegree = 0;
	}
	public String getName() {
		return name;
	}
	public int getHotDegree() {
		return hotDegree;
	}
	public void setName(String name) {
		this.name = name;
	}
	public void setHotDegree(int hotDegree) {
		this.hotDegree = hotDegree;
	}
	@Override
	public String toString() {
		return "Tag [name=" + name + ", hotDegree=" + hotDegree + "]";
	}
	
}