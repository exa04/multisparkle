# ✨multisparkle✨

Generates sparkles with the PIL library for Python.

## Syntax

### multisparkle.sparkle(rayWidth, srayWidth, srayshortness, middleRadius, softness)

Returns one sparkle of 400x400 pixels, PIL image (RGBA)

| Parameter     | Description                                       |
| ------------- | ------------------------------------------------- |
| rayWidth      | Width of the main (horizontal and vertical) rays  |
| srayWidth     | Width of the secondary (45° rotated) rays         |
| srayshortness | Factor by which the secondary rays are decreased  |
| middleRadius  | Radius of the circle at the center of the sparkle |
| softness      | Blur radius                                       |

### multisparkle.generate()

Returns a PIL Image (RGBA) with multiple sparkles

| Parameter                         | Description                                                               |
| --------------------------------- | ------------------------------------------------------------------------- |
| width                             | Width of the output image                                                 |
| height                            | Height of the output image                                                |
| fname                             | Filename of the output image                                              |
| size                              | Minimum size of all sparkles                                              |
| variation                         | Amount of variation in size                                               |
| count                             | Amount of sparkles                                                        |
| sparkle_main_width                | Width of the main (horizontal and vertical) rays                          |
| sparkle_secondary_width           | Width of the secondary (45° rotated) rays                                 |
| sparkle_secondary_shortness       | Factor by which the secondary rays are decreased                          |
| sparkle_middle_width              | Radius of the circle at the center of the sparkles                        |
| sparkle_blur                      | Blur radius                                                               |
| fg_size                           | Minimum size of foreground sparkles                                       |
| fg_variation                      | Amount of variation in foreground sparkles' size                          |
| fg_count                          | Amount of foreground sparkles                                             |
| fg_sparkle_main_width             | Width of the main (horizontal and vertical) rays of foreground sparkles   |
| fg_sparkle_secondary_width        | Width of the secondary (45° rotated) rays of foreground sparkles          |
| fg_sparkle_secondary_shortness    | Factor by which the secondary rays of foreground sparkles are decreased   |
| fg_sparkle_middle_width           | Radius of the circle at the center of foreground sparkles                 |
| fg_sparkle_blur                   | Blur radius                                                               |
