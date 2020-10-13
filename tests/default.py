import multisparkle

multisparkle.generate(
    width = 1920,
    height = 1080,
    fname = "sparkle.png",

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
).save("sparkle.png")
