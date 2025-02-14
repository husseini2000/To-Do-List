# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:40:52 2025

@author: makka
"""

import json

# File to store tasks
TASK_FILE = "tasks.json"


def load_tasks():
  try:
    with(open(TASK_FILE, "r")) as f:
      return json.load(f)
  except (FileNotFoundError, json.JSONDecodeError):
    return []

def save_tasks(tasks):
  try:
    with(open(TASK_FILE, "w")) as f:
      json.dump(tasks, f, indent=4)
  except Exception as e:
    print(f"Error saving tasks: {e}")
    

def display_menu():
  print("\n📌 TO-DO LIST 📌")
  print("1. Add a task")
  print("2. View tasks")
  print("3. Mark task as completed")
  print("4. Delete a task")
  print("5. Update task")
  print("6. Load tasks")
  print("7. Exit")


def view_tasks(tasks):
  if not tasks:
    print("\n❌ No tasks in your list!")
  else:
    print("\n📋 Your To-Do List:")
    for i, task in enumerate(tasks, start=1):
      status = "✅" if task["completed"] else "❌"
      print(f"{i}. {status} {task['title']}")


def add_task(tasks):
  task = input("Enter the task: ").strip()
  if not task:
    raise ValueError("⚠️Task cannot be empty.")
  if any(t['title'].lower() == task.lower() for t in tasks):
    print("Task already exists.")
    return
  if task:
    tasks.append({"title": task, "completed": False})
    save_tasks(tasks)
    print(f"✅ Task '{task}' added successfully!")
  else:
    print(f"❌ Task '{task}' not added.")

def delete_task(tasks):
  view_tasks(tasks)
  try:
    task_num = int(input("\nEnter task number to remove: ")) - 1
    if 0 <= task_num < len(tasks):
        removed = tasks.pop(task_num)
        save_tasks(tasks)
        print(f"✅ Removed task: {removed['title']}")
    else:
        print("⚠️ Invalid task number!")
  except ValueError:
    print("⚠️ Please enter a valid number!")
  
def update_task(tasks):
  if not tasks:
    print("\n❌ No tasks in your list!")
    return
    
  view_tasks(tasks)
  try:
    task_num = int(input("\nEnter task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
      new_title = input("Enter new task title: ").strip()
      if not new_title:
          print("⚠️ Task title cannot be empty!")
          return

      if any(t["title"].lower() == new_title.lower() for t in tasks):
          print("⚠️ Task already exists. Choose a different name.")
          return

      tasks[task_num]["title"] = new_title
      save_tasks(tasks)
      print(f"✅ Task {tasks[task_num]['title']} updated successfully!")
    else:
      print("⚠️ Invalid task number!")
  except ValueError:
    print("⚠️ Please enter a valid number!")

def mark_task_complete(tasks):
    if not tasks:
        print("\n❌ No tasks to mark as completed!")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            save_tasks(tasks)
            print("✅ Task marked as completed!")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

def main():
  tasks = load_tasks()
  while True:
    display_menu()
    choice = input("Enter your choice: ").strip()
    if choice == "1":
      add_task(tasks)
    elif choice == "2":
      view_tasks(tasks)
    elif choice == "3":
      mark_task_complete(tasks)
    elif choice == "4":
      delete_task(tasks)
    elif choice == "5":
      update_task(tasks)
    elif choice == "6":
      tasks = load_tasks()  # Update the local tasks list
      print("✅ Tasks loaded successfully!")
    elif choice == "7":
      print("Exiting the program...")
      break
    else:
      print("⚠️Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
    