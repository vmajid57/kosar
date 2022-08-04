from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View


from .forms import RegisterForm, LoginForm


def home(request):
    return render(request, 'account/home.html')


@login_required
def profile(request):
    return render(request, 'account/profile.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'} # TODO: what is initial???
    template_name = 'account/register.html'

    # TODO: read about dispatch function
    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


# TODO: add remember me
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'account/home.html'
    # TODO: why cant wtite template_name here and use self.template_name in render?

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        context = {'username': username}
        print("\n****", context, "********\n")
        # return redirect(to='/')
        # return render(self.request, 'account/profile.html', {'context': context})
        return super(CustomLoginView, self).form_valid(form)
