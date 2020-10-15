from __future__ import print_function
from PIL import Image, ImageFilter, ImageDraw
from random import randrange
import datetime
import time
import os

def sparkle(rayWidth = 20, srayWidth = 10, srayshortness = 50, middleRadius = 100, softness = 5):
    size = 400
    img = Image.new("RGBA", (size, size)) 

    # Middle

    middleGeoRadius = (size - middleRadius) / 2
    middleShape = [(middleGeoRadius, middleGeoRadius), (middleGeoRadius + middleRadius, middleGeoRadius + middleRadius)]

    middle = Image.new('RGBA', (size, size))
    mdraw = ImageDraw.Draw(middle)
    mdraw.ellipse(middleShape, 'white')
    img.paste(middle)
    img = img.filter(ImageFilter.GaussianBlur(radius = softness * 5))

    # Main rays

    rayA = [((size - rayWidth) / 2, softness), ((size + rayWidth) / 2, size - softness)]
    rayB = [(softness, (size - rayWidth) / 2), (size - softness, (size + rayWidth) / 2)] 

    img1 = ImageDraw.Draw(img)   
    img1.ellipse(rayA, "white") 
    img1.ellipse(rayB, "white") 

    # Secondary rays, rotated 45 degrees

    srayA = [((size - srayWidth) / 2, softness + srayshortness), ((size + srayWidth) / 2, size - softness - srayshortness)]
    srayB = [(softness + srayshortness, (size - srayWidth) / 2), (size - softness - srayshortness, (size + srayWidth) / 2 )] 

    overlay = Image.new('RGBA', (size, size))
    draw = ImageDraw.Draw(overlay)
    draw.ellipse(srayA, 'white')
    draw.ellipse(srayB, 'white')

    rotated = overlay.rotate(45, expand=True)
    img.paste(rotated, (-83, -83), rotated)

    # Blur

    img = img.filter(ImageFilter.BoxBlur(radius = softness))
    return img

def generate(
    width = 1920,
    height = 1080,

    size = 5,
    variation = 50,
    count = 700,

    sparkle_main_width = [10, 45],
    sparkle_secondary_width = [2, 18],
    sparkle_secondary_shortness = [30, 150],
    sparkle_middle_width = [0, 150],
    sparkle_blur = [5, 8],

    fg_size = 100,
    fg_variation = 100,
    fg_count = 10,

    fg_sparkle_main_width = [5, 13],
    fg_sparkle_secondary_width = [3, 6],
    fg_sparkle_secondary_shortness = [10, 70],
    fg_sparkle_middle_width = [20, 50],
    fg_sparkle_blur = [2, 3]
    ):

    result = Image.new("RGBA", (width, height), "black")

    for i in range(count):
        trans = Image.new("RGBA", (width, height))
        spsize = size + randrange(variation)
        img = sparkle(  randrange(sparkle_main_width[0], sparkle_main_width[1]),
                        randrange(sparkle_secondary_width[0], sparkle_secondary_width[1]),
                        randrange(sparkle_secondary_shortness[0], sparkle_secondary_shortness[1]),
                        randrange(sparkle_middle_width[0], sparkle_middle_width[1]),
                        randrange(sparkle_blur[0], sparkle_blur[1]),)

        img.thumbnail((spsize, spsize), Image.ANTIALIAS)
        x = randrange(-size-variation, width)
        y = randrange(-size-variation, height)
        w, h = img.size
        trans.paste(img, (x, y, x + w, y + h))
        result = Image.alpha_composite(result, trans)
        print('Added sparkle {4}/{5} at {0}, {1}, sized {2}x{3}'.format(x, y, w, h, i+1, count))

    for i in range(fg_count):
        trans = Image.new("RGBA", (width, height))
        spsize = fg_size + randrange(fg_variation)
        img = sparkle(  randrange(fg_sparkle_main_width[0], fg_sparkle_main_width[1]),
                        randrange(fg_sparkle_secondary_width[0], fg_sparkle_secondary_width[1]),
                        randrange(fg_sparkle_secondary_shortness[0], fg_sparkle_secondary_shortness[1]),
                        randrange(fg_sparkle_middle_width[0], fg_sparkle_middle_width[1]),
                        randrange(fg_sparkle_blur[0], fg_sparkle_blur[1]),)
        img.thumbnail((spsize, spsize), Image.ANTIALIAS)
        x = randrange(-size-variation, width)
        y = randrange(-size-variation, height)
        w, h = img.size
        print('Foreground sparkle {4}/{5} at {0}, {1}, sized {2}x{3}'.format(x, y, w, h, i+1, fg_count))
        trans.paste(img, (x, y, x + w, y + h))
        result = Image.alpha_composite(result, trans)
        
    return result
