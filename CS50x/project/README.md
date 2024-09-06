TODO
# To-Do List CLI

#### Video Demo:  <https://youtu.be/j85BswTslzs>

#### Description:

A simple command-line interface (CLI) for managing a to-do list provides a streamlined and efficient way to handle your tasks. This CLI tool is designed to facilitate the management of to-dos with a unique identifier for each task, making it easy to track and organize them. The system relies on a JSON file for storing the details of the to-dos and a text file to keep track of the last used ID, ensuring that each new to-do receives a distinct and non-repeating identifier.

The core functionality of this CLI includes several key features:

- Add: Users can add new to-dos to their list, each with a unique ID. This feature is essential for expanding your task list, and the unique ID helps in keeping track of each item independently. For instance, when you add a to-do item such as "Buy groceries," the system assigns it a unique ID, ensuring that it can be referenced or modified separately from other tasks.

- Display: The CLI allows you to display all current to-dos in a clear and organized manner. This feature is crucial for reviewing your tasks at a glance. By executing a simple command, users can see the full list of their to-dos, including their unique IDs and descriptions, which helps in managing and prioritizing tasks more effectively.

- Update: Existing to-dos can be updated to reflect changes or corrections. Whether you need to amend a typo or update the description of a task, this feature provides a way to modify the text of any to-do. For example, if you initially added "Buy groceries" but later decided to change it to "Buy vegetables," the update functionality allows you to make this change without having to remove and re-add the task.

- Delete: Users can delete specific to-dos by their text. This functionality is useful for removing completed or irrelevant tasks from your list. When a task is deleted, the system automatically adjusts the IDs of remaining tasks to maintain sequential order and updates the text file that tracks the last used ID. This ensures that the to-do list remains clean and organized, without any gaps or inconsistencies in the task IDs.

The **purpose** of the To-Do List CLI is to provide a simple yet effective solution for task management, especially in environments where users prefer a command-line interface over a graphical user interface. In a world filled with numerous tasks and responsibilities, staying organized can be a significant challenge. This CLI tool aims to address that challenge by offering a streamlined and user-friendly method for managing to-dos. It is particularly suitable for users who appreciate the efficiency and minimalism of command-line operations, as well as for those seeking a lightweight solution that avoids the complexity of more elaborate task management software.

The project comprises several important **files**:

- **index.js:** This is the primary script file where the main functionality of the CLI is implemented. It incorporates external libraries such as "Commander" and "Chalk." The Commander library is used to handle command-line arguments and facilitate the execution of commands such as add, delete, update, and display. It also provides a built-in help feature, accessible via the -h flag. The Chalk library is used to add color and improve the readability of the command-line output, enhancing the user experience by making the interface more visually appealing and easier to navigate.

- **package.json:** This file is created by default when initializing a Node.js project. It serves as a manifest for the project, listing all the external libraries and dependencies required for the CLI to function correctly. By running the npm install command, users can install all the necessary packages as specified in this file, ensuring that the project has access to all required libraries and can run smoothly.

- **todoID.txt:** This text file is used to keep track of the last used ID for to-dos. It plays a crucial role in ensuring that each new to-do receives a unique identifier. By recording the most recent ID, the system can generate a new, sequential ID for each subsequent to-do, preventing any duplication and maintaining the integrity of the task management system.

- **todos.json:** This JSON file acts as the database for storing all to-dos. It contains an array of to-do objects, each with its unique ID and description. The use of JSON allows for structured and easily manageable data storage, making it straightforward to read, write, and update task information. This file ensures that all to-do items are preserved between sessions and can be accessed or modified as needed.

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. **Install Dependencies:**
    Make sure you have Node.js installed. Then, run the following command:
   ```bash
   npm install

3. **Create Necessary files:**
    Run following commands if you don't have todoID.txt or todos.json files:
   ```bash
   echo "[]" > todos.json
   echo "0" > todoID.txt

# Usage
1. **Adding a To-do**
    Add a new to-do item to your list. Each to-do will have a unique ID.

   ```bash
    node index.js add "Buy groceries"

2. **Displaying All To-dos**
    Display all to-dos stored in your list.

    ```bash
    node index.js display

3. **Updating a To-do**
    Update the text of an existing to-do.

    ```bash
    node index.js update "Buy groceries" "Buy vegetables"

4. **Deleting a To-do**
Delete a specific to-do by its text.

    ```bash
    node index.js delete "Buy vegetables"

This will remove the to-do with the text "Buy vegetables" from your list, decrement the IDs of all following to-dos, and update the todoID.txt file accordingly.
