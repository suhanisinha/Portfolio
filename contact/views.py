from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
	if request.method == 'POST':
		sender_message = request.POST['sender-message']
		sender_name = request.POST['sender-name']
		sender_email = request.POST['sender-email']

		send_mail(
			sender_name,
			sender_message,
			sender_email,
			['suhanisinha2181998@gmail.com'],
		)

		return render(request, 'index.html', {'sender_name': sender_name})

	else:
		return render(request, 'index.html', {})
