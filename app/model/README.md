# About /model/

The `` app/model/ `` implements the observer pattern. This means that the class must support adding, removing, and alerting observers. 

In this case, the model is completely independent of controllers and views. 

It is important that all registered observers implement a specific method that will be called by the
model when they are notified.

Your model may be doing database call and other API calls. 

You may also need to create a folder in `` /model/ ` and put in your model 
