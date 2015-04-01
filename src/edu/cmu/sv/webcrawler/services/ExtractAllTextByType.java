package edu.cmu.sv.webcrawler.services;

import net.htmlparser.jericho.Source;

public class ExtractAllTextByType {
	public String extractAllText20F(String htmlText) {

		Source source = new Source(htmlText);

		String page = source.getTextExtractor().toString().toLowerCase().replaceAll(" +"," ");

		// System.out.println(page);

		boolean flag = true;

		int start = 0, start_risk = 0, end = 0, startItem4 = 0, see = 0, nextStart = 0;

		while (flag) {

			start = page.indexOf("item 3", start + 1);

			nextStart = page.indexOf("item 3", start + 1);

			see = page.indexOf("see", start - 20);

			startItem4 = page.indexOf("item 4", start + 1);

			start_risk = page.indexOf("risk factors", start + 1);

			if (start == -1 || start_risk == -1) {

				return null;

			}

			if (((startItem4 - start) < 120) || ((see != -1) && (start > see))
					|| ((nextStart != -1) && (nextStart < start_risk))

					|| ((start_risk - start) < 300)) {

				continue;

			}

			page = page.substring(start);

			end = page.indexOf("item 4");

			if (end == -1) {

				end = page.indexOf("item 4");

			}

			if (end > 100) {

				String input = page.substring(start_risk - start, end);

				return input;

			}

		}

		return null;

	}

	public String extractAllText10Q(String htmlText) {
		Source source = new Source(htmlText);
		String page = source.getTextExtractor().toString().toLowerCase();

		boolean flag = true;
		int start = 0, start_risk = 0, end = 0, startItem6 = 0, startItem2 = 0;
		while (flag) {
			start = page.indexOf("item 1a", start + 1);
			startItem6 = page.indexOf("item 6", start + 1);
			startItem2 = page.indexOf("item 2", start + 1);
			start_risk = page.indexOf("risk factors", start + 1);
			if (start == -1 || start_risk == -1) {
				return null;
			}
			if ((page.charAt(start + 7) != '.')
					|| (Math.abs(startItem6 - start) < 1000 || Math
							.abs(startItem2 - start) < 1000)) {
				continue;
			}
			if (startItem6 == -1)
				end = startItem2;
			else if (startItem2 == -1)
				end = startItem6;
			else
				end = Math.min(startItem6, startItem2);
			return page.substring(0, end);
		}
		return null;
	}

