import { open } from 'node:fs/promises';

function isSafe(line) {
    line.sort()
}

var file = await open("src/day-02/input.txt")
var lines = []
for await (const line of file.readLines()) {
    lines.push(line)
}







console.log("hello")