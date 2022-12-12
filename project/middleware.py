from ipware import get_client_ip
from datetime import datetime
# from .models import IpModel

ipSet = set()

def is_valid_ip(get_response):

	# ya recibe el request

	def middleware(request):
		
		ip = get_client_ip(request)
		ip_address = ip[0]
		print("ip: ", ip_address, "|| time:", datetime.now() )
		# get_ip= IpModel()

		# get_ip.ipAddress = ip[0]

		# get_ip.save()
		ipSet.add(ip_address)

		print("||||SAVING...||||")



		response = get_response(request)

		return response

	return middleware