package edu.cmu.sv.webcrawler.apis;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.nio.charset.Charset;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map.Entry;
import java.io.InputStream;

import javax.ws.rs.*;

import org.apache.commons.io.IOUtils;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
 
@Path("/parser")   //http://localhost:8080/webapi/parser
@Produces("text/plain")
public class TradeOffParser {

    @GET
    @Path("/allkey")
    @Produces("text/plain")
    public String get_allKey()
            throws JSONException {
        return "Need re-implement";
    }

    @POST
    @Path("/select")
    @Produces("application/json")
    @Consumes("text/plain")
    public Response get_seleKey(String incomingData)
            throws JSONException {

        JSONObject object = new JSONObject(incomingData);
        JSONArray companies = object.getJSONArray("companies");
        JSONArray keywords = object.getJSONArray("keywords");
        String year = object.getString("year");

        String subject = "Risk";

        JSONArray comp_data = new JSONArray();
        for(int i = 0; i < companies.length(); i++){
            JSONObject jo = crawl_generate(companies.getString(i), year);
            comp_data.put(jo);
        }

        JSONObject resd = new JSONObject();
        JSONArray columns = new JSONArray();

        HashMap<String, String> nk = new HashMap<String, String>();
        for(int i = 0; i < keywords.length(); i++){
            JSONObject tmpjo = new JSONObject();
            JSONObject tmpObject = keywords.getJSONObject(i);
            String cate = tmpObject.getString("category");
            tmpjo.put("key", cate);
            tmpjo.put("full_name", cate);
            tmpjo.put("type", "numeric");
            tmpjo.put("is_objective", "TRUE");
            tmpjo.put("goal", "MIN");
            columns.put(tmpjo);
            JSONArray keys = tmpObject.getJSONArray("factors");
            for(int j = 0; j < keys.length(); j++){
                nk.put(keys.getString(j), cate);
            }
        }

        resd.put("columns", columns);
        resd.put("subject", subject);

        JSONArray pd;
        pd = parser(comp_data, nk);
        resd.put("options", pd);
        return Response.ok(resd.toString()+"\n") //200
                .header("Access-Control-Allow-Origin", "*")
                .header("Access-Control-Allow-Methods", "GET, POST, DELETE, PUT")
                .allow("OPTIONS").build();
    }

    public JSONObject crawl_generate(String company_name, String year) throws JSONException{
        JSONObject json = new JSONObject();
        try {
            json = new JSONObject(
                IOUtils.toString(
                    new URL(
                        "http://riskanalysis.mybluemix.net/api/results/"+company_name+"?year="+year
                        ), Charset.forName("UTF-8")));
        } catch (Exception ex) {
            System.err.println(ex);
        }
        JSONArray ja = (JSONArray) json.get("records");
        if(ja.length()!=0){
            JSONObject rmDup = ja.getJSONObject(0);
            String comp = rmDup.getString("companyName");
            JSONObject ret = new JSONObject();
            rmDup.remove("riskFactor");
            ret.put("records", rmDup);
            ret.put("companyName", comp);
            return ret;
        }
        else{
            try{
                json = new JSONObject();
                URL tmp = new URL(
                    "http://riskanalysis.mybluemix.net/api/crawl/"+company_name+""
                    );
                JSONObject tmpJson = new JSONObject(
                    IOUtils.toString(
                        new URL(
                            "http://riskanalysis.mybluemix.net/api/results/"+company_name+"?year="+year
                            ), Charset.forName("UTF-8")));
                JSONObject rmDup = tmpJson.getJSONArray("records").getJSONObject(0);
                rmDup.remove("riskFactor");
                json.put("companyName", rmDup.getString("companyName"));
                json.put("records", rmDup);
            } catch (Exception ex) {
                System.err.println(ex);
            }
            return json;
        }
    }


    public HashMap<String, Integer> filter_keyswords(HashMap<String, Integer> keywords, HashMap<String, String> filter_set){
        HashMap<String, Integer> filteredKeys = new HashMap<String, Integer>();
        for(String val: filter_set.values()){
            filteredKeys.put(val, 0);
        }
        for(Entry<String, Integer> entry : keywords.entrySet()){
            if(filter_set.containsKey(entry.getKey())){
                String cate = filter_set.get(entry.getKey());
                filteredKeys.put(cate, filteredKeys.get(cate)+entry.getValue());
            }
        }
        return filteredKeys;
    }

    public JSONArray parser(JSONArray d, HashMap<String, String> nk) throws JSONException{
        JSONArray options = new JSONArray();
        int index = 0;
        for(int i = 0; i < d.length(); i++){
            JSONObject data = d.getJSONObject(i);
            JSONObject entry = data.getJSONObject("records");
            JSONObject valuesJSON = entry.getJSONObject("keywords");
            HashMap<String, Integer> values = new HashMap<String, Integer>();
            Iterator keys = valuesJSON.keys();
            while(keys.hasNext()){
                String key = (String) keys.next();
                values.put(key, Integer.parseInt(valuesJSON.get(key).toString()));
            }
            values = filter_keyswords(values, nk);
            JSONObject ele = new JSONObject();
            ele.put("key", String.valueOf(index));
            ele.put("name",data.get("companyName"));
            ele.put("values", values);
            ele.put("description_html", "Risk Advisor feat. TradeOff Analysis");
            options.put(ele);
            index += 1;
        }
        return options;
    }
}
