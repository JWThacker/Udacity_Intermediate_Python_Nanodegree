"""Creates an app that generates a meme given a file and a quote.

Creates a Flask app that either:

(1) Creates a randomly generated meme from module files

or

(2) Creates a meme from a user submitted URL
"""


import random
import os
import requests
from flask import Flask, render_template, request, flash, redirect, url_for
from MemeGenerator import MemeQuoteError


# @TODO Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeGenerator

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for quote_file in quote_files:
        quotes.extend(Ingestor.parse(quote_file))

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    img_url = request.form.get("image_url")
    try:
        response = requests.get(img_url, stream=True)
    except requests.exceptions.RequestException:
        flash("Please enter a valid Image URL!")
        return redirect(url_for("meme_form"))

    img_path = f"./img_{random.randint(0, 10000000)}.jpg"
    with open(img_path, "wb") as f:
        f.write(response.content)

    body = request.form.get("body", "")
    if body:
        body = f"'{body}'"
    author = request.form.get("author", "")
    quote = f'"{body}" - {author}'
    quote_obj = QuoteModel(quote)

    try:
        print(f'{quote_obj.body} - {quote_obj.author}')
        path = meme.make_meme(img_path, quote_obj.body, quote_obj.author)
    except MemeQuoteError:
        flash("Please enter a both a body and an author!")
        if os.path.exists(img_path):
            os.remove(img_path)
        return redirect(url_for("meme_form"))

    if os.path.exists(img_path):
        os.remove(img_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
