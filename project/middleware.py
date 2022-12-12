from ipware import get_client_ip

def is_valid_ip(get_response):

	# ya recibe el request

	def middleware(request):
		
		ip = get_client_ip(request)

		print("ip: ", ip)

		response = get_response(request)

		return response

	return middleware