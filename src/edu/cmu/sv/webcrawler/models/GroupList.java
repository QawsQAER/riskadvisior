package edu.cmu.sv.webcrawler.models;

import java.util.List;

public class GroupList {
	List<String> groupList;
	int count;
	public List<String> getGroupList() {
		return groupList;
	}
	public int getCount() {
		return count;
	}
	public void setGroupList(List<String> groupList) {
		this.groupList = groupList;
	}
	public void setCount(int count) {
		this.count = count;
	}
	@Override
	public String toString() {
		return "GroupList [groupList=" + groupList + ", count=" + count + "]";
	}
	public GroupList(List<String> groupList) {
		super();
		this.groupList = groupList;
		this.count = (groupList==null)?0:groupList.size();
	}
	
}
