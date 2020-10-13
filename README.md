# ✨multisparkle✨
Generates sparkles with the PIL library for Python.

## Examples

```py
import multisparkle

multisparkle.generate(
    width = 1000,
    height = 1000,
    count = 50,
    fg_count = 2    
).show()
```
A very basic example

```py
import multisparkle

multisparkle.generate(
    width = 500,
    height = 500,
    count = 1000,
    size = 5,
    variation = 10,
    fg_count = 0,
    sparkle_blur = [0,5]
).show()
```
Generates lots of small sparkles

```py
import multisparkle

multisparkle.generate(
    width = 1000,
    height = 1000,
    count = 200,
    size = 60,
    variation = 80,
    sparkle_main_width = [5, 15],
    sparkle_secondary_width = [2, 10],
    fg_count = 0,
    fg_sparkle_blur = 20,
    sparkle_middle_width = [100, 200]
).show()
```

## Syntax

### multisparkle.sparkle(rayWidth, srayWidth, srayshortness, middleRadius, softness)

Returns one sparkle of 400x400 pixels, PIL image (RGBA)

| Parameter     | Description                                       | Default Value |
| ------------- | ------------------------------------------------- | ------------- |
| rayWidth      | Width of the main (horizontal and vertical) rays  | 20            |
| srayWidth     | Width of the secondary (45° rotated) rays         | 10            |
| srayshortness | Factor by which the secondary rays are decreased  | 50            |
| middleRadius  | Radius of the circle at the center of the sparkle | 100           |
| softness      | Blur radius                                       | 5             |

### multisparkle.generate()

Returns a PIL Image (RGBA) with multiple sparkles. Sparkle-specific values are lists of a min and max value pair.

| Parameter                         | Description                                                                       | Default Value |
| --------------------------------- | --------------------------------------------------------------------------------- | ------------- |
| width                             | Width of the output image                                                         | 1920          |
| height                            | Height of the output image                                                        | 1080          |
| size                              | Minimum size of all sparkles                                                      | 5             |
| variation                         | Amount of variation in size                                                       | 50            |
| count                             | Amount of sparkles                                                                | 700           |
| sparkle_main_width                | Width of the main (horizontal and vertical) rays                                  | [10, 45]      |
| sparkle_secondary_width           | Width of the secondary (45° rotated) rays                                         | [2, 18]       |
| sparkle_secondary_shortness       | Factor by which the secondary rays are decreased in length                        | [30, 150]     |
| sparkle_middle_width              | Radius of the circle at the center of the sparkles                                | [0, 150]      |
| sparkle_blur                      | Blur radius                                                                       | [5, 8]        |
| fg_size                           | Minimum size of foreground sparkles                                               | 100           |
| fg_variation                      | Amount of variation in foreground sparkles' size                                  | 100           |
| fg_count                          | Amount of foreground sparkles                                                     | 10            |
| fg_sparkle_main_width             | Width of the main (horizontal and vertical) rays of foreground sparkles           | [5, 13]       |
| fg_sparkle_secondary_width        | Width of the secondary (45° rotated) rays of foreground sparkles                  | [3, 6]        |
| fg_sparkle_secondary_shortness    | Factor by which the secondary rays of foreground sparkles are decreased in length | [10, 70]      |
| fg_sparkle_middle_width           | Radius of the circle at the center of foreground sparkles                         | [20, 50]      |
| fg_sparkle_blur                   | Blur radius                                                                       | [2, 3]        |
