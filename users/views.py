from django.contrib.auth.hashers import make_password
from .forms import UserAddForm, UserUpdateForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.views import View
from .models import User


# Show All Users
class AllUser(View):

    def get(self, request):
        users = User.objects.all()
        context = {
            'users': users
        }
        return render(request, 'users/index.html', context)


# Add new user
class AddUser(View):

    def get(self, request):
        data = UserAddForm()
        return render(request, 'users/add.html', {'forms': data})

    def post(self, request):
        form = UserAddForm(request.POST)
        if form.is_valid():
            try:
                user = User()
                user.name = request.POST['name']
                user.email = request.POST['email']
                user.password = make_password(request.POST['password'])
                user.save()
                messages.success(request, 'User has been created successfully', extra_tags='alert-success')

            except:
                messages.error(request, 'something went\'s wrong', extra_tags='alert-danger')

        else:
            context = {
                "forms": form
            }
            return render(request, 'users/add.html', context)

        return HttpResponseRedirect('/users/index')


# Change/Update User
class ChangeUser(View):

    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        form = UserUpdateForm(initial={'name': user.name})
        context = {
            'user': user,
            'forms': form
        }
        return render(request, 'users/change.html', context)

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        form = UserUpdateForm(request.POST)

        if form.is_valid():
            try:
                user.name = request.POST['name']
                user.password = make_password(request.POST['password'])
                user.save()

                messages.success(request, 'User data has been updated successfully', extra_tags='alert-success')

            except:
                messages.error(request, 'something went\'s wrong', extra_tags='alert-danger')

        else:
            context = {
                'user': user,
                'forms': form
            }
            return render(request, 'users/change.html', context)

        return HttpResponseRedirect('/users/index')


# Delete User
class DeleteUser(View):

    def get(self, request, user_id):
        try:
            User.objects.filter(id=user_id).delete()
            messages.success(request, 'User data has been deleted successfully', extra_tags='alert-success')

        except:
            messages.error(request, 'Something went\'s wrong', extra_tags='alert-danger')

        return HttpResponseRedirect('/users/index')
