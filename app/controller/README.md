# About /controller/

The `` app/controller/ `` class represents a controller implementation. Coordinates work of the view with the model.

The controller implements the strategy pattern. The controller connects to the view to control its actions.

Instead of implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to use

It does something like 
    View => `` controller `` => Model

It pokes it nose into the view and Model without actually knowing their implementations

You are likely to be doing validations and other checks of data from the view before selecting the kind of family of algorithms to branch into in your model

You would have to create a sub-folder in `` /controller/ `` to keep your controller in



    
