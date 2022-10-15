# Challenge 1

## Challenge:
There are 100 doors in a row that are all initially closed. You make 100 passes by the doors.

The first time through, visit every door and toggle the door (if the door is closed, open it; if it is open, close it).

The second time, only visit every 2nd door (door #2, #4, #6, ...), and toggle it.

The third time, visit every 3rd door (door #3, #6, #9, ...)

Repeat until you only visit the 100th door.

Task: After all 100 passes, output the state of all the doors. Which are open, and which are closed?

## Plan:
1. Create a dict with the doors and their status'
2. Create a toggle function
3. Function for all doors to be toggled
4. Function that toggles every 2nd door
5. Function that toggles every 3rd door
6. Repeat the functions on lines 3, 4, 5 until i=100