from django.shortcuts import render

#Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Friend:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

friends = [
  Friend('Tyson', 'Lab', 'Very energetic dog who loves you', 15),
  Friend('Tabby', 'Tortoise shell', 'Four little black monster that will attack your feet', 0),
  Friend('Leah', 'Mini Pinsch', 'Golden Dark Brown Queen', 4)
]

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def friends_index(request):
    return render(request, 'friends/index.html', {'friends': friends})