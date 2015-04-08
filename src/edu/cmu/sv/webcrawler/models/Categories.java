package edu.cmu.sv.webcrawler.models;

import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import com.mongodb.BasicDBList;
import com.mongodb.BasicDBObject;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.DBObject;

import edu.cmu.sv.webcrawler.util.MongoHelper;

public class Categories {
    Map<String, List<String>> categories;
    Map<String, Integer> map;
    DBCollection collection;
    String _id;

    public Categories() {
        categories = new HashMap<String, List<String>>();
        MongoHelper helper = new MongoHelper();
        this.collection = helper.getDb().getCollection("categories");
        readFromDb();
    }

    // generate categories map
    /*
     * { finacial: 5 law: 7 }
	 */
    public Categories(Map<String, Integer> keywordsMap) {
        categories = new HashMap<String, List<String>>();
        MongoHelper helper = new MongoHelper();
        this.collection = helper.getDb().getCollection("categories");
        readFromDb();
        this.map = new HashMap<String, Integer>();
        for (String key : categories.keySet()) {
            map.put(key, 0);
        }
        for (String key : keywordsMap.keySet()) {
            String cateKey = getCateKey(key);
            System.out.println(cateKey);
            if (cateKey != null) {
                map.put(cateKey, map.get(cateKey) + keywordsMap.get(key));
            }
        }
    }

    /**
     * @return the initMap
     */
    public Map<String, List<String>> getInitMap() {
        return categories;
    }

    private String getCateKey(String key) {
        for (String cateKey : this.categories.keySet()) {
            List<String> list = categories.get(cateKey);
            if (list.contains(key)) {
                System.out.println(cateKey);
                return cateKey;
            }
        }
        return null;
    }

    private void readFromDb() {
        BasicDBObject doc = new BasicDBObject();
        DBCursor cursor = this.collection.find(doc);
        try {
            while (cursor.hasNext()) {
                DBObject obj = cursor.next();
                for (String key : obj.keySet()) {
                    if (key.equals("_id")) {
                        this._id = doc.getString(key);
                        continue;
                    }
                    BasicDBList category = (BasicDBList) obj.get(key);
                    List<String> list = new ArrayList<String>();
                    for (Object s : category) {
                        list.add((String) s);
                    }
                    categories.put(key, list);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void load(InputStream is) {

        try {
            if (is != null) {
                InputStreamReader isr = new InputStreamReader(is);
                JSONParser parser = new JSONParser();
                JSONObject json = (JSONObject) parser.parse(isr);
                Iterator<?> iter = json.keySet().iterator();
                while (iter.hasNext()) {
                    String key = (String) iter.next();
                    JSONArray msg = (JSONArray) json.get(key);
                    List<String> list = new ArrayList<String>();
                    for (Object value : msg.toArray()) {
                        list.add((String) value);
                    }
                    categories.put(key, list);
                }
                System.out.println(categories);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        removeAll();
        save();
    }

    private void save() {
        BasicDBObject doc = new BasicDBObject();
        doc.put("_id", this._id);
        for (String key : this.categories.keySet()) {
            BasicDBList list = new BasicDBList();
            for (String value : this.categories.get(key)) {
                list.add(value);
            }
            doc.put(key, list);
        }
        this.collection.insert(doc);
    }

    private void removeAll() {
        BasicDBObject doc = new BasicDBObject();
        collection.remove(doc);
    }

    public Map<String, Integer> getMap() {
        return map;
    }

    public void insert(String category, String keyword) {
        List<String> keyword_list = this.categories.get(category);
        if (keyword_list.contains(keyword)) return;
        keyword_list.add(keyword);
        this.categories.put(category, keyword_list);
        removeAll();
        this.save();
    }

    public void remove(String category, String keyword) {
        List<String> keyword_list = this.categories.get(category);
        keyword_list.remove(keyword);
        this.categories.put(category, keyword_list);
        removeAll();
        this.save();
    }

}
