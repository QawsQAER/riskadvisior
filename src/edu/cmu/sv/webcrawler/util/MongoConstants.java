package edu.cmu.sv.webcrawler.util;

public class MongoConstants {

	// local host mongo - no authentication required
//	public final static boolean USEAUTH = false;	
//	public final static String HOST = "127.0.0.1";
//	public final static int PORT = 27017;
//	public final static String DATABASE = "riskanalysis";
//	public final static String COLLECTIONS = "webcrawler";
//	public final static String USERNAME = "riskanalysis";
//	public final static String PASSWORD = "just4you";	

	// external mongolab, use authentication
//    public final static boolean USEAUTH = true;
//	public final static String HOST = "23.246.199.111";
//	public final static int PORT = 10026;
//	public final static String DATABASE = "db";
//	public final static String COLLECTIONS = "webcrawler";
//	public final static String USERNAME = "e8f0f844-da34-4c69-a5e3-559cfd15d666";
//	public final static String PASSWORD = "a2043e9b-6693-459b-a688-b58b6b681b46";	
	
	//mongolab
	public final static boolean USEAUTH = true;
	public final static String HOST = "mongodb://ds047591.mongolab.com";
	public final static int PORT = 47591;
	public final static String DATABASE = "bluemixdb";
	public final static String COLLECTIONS = "webcrawler";
	public final static String USERNAME = "123";
	public final static String PASSWORD = "123";
	
	
	// ds033699.mongolab.com:33699/riskanalysis -u <dbuser> -p <dbpassword>
	
	//no longer use
//	public final static String HOST = "23.20.33.31";
//	public final static int PORT = 53419;
//	public final static String DATABASE = "db";
//	public final static String COLLECTIONS = "webcrawler";
//	public final static String USERNAME = "gonghan";
//	public final static String PASSWORD = "123456";	

	// public final static String LOCALURL="mongodb://localhost/27017:db";
}


