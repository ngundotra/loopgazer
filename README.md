# LoopGazer
For creating loops that update an app!

This package has 1 purpose: update your phone about the status
of your Python loops. That's it folks.

Put your username and password in a {--TODO--} file, we'll securely 
use it to verify your loop updates on our servers before sending
you an update.

Corresponding iOS app to be launched soon.

-ngundotra


Examples:
```python
from loopgazer import Loop

# If your credentials are incorrect,
# a halting error will be thrown
Loop.config('usr_n_pwd.txt')

for i in Loop(range(5)):
    # Do something
    ...
    
```
On our side, we'll store your loop's progress, and let you
see the result.
```python
from loopgazer import WatchLoop



```