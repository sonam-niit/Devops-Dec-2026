# Background and Foreground Process

- Foreground: A processes which takes control of your terminal.
- Background: A processes which run without blocking your terminal.

- Let's say one of my code needs delay for 60 seconds, but i don't want to wait for 60 sec, so i can put that process in background

```bash
sleep 60 & # sleep for 60 seconds in background

jobs # show you process running in backgroud
# this is not blocking your terminal

ping google.com # this is forground process
# if i want to use terminal then i need to stop this using ctrl+c

# let's understand fg and bd
sleep 120 & # run in background
jobs # check background jobs
fg %1 # get background job in foreground
ctrl+z to stop running job
jobs # you can see background process stoppen
bg # it will resume job in background only
kill %1 # will kill process

# also once you get job from back to forground
# if you do ctrl+c that will also kill process
```