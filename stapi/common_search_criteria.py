class CommonSearchCriteria:

	def __init__(self, pageNumber=0, pageSize=50, sort=None):
		self.pageNumber = pageNumber
		self.pageSize = pageSize
		self.sort = sort


# name,ASC;surname,DESC

        
        # def search(self, searchCriteria, pageNumber=0, pageSize=50):
        #     url_to_post = self.url + "/api/v1/rest/animal/search?pageNumber=1&pageSize=10"
        #     data_to_post = {"name" : searchCriteria}
        #     post_request = requests.post(url_to_post, data_to_post)
        #     response_text = post_request.text
        #     response_dict = loads(response_text)
        #     return response_dict
        #     