# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:40:52 2025

@author: Al-Husseini Rayan
"""

import json
import os
from datetime import datetime
from shutil import copy2
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum

class Priority(Enum):
    """Task priority levels.
    
    Enumeration of possible task priority levels from low to high.
    """
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

@dataclass
class Task:
    """A task in the todo list.
    
    Attributes:
        title (str): The task title.
        completed (bool): Whether the task is completed.
        priority (Priority): The task priority level.
        due_date (Optional[str]): The due date in YYYY-MM-DD format.
        category (str): The task category.
        description (Optional[str]): Additional task details.
        color (Optional[str]): Color code for visual representation.
    """
    title: str
    completed: bool = False
    priority: Priority = Priority.MEDIUM
    due_date: Optional[str] = None
    category: str = "general"
    description: Optional[str] = None
    color: Optional[str] = None
    
    def to_dict(self) -> Dict:
        data = asdict(self)
        data['priority'] = self.priority.value
        return data
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        if 'priority' in data:
            data['priority'] = Priority(data['priority'])
        return cls(**data)

# File to store tasks
TASK_FILE = "tasks.json"
BACKUP_DIR = ".backups"


def create_task_index(tasks: List[Task]) -> Dict[str, int]:
    """Create an index of task titles for faster lookups.
    
    Args:
        tasks: List of Task objects to index.
        
    Returns:
        A dictionary mapping lowercase task titles to their indices.
    """
    return {t.title.lower(): i for i, t in enumerate(tasks)}

def validate_task_title(title: str, tasks: List[Task], task_index: Optional[Dict[str, int]] = None) -> str:
    """Validate the task title and check for duplicates.
    
    Args:
        title: The task title to validate.
        tasks: List of existing tasks to check for duplicates.
        task_index: Optional pre-computed index of task titles for faster lookups.
    
    Returns:
        The validated and stripped title string.
        
    Raises:
        ValueError: If the title is empty or already exists.
    """
    if not title.strip():
        raise ValueError("⚠️ Task title cannot be empty.")
        
    # Use the index if provided, otherwise do a one-time check
    if task_index is not None:
        if title.lower() in task_index:
            raise ValueError("⚠️ Task already exists.")
    else:
        title_lower = title.lower()
        if any(t['title'].lower() == title_lower for t in tasks):
            raise ValueError("⚠️ Task already exists.")
    return title.strip()

def load_tasks() -> List[Task]:
    """Load tasks from the JSON file.
    
    Returns:
        A list of Task objects loaded from the JSON file.
        Returns an empty list if the file doesn't exist or is invalid.
    
    Note:
        Automatically adds default values for missing task fields.
    """
    try:
        with open(TASK_FILE, "r") as f:
            data = json.load(f)
            return [Task.from_dict(task_data) for task_data in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks: List[Task]) -> None:
    """Save tasks to file with automatic backup mechanism.
    
    Args:
        tasks: List of Task objects to save.
        
    Note:
        Creates a timestamped backup before saving.
        Attempts to restore from backup if save fails.
    """
    
    # Create backup
    if os.path.exists(TASK_FILE):
        backup_file = f"{TASK_FILE}.{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        try:
            copy2(TASK_FILE, backup_file)
        except Exception as e:
            print(f"⚠️ Warning: Could not create backup: {e}")
    
    try:
        with open(TASK_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print(f"❌ Error saving tasks: {e}")
        if os.path.exists(backup_file):
            try:
                copy2(backup_file, TASK_FILE)
                print("✅ Restored from backup.")
            except Exception as e:
                print(f"❌ Error restoring backup: {e}")
    

def display_menu() -> None:
    """Display the main menu options.
    
    Prints all available commands with their corresponding numbers.
    """
    print("\n📌 TO-DO LIST 📌")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. View pending tasks")
    print("4. View completed tasks")
    print("5. Toggle task completion")
    print("6. Delete a task")
    print("7. Update task")
    print("8. Filter by priority")
    print("9. Filter by category")
    print("10. Sort tasks")
    print("11. Show statistics")
    print("12. Search tasks")
    print("13. Export tasks")
    print("14. Exit")


def view_tasks(tasks: List[Task], filter_by: Optional[str] = None) -> None:
    """Display tasks with optional filtering.
    
    Args:
        tasks: List of Task objects to display.
        filter_by: Optional filter string in the format:
            - "completed" - show only completed tasks
            - "pending" - show only pending tasks
            - "priority:value" - show tasks with specific priority
            - "category:value" - show tasks in specific category
    
    Note:
        Uses dictionary-based filtering for efficiency.
        Shows task status, priority, title, category and due date.
    """
    if not tasks:
        print("\n❌ No tasks in your list!")
        return

    # Use dictionary-based filtering for better efficiency
    filter_funcs = {
        "completed": lambda tasks: {i: t for i, t in enumerate(tasks) if t["completed"]},
        "pending": lambda tasks: {i: t for i, t in enumerate(tasks) if not t["completed"]},
    }
    
    filtered_tasks = {}
    if filter_by:
        if filter_by in filter_funcs:
            filtered_tasks = filter_funcs[filter_by](tasks)
        elif filter_by.startswith(("priority:", "category:")):
            filter_type, value = filter_by.split(":")
            key = filter_type.rstrip(":")
            filtered_tasks = {i: t for i, t in enumerate(tasks) if t[key] == value}
    else:
        filtered_tasks = {i: t for i, t in enumerate(tasks)}

    if not filtered_tasks:
        print("\n❌ No tasks match your filter!")
        return
        
    # Pre-define constant mappings outside the loop
    priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}
    
    print("\n📋 Your To-Do List:")
    for i, task in filtered_tasks.items():
        status = "✅" if task["completed"] else "❌"
        priority = priority_icon.get(task["priority"], "⚪")
        due = f"📅 {task['due_date']}" if task["due_date"] else ""
        category = f"[{task['category']}]"
        print(f"{i + 1}. {status} {priority} {task['title']} {category} {due}")


def add_task(tasks: List[Task]) -> None:
    """Add a new task with user-provided details.
    
    Args:
        tasks: List of existing Task objects to append to.
    
    Note:
        Prompts user for:
        - Task title (required, must be unique)
        - Priority (1=Low, 2=Medium, 3=High)
        - Due date (optional, YYYY-MM-DD format)
        - Category (optional, defaults to "general")
        
    Automatically saves tasks after successful addition.
    """
    try:
        # Create index once for faster lookups
        task_index = create_task_index(tasks)
        
        title = input("Enter the task: ").strip()
        validate_task_title(title, tasks, task_index)
        
        # Get priority using predefined mapping
        print("\nPriority levels: 1=Low, 2=Medium, 3=High")
        priority = input("Enter priority (1-3) [2]: ").strip() or "2"
        priority_map = {"1": "low", "2": "medium", "3": "high"}
        if priority not in priority_map:
            raise ValueError("⚠️ Invalid priority level!")
            
        # Get due date
        due_date = input("Enter due date (YYYY-MM-DD) [optional]: ").strip()
        if due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("⚠️ Invalid date format! Use YYYY-MM-DD")
                
        # Get category
        category = input("Enter category [general]: ").strip() or "general"
        
        new_task = {
            "title": title,
            "completed": False,
            "priority": priority_map[priority],
            "due_date": due_date or None,
            "category": category
        }
        
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"✅ Task '{title}' added successfully!")
        
    except ValueError as e:
        print(str(e))

def delete_task(tasks: List[Task]) -> None:
    """Delete a task from the list.
    
    Args:
        tasks: List of Task objects to delete from.
        
    Note:
        Shows current tasks and prompts for task number.
        Automatically saves tasks after successful deletion.
    """
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"✅ Removed task: {removed.title}")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")
  
def update_task(tasks: List[Task]) -> None:
    """Update an existing task."""
    if not tasks:
        print("\n❌ No tasks in your list!")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to update: ")) - 1
        if not (0 <= task_num < len(tasks)):
            print("⚠️ Invalid task number!")
            return

        print("\nUpdate:")
        print("1. Title")
        print("2. Priority")
        print("3. Due date")
        print("4. Category")
        print("5. Description")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            new_title = input("Enter new title: ").strip()
            task_index = {t.title.lower(): i for i, t in enumerate(tasks) if i != task_num}
            validate_task_title(new_title, tasks, task_index)
            tasks[task_num].title = new_title
        
        elif choice == "2":
            print("\nPriority levels: 1=Low, 2=Medium, 3=High")
            priority = input("Enter priority (1-3): ").strip()
            priority_map = {"1": Priority.LOW, "2": Priority.MEDIUM, "3": Priority.HIGH}
            if priority not in priority_map:
                raise ValueError("⚠️ Invalid priority level!")
            tasks[task_num].priority = priority_map[priority]
        
        elif choice == "3":
            due_date = input("Enter due date (YYYY-MM-DD) [optional]: ").strip()
            if due_date:
                datetime.strptime(due_date, "%Y-%m-%d")
            tasks[task_num].due_date = due_date or None
        
        elif choice == "4":
            category = input("Enter new category: ").strip()
            if not category:
                raise ValueError("⚠️ Category cannot be empty!")
            tasks[task_num].category = category
        
        elif choice == "5":
            description = input("Enter new description [optional]: ").strip()
            tasks[task_num].description = description or None
        
        else:
            print("⚠️ Invalid choice!")
            return
        
        save_tasks([t.to_dict() for t in tasks])
        print("✅ Task updated successfully!")
        
    except ValueError as e:
        print(f"⚠️ {str(e)}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def toggle_task_completion(tasks: List[Task]) -> None:
    """Toggle the completion status of a task.
    
    Args:
        tasks: List of Task objects to modify.
        
    Note:
        Shows current tasks and prompts for task number.
        Toggles between completed and pending states.
        Automatically saves tasks after toggling.
    """
    if not tasks:
        print("\n❌ No tasks in your list!")
        return
        
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to toggle completion: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = not tasks[task_num]["completed"]
            status = "completed" if tasks[task_num]["completed"] else "pending"
            save_tasks(tasks)
            print(f"✅ Task marked as {status}!")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

def sort_tasks(tasks: List[Task]) -> None:
    """Sort tasks by various criteria."""
    print("\nSort by:")
    print("1. Due date")
    print("2. Priority")
    print("3. Title")
    print("4. Category")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        sorted_tasks = sorted(tasks, key=lambda x: x.due_date or "9999-99-99")
    elif choice == "2":
        priority_order = {Priority.HIGH: 0, Priority.MEDIUM: 1, Priority.LOW: 2}
        sorted_tasks = sorted(tasks, key=lambda x: priority_order[x.priority])
    elif choice == "3":
        sorted_tasks = sorted(tasks, key=lambda x: x.title.lower())
    elif choice == "4":
        sorted_tasks = sorted(tasks, key=lambda x: x.category.lower())
    else:
        print("⚠️ Invalid choice!")
        return
        
    view_tasks(sorted_tasks)

def show_statistics(tasks: List[Task]) -> None:
    """Display task statistics."""
    total = len(tasks)
    completed = sum(1 for t in tasks if t.completed)
    pending = total - completed
    
    by_priority = {p: sum(1 for t in tasks if t.priority == p) for p in Priority}
    by_category = {}
    for t in tasks:
        by_category[t.category] = by_category.get(t.category, 0) + 1
    
    print("\n📊 Task Statistics")
    print(f"Total tasks: {total}")
    completed_pct = (completed/total*100) if total > 0 else 0
    pending_pct = (pending/total*100) if total > 0 else 0
    print(f"Completed: {completed} ({completed_pct:.1f}%)")
    print(f"Pending: {pending} ({pending_pct:.1f}%)")
    
    print("\nBy Priority:")
    for p, count in by_priority.items():
        print(f"{p.value}: {count}")
    
    print("\nBy Category:")
    for cat, count in by_category.items():
        print(f"{cat}: {count}")

def search_tasks(tasks: List[Task]) -> None:
    """Search tasks by keyword."""
    keyword = input("Enter search term: ").strip().lower()
    if not keyword:
        print("⚠️ Search term cannot be empty!")
        return
        
    matches = [t for t in tasks if 
              keyword in t.title.lower() or 
              (t.description and keyword in t.description.lower()) or
              keyword in t.category.lower()]
              
    if matches:
        view_tasks(matches)
    else:
        print("❌ No matching tasks found!")

def export_tasks(tasks: List[Task]) -> None:
    """Export tasks to different formats."""
    print("\nExport format:")
    print("1. CSV")
    print("2. Text file")
    
    choice = input("Enter your choice: ").strip()
    
    try:
        if choice == "1":
            filename = "tasks_export.csv"
            with open(filename, 'w') as f:
                f.write("Title,Status,Priority,Due Date,Category,Description\n")
                for task in tasks:
                    status = "Completed" if task.completed else "Pending"
                    f.write(f'"{task.title}",{status},{task.priority.value},' +
                           f'"{task.due_date or ""}","{task.category}",' +
                           f'"{task.description or ""}"\n')
        elif choice == "2":
            filename = "tasks_export.txt"
            with open(filename, 'w') as f:
                for task in tasks:
                    status = "✅" if task.completed else "❌"
                    f.write(f"{status} {task.title}\n")
                    f.write(f"Priority: {task.priority.value}\n")
                    if task.due_date:
                        f.write(f"Due: {task.due_date}\n")
                    f.write(f"Category: {task.category}\n")
                    if task.description:
                        f.write(f"Description: {task.description}\n")
                    f.write("\n")
        else:
            print("⚠️ Invalid choice!")
            return
            
        print(f"✅ Tasks exported to {filename}")
    except Exception as e:
        print(f"❌ Error exporting tasks: {e}")

def main() -> None:
    """Main program loop.
    
    Loads tasks and runs the main menu loop until exit.
    Handles all user input and menu selections.
    Catches and reports any errors that occur during operation.
    """
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        try:
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                view_tasks(tasks, filter_by="pending")
            elif choice == "4":
                view_tasks(tasks, filter_by="completed")
            elif choice == "5":
                toggle_task_completion(tasks)
            elif choice == "6":
                delete_task(tasks)
            elif choice == "7":
                update_task(tasks)
            elif choice == "8":
                print("\nPriority levels: low, medium, high")
                priority = input("Enter priority to filter: ").strip().lower()
                if priority in ["low", "medium", "high"]:
                    view_tasks(tasks, filter_by=f"priority:{priority}")
                else:
                    print("⚠️ Invalid priority level!")
            elif choice == "9":
                category = input("Enter category to filter: ").strip().lower()
                view_tasks(tasks, filter_by=f"category:{category}")
            elif choice == "10":
                sort_tasks(tasks)
            elif choice == "11":
                show_statistics(tasks)
            elif choice == "12":
                search_tasks(tasks)
            elif choice == "13":
                export_tasks(tasks)
            elif choice == "14":
                print("👋 Goodbye!")
                break
            else:
                print("⚠️ Invalid choice. Please try again.")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            continue

if __name__ == "__main__":
  main()
    