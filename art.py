#!/usr/bin/env python

from __future__ import print_function
import os

from PIL import Image

folders = ['change', 'landscapes', 'shadows', 'textures', 'window_view', 'other_abstraction']
links = ['          <h4><a href="%s.html">%s</a></h4>' % (x, ' '.join([y.title() for y in x.split('_')])) for x in folders]

header = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<!-- THIS PAGE IS AUTO GENERATED -->

  <head>

    <title>Iris Warchall: %%s</title>

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
	  <h3><a href="bio.html">About / Contact</a></h3>
          <h3>Art</h3>
%s
	</div>

	<div class="two-thirds" style="width: 660px; height: %%dpx">
''' % ('\n'.join(links))

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

for category in folders:

    images = sorted(os.listdir(category))

    with open('%s.html' % category, 'w') as fp:

        category_name = ' '.join([x.title() for x in category.split('_')])
        image_section = ['          <h1 style="margin: 10px">%s</h1>' % category_name]

        idx = 0
        height = 69
        for image in images:

            left = (idx % 2 == 0)

            if idx == 0:
                image_section.append(
                    '          <div class="imagerow" style="padding: 10px">')
            elif left:
                image_section.extend([
                    '          </div>',
                    '          <div class="imagerow">'])

            (x, y) = Image.open(category + '/' + image).size

            image_float = 'left' if left else 'right'

            if x > y:
                image_height = int((315.0 * y) / x)
                padding = (315 - image_height) / 2
                image_style = 'width="315px" style="margin-top: %dpx"' % padding
            else:
                image_style = 'height="315px"'
        
            image_section.extend([
                '            <div class="imagebox" style="float: %s">' % image_float,
                '              <a href="%s/%s">' % (category, image),
                '                <img src="%s/%s" class="grid" %s />' % (category, image, image_style),
                '                <h4 style="margin: 4px">%s</h4>' % ' '.join([x.title() for x in image[:-4].split('_')]),
                '              </a>',
                '            </div>',
            ])
        
            if left:
                height += 341

            idx += 1

        image_section.append('          </div>')
    
        print(header % (category_name, height), file=fp)

        print('\n'.join(image_section), file=fp)
    
        print(footer, file=fp)

