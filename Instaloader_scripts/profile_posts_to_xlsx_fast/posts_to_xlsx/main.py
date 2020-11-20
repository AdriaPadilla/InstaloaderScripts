import time
import concurrent.futures
import query as q
import extractor as e
import export as x

profile_list = ["profile_name1", "profile_name2", "etc"] # Put here the username lists

def insta_request(profile_list):
	requested_data_list = []
	for user in profile_list:
		insta_response = q.request(user)
		requested_data_list.extend(insta_response)
	return requested_data_list

def extractor(requested_data):
	parsed_data_list = []
	print("------> Parsing responses to dictionary: | wait!")
	with concurrent.futures.ThreadPoolExecutor() as executor:
		parsed_data = executor.map(e.post_to_dict, requested_data)
		parsed_data_list.extend(parsed_data)
	return parsed_data_list

if __name__ == '__main__':

	start_time = time.time()

	requested_data = insta_request(profile_list)
	parsed_data = extractor(requested_data)
	x.framer(parsed_data)
	print("--- %s seconds ---" % (time.time() - start_time))
