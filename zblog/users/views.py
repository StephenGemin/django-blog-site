from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, UpdateView

from .forms import UserRegisterForm
from .models import Profile


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created. You are now able to log in"
            )
            return redirect("user-login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", context={"form": form})


# Function view approach for the class below.
# @login_required
# def profile(request):
#     if request.method == "POST":
#         u_form = UserUpdateForm(data=request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(
#             data=request.POST, files=request.FILES, instance=request.user.profile
#         )
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(
#                 request, f"Your profile information was successfully updated"
#             )
#             return redirect("user-profile")
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {"u_form": u_form, "p_form": p_form}
#     return render(request, "users/profile.html", context=context)
class UserProfileView(LoginRequiredMixin, TemplateView):
    model = Profile
    template_name = "users/profile.html"


class UserLoginAndSecurityView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile_login_security.html"


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "users/profile_update_form.html"
    model = Profile
    fields = ("hobbies", "image")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(
            self.request, f"Your profile information was successfully updated"
        )
        return super().form_valid(form)

    def get_object(self):
        return Profile.objects.get(pk=self.request.user.profile.id)
