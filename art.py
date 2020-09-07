#!/usr/bin/env python

from __future__ import print_function
import os

from PIL import Image

header = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<!-- THIS PAGE IS AUTO GENERATED -->

  <head>

    <title>Iris Warchall</title>

    <link rel="stylesheet" type="text/css" href="stylesheet.css" />


    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-177325233-1"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      
      gtag('config', 'UA-177325233-1');
    </script>
  </head>

  <body>

    <div id="wrapper">
      <div class="full">

	<div class="one-third" style="height: 300px">
	  <h1><a href="index.html">Iris Warchall</a></h1>
	  <h3><a href="art.html">Artwork</a></h3>
	  <h3><a href="bio.html">About / Contact</a></h3>
	</div>

	<div class="two-thirds" style="width: 660px; height: %dpx">
'''

footer = '''
	</div>

      </div>
    </div>

    <div id="bottom">
      <h5>
	&copy 2020 &mdash;
        <a href="mailto:info@iriswarchall.com">
	  Contact
	</a> 
	&mdash;
	<a href="https://www.instagram.com/iwarchall/">
	  Instagram
	</a>
      </h5>
    </div>

  </body>
</html>
'''

images = os.listdir('images')

with open('art.html', 'w') as fp:

    image_section = []

    idx = 0
    height = 10
    for image in images:

        left = (idx % 2 == 0)

        if idx == 0:
            image_section.append(
                '          <div class="imagerow" style="padding: 10px">')
        elif left:
            image_section.extend([
                '          </div>',
                '          <div class="imagerow">'])

        (x, y) = Image.open('images/' + image).size

        image_float = 'left' if left else 'right'

        if x > y:
            image_height = int((315.0 * y) / x)
            padding = (315 - image_height) / 2
            image_style = 'width="315px" style="margin-top: %dpx"' % padding
        else:
            image_style = 'height="315px"'
        
        image_section.extend([
            '            <div class="imagebox" style="float: %s">' % image_float,
            '              <a href="images/%s">' % image,
            '                <img src="images/%s" class="grid" %s />' % (image, image_style),
            '              </a>',
            '            </div>',
        ])
        
        if left:
            height += 325

        idx += 1

    image_section.append('          </div>')
    
    print(header % height, file=fp)

    print('\n'.join(image_section), file=fp)
    
    print(footer, file=fp)

