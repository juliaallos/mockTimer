# Mock Trial Timer
## Julia Allos - Dartmouth Mock Trial Society
## 8/25/2025 

## What is Mock Trial
Mock Trial is an extracurricular activity where students dive deep into a fictional court case, preparing to act as attorneys and witnesses while practicing legal procedures, public speaking, and critical thinking.

## Purpose of this Project
In Mock Trial, different parts of the trial have time limits. Rather than using stopwatches where the times are easy to mess up or get confused, I wanted to create code that would allow members of the team to more easily time their materials in competition/practices

## Details of Project

This is a command-line timer application designed to help mock trial teams manage their speech and examination segments during scrimmages or tournaments.

The program is built using Python classes and provides the following features:

Custom Segments: Define an ordered list of trial segments (e.g., opening statements, directs, crosses) with customizable durations.

Live Countdown: Displays the current segment’s time remaining in MM:SS format, updating every second.

User Controls:
- Press Enter to skip to the next segment.
- Press B to go back to the previous segment.
- Press Q to quit the timer at any point.

Logging: Every second is logged to timer_log.txt for review or record-keeping.

Summary: At the end, the app prints out how much time remained for each segment.

This project is intentionally simple (no GUI), focusing on clarity and reusability. It can easily be adapted for different mock trial formats, speech events, or other timed competitions.


## Future Improvements/In the Works
I am still very early in creating this project, so there's a lot that needs to be improved.
- Pause/Resume function: Allow the timer to pause and resume without resetting the current segment during objections
- Cleaner display of time: Ensure the countdown prints consistently (no overlapping numbers or formatting glitches or saying 'skipped' when a few seconds have already passed).
- More Flexible Controls: Support additional commands (e.g., jump to a specific segment, extend/reduce time mid-run).
- eventually, GUI Version: Add a graphical interface for easier use during live trials.

## Things I know don't work
- Countdown Display: The seconds do not correctly countdown in the terminal. This is my priority to fix. Only the crosses section displays the time spent after clicking enter.
- Cannot be used by team yet since there is no pause feature
- The seconds countdown sometimes says "skipped" even when it has already been running for a few seconds. The overall time at the end still appears right, so this should be a quick fix
- Overall, there is A LOT of work to be done, and I"m hoping to continue developing in my free time!