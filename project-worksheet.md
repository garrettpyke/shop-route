# Project Overview

## Project Links

- [TBD]()
- [TBD]()

## Project Description

My capstone SEI bootcamp project will be Shop-Route, a utility for shopping at a grocery store. The concept is an intelligent shopping list that will "route" the user through the store in order to maximize efficiency and save time. Most grocery shoppers would rather be spending their time elsewhere. 

The main user story is the typical shopper who traverses from one side of the store to the other, trying to be efficient while checking off items on their list. Unfortunately, as the list nears completion the shopper finds they forgot to get a certain produce item that happens to be at the far end of the store.

The application would likely require some initial setup by the user. The user could define how many aisles are in the store (preferably the store they normally frequent) and number them. The application will then section the aisle into 2 sides (left and right) and 3 parts (front, middle and back). For example, '3LM' would indicate aisle 3, left side, middle of the aisle. Assumptions will be made that adjacent aisles are facing each other and that the travel between the 2 facing aisles is minimal. 

The user will input a list of items, and the application will sort the list by location and display the location for each item. When the user is "checking off" an item, they will be able to enter its location if the application hasn't already "learned" it. 

Later versions could include more specific location information such as top or bottom rack. Another potential user story is the "I forgot the milk" situation when a person returns from shopping only to find they are out of a certain staple item. In this case, the application could use purchase history to remind the user that they may be low on a certain staple if they happen to be at the store now and the item is not on their list. The application could also be scoped out to include more than one store layout per shopper. Potential future updates:

1. More specific location information (top/bottom rack, etc.)
1. Feature to prevent the "I forgot the milk" situation as outlined above
1. Feature to save frequently used lists of staple items or ingredients for different recipes
1. The ability to save more than one set of locations (to support multiple stores) 

## Tech Stack: "PDRN"
- Back-end
	- Python
	- Django
- Front-end
	- React
	- Node.js

## Wireframes

Upload images of wireframe to cloudinary and add the link here with a description of the specific wireframe. Also, define the the React components and the architectural design of your app.

- [add link to your wireframes]()
- [add link to your react architecture]()


### MVP/PostMVP - 5min

The functionality will then be divided into two separate lists: MPV and PostMVP.  Carefully decided what is placed into your MVP as the client will expect this functionality to be implemented upon project completion.  

#### MVP
- Allow user to enter items and quantities on shopping list
- Display location of items
- If location of an item is not in DB, allow user to enter it and store in DB
- Sort items by location, and use a logical algorithm for picking items from the opposite aisles as the user moves down the aisle
- When an item has been "checked off", change font or remove from list
- Allow user to delete an item
- Enable user to clear entire list

#### PostMVP

- An edit page to allow for item locations to change
- More specific location information (upper/lower rack and more zones than front, middle & back)
- Classification of staple items and reminders based on purchase history when user is actively shopping and a certain item isn't on the current list
- Support for more than 1 store
- Graphical view of aisles & user's route through store

## Components
##### Writing out your components and its descriptions isn't a required part of the proposal but can be helpful.

Based on the initial logic defined in the previous sections try and breakdown the logic further into stateless/stateful components. 

| Component | Description | 
| --- | :---: |  
| App | This will make the initial data pull and include React Router| 
| Header | This will render the header include the nav | 
| Footer | This will render the header include the nav | 


Time frames are also key in the development cycle.  You have limited time to code all phases of the game.  Your estimates can then be used to evalute game possibilities based on time needed and the actual time you have before game must be submitted. It's always best to pad the time by a few hours so that you account for the unknown so add and additional hour or two to each component to play it safe. Also, put a gif at the top of your Readme before you pitch, and you'll get a panda prize.

| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Adding Form | H | 3hrs| 3.5hrs | 3.5hrs |
| Working with API | H | 3hrs| 2.5hrs | 2.5hrs |
| Total | H | 6hrs| 5hrs | 5hrs |

## Additional Libraries
 Use this section to list all supporting libraries and thier role in the project such as Axios, ReactStrap, D3, etc. 

## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of an a brief description.  Code snippet should not be greater than 10 lines of code. 

```
function reverse(string) {
	// here is the code to reverse a string of text
}
```
