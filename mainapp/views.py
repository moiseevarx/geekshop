from django.shortcuts import render
import json, os

JSON_PATH = 'mainapp/json'

def loadMenuFromJSON():
    with open(os.path.join(JSON_PATH, 'menu.json'), 'r') as infile:
        return json.load(infile)

def main(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu, 'username': 'roksana', 'array': [1,2,3,4,5]}
    return render(request, 'mainapp/main.html', {'username': 'roxana'})

def products(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu}
    return render(request, 'mainapp/products.html')

def contacts(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu}
    return render(request, 'mainapp/contacts.html')