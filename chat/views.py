
# from django.shortcuts import render, redirect


# def chatPage(request, *args, **kwargs):
# 	if not request.user.is_authenticated:
# 		return redirect("login-user")
# 	context = {}
# 	return render(request, "/chat/chatPage.html", context)


# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect

# @login_required(login_url='login-user')  # Decorator to ensure user is logged in
# def chatPage(request, *args, **kwargs):
#     user = request.user  # Get the logged-in user object
#     first_name = user.first_name  # Fetch the first name of the user
#     context = {'first_name': first_name}  # Pass the first name to the context
#     return render(request, "chat/chatPage.html", context)
