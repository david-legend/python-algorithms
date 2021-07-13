# Largest Rectangle Under Skyline ✩

Write a function that takes in an array of positive integers representing the heights of adjacent buildings and returns the area of the largest rectangle that can be created by any number of adjacent buildings, including just one building. Note that all buildings have the same width of 1 unit.

For example, given buildings = [2, 1, 2], the area of the largest rectangle that can be

created is 3, using all three buildings. Since the minimum height of the three buildings is 1.you can create a rectangle that has a height of 1 and a width of 3 (the number of buildings). You could also create rectangles of area 2 by usi only the first building or the last building, but these clearly wouldn't be the largest rectangles. Similarly, you could create rectangles of area 2 by using the first and second building or the second and third building.

To clarify, the width of a created rectangle is the number of buildings used to create the rectangle, and its height is the height of the smallest building used to create it.

Note that if no rectangles can be created, your function should return

### Sample Input

`buildings =  [1, 3, 3, 2, 4, 1, 5, 3, 2]`

### Sample Output

`9`

`// Below is a visual representation of the sample input.`
`//                       `
`//              _        `
`//          _  | |       `
`//    _ _  | | | |_      `
`//   | | |_| | | | |_    `
`//  _| | | | |_| | | |   `
`// |_|_|_|_|_|_|_|_|_|   `