import sys;
import json;

if __name__ == "__main__":
	filepath = sys.argv[1];
	output_path = sys.argv[2];
	f_input = open(filepath,"r");
	f_output = open(output_path,"w");
	data = dict();
	symbol_list = list()
	for line in f_input:
		line = line[:-1];
		symbol_list.append(line);
	data["symbol_list"] = symbol_list
	print symbol_list;
	json.dump(data,f_output);
	f_input.close();
	f_output.close();