from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfilForm


@login_required
def profil(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST,
                          request.FILES,
                          instance=request.user.profil)
        if form.is_valid():
            form.save()
    else:
        form = ProfilForm(instance=request.user.profil)

    return render(request, 'profil.html', {'form': form})
