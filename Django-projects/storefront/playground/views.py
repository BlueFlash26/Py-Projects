from django.http import HttpResponse, request
from django.shortcuts import render
from django.views import generic, View
from html import escape

# Create your views here.
# request -> response
# request handler
# action
 
def say_hello(request):
    return render(request, 'hello.html', {'name': "BlueFlash"})

class GuessView(View):
    def checkGuess(self, guess):
        msg = False
        if guess:
            try:
                if int(guess) < 4:
                    msg = "Too low"
                elif int(guess) > 4:
                    msg = "Too high"
                else:
                    msg = "congratulations"
            except:
                msg = "Bad format for guess " + escape(guess)
        return msg
    
    def get(self, request):
        guess = request.GET.get('guess')
        x = {'guess': guess, 'message': self.checkGuess(guess)} 
        return render(request, 'guess.html', x)
    
    def post(self, request):
        guess = request.POST.get('guess')
        x = {'guess': guess, 'message': self.checkGuess(guess)} 
        return render(request, 'guess.html', x)

    
    def guess(request):
        return render(request, "guess.html")