	public String extractAllText10K(String htmlText) {
		Source source = new Source(htmlText);
		String page = source.getTextExtractor().toString().toLowerCase();

		boolean flag = true;
		int start = 0, start_risk = 0, end = 0;
		while (flag) {
			start = page.indexOf("item 1a", start + 1);
			start_risk = page.indexOf("risk factors", start + 1);
			if (start == -1 || start_risk == -1) {
				return null;
			}
			if ((page.charAt(start - 1) != ' ' && page.charAt(start - 1) != '.')
					|| (page.charAt(start + 7) != ' ' && page.charAt(start + 7) != '.')
					|| (page.charAt(start_risk - 1) != ' ' && page
							.charAt(start_risk - 1) != '.')
					|| start_risk - start > 20) {
				System.out.println("start:" + start + " start_risk:"
						+ start_risk);
				continue;
			}
			page = page.substring(start);
			end = page.indexOf("unresolved staff comments");
			if (end == -1) {
				end = page.indexOf("unregistered sales");
			}
			if (end > 100) {
				String input = page.substring(0, end + 10);

				/*
				 * int length = input.length(); int counter = 0;
				 * 
				 * StringBuilder result = new StringBuilder();
				 * 
				 * while (counter + 1000 < length) { String inputPart =
				 * input.substring(counter, counter + 1000); counter += 1000;
				 * 
				 * List<NameValuePair> qparams = new ArrayList<NameValuePair>();
				 * qparams.add(new BasicNameValuePair("txt", inputPart ));
				 * qparams.add(new BasicNameValuePair("sid", "ie-en-news" ));
				 * qparams.add(new BasicNameValuePair("rt","xml" ));
				 * 
				 * String username = "c1710f29-e0e3-4536-a46c-1d28f482c850";
				 * String password = "UVUlkPTUOb5j"; String baseURL =
				 * "https://gateway.watsonplatform.net/laser/service/api/v1/sire/193edf4a-c102-4619-9100-28bc95ffa435"
				 * ;
				 * 
				 * Executor executor = Executor.newInstance().auth(username,
				 * password); String auth = username + ":" + password;
				 * 
				 * String response = null;
				 * 
				 * try { URI serviceURI = new URI(baseURL).normalize();
				 * 
				 * byte[] responseB = executor.execute(Request.Post(serviceURI)
				 * .addHeader("Authorization", "Basic "+
				 * Base64.encodeBase64String(auth.getBytes()))
				 * .bodyString(URLEncodedUtils.format(qparams, "utf-8"),
				 * ContentType.APPLICATION_FORM_URLENCODED)
				 * ).returnContent().asBytes();
				 * 
				 * response = new String(responseB, "UTF-8");
				 * 
				 * DocumentBuilderFactory dbf =
				 * DocumentBuilderFactory.newInstance(); DocumentBuilder db =
				 * dbf.newDocumentBuilder(); InputSource is = new InputSource();
				 * is.setCharacterStream(new StringReader(response));
				 * 
				 * Document document = db.parse(is);
				 * document.getDocumentElement().normalize();
				 * 
				 * NodeList nodes = document.getElementsByTagName("mention");
				 * 
				 * for (int i = 0; i < nodes.getLength(); i++) { Node node =
				 * nodes.item(i); String value = node.getTextContent();
				 * result.append(value); result.append(" "); } } catch
				 * (Exception e) {
				 * 
				 * } }
				 * 
				 * String inputPart = input.substring(counter, length);
				 * 
				 * List<NameValuePair> qparams = new ArrayList<NameValuePair>();
				 * qparams.add(new BasicNameValuePair("txt", inputPart ));
				 * qparams.add(new BasicNameValuePair("sid", "ie-en-news" ));
				 * qparams.add(new BasicNameValuePair("rt","xml" ));
				 * 
				 * String username = "c1710f29-e0e3-4536-a46c-1d28f482c850";
				 * String password = "UVUlkPTUOb5j"; String baseURL =
				 * "https://gateway.watsonplatform.net/laser/service/api/v1/sire/193edf4a-c102-4619-9100-28bc95ffa435"
				 * ;
				 * 
				 * Executor executor = Executor.newInstance().auth(username,
				 * password); String auth = username + ":" + password;
				 * 
				 * String response = null;
				 * 
				 * try { URI serviceURI = new URI(baseURL).normalize();
				 * 
				 * byte[] responseB = executor.execute(Request.Post(serviceURI)
				 * .addHeader("Authorization", "Basic "+
				 * Base64.encodeBase64String(auth.getBytes()))
				 * .bodyString(URLEncodedUtils.format(qparams, "utf-8"),
				 * ContentType.APPLICATION_FORM_URLENCODED)
				 * ).returnContent().asBytes();
				 * 
				 * response = new String(responseB, "UTF-8");
				 * 
				 * DocumentBuilderFactory dbf =
				 * DocumentBuilderFactory.newInstance(); DocumentBuilder db =
				 * dbf.newDocumentBuilder(); InputSource is = new InputSource();
				 * is.setCharacterStream(new StringReader(response));
				 * 
				 * Document document = db.parse(is);
				 * document.getDocumentElement().normalize();
				 * 
				 * NodeList nodes = document.getElementsByTagName("mention");
				 * 
				 * for (int i = 0; i < nodes.getLength(); i++) { Node node =
				 * nodes.item(i); String value = node.getTextContent();
				 * result.append(value); result.append(" "); }
				 * 
				 * } catch (Exception e) {
				 * 
				 * }
				 */

				// return result.toString();
				return input;
			}
		}
		return null;
	}
}
