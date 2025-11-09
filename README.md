# To-Do List Application

A feature-rich command-line todo list application written in Python that helps you manage your tasks efficiently. The application follows Python best practices including PEP 8 style guide and PEP 257 docstring conventions.

## 🌟 Features

### Core Features
- Add, view, update, and delete tasks
- Mark tasks as complete/incomplete
- Filter tasks by status (pending/completed)
- Categorize tasks
- Set task priorities
- Add due dates
- Color coding support
- Task descriptions
- Full type hints support
- Comprehensive documentation

### Advanced Features
- 🔄 Sort tasks by:
  - Due date
  - Priority
  - Title
  - Category
  
- 📊 Task Statistics
  - Total tasks count
  - Completion rates
  - Distribution by priority
  - Distribution by category

- 🔍 Search Functionality
  - Search across titles
  - Search in descriptions
  - Search by category

- 📤 Export Options
  - CSV format (for spreadsheet analysis)
  - Text format (for readable backup)

## 🔧 Technical Specifications

### Code Structure
- Follows PEP 8 style guide
- Implements PEP 257 docstring conventions
- Uses Python type hints throughout
- Implements dataclasses for data management
- Uses enums for type safety
- Modular function design
- Comprehensive error handling

### Data Model
```python
@dataclass
class Task:
    title: str
    completed: bool = False
    priority: Priority = Priority.MEDIUM
    due_date: Optional[str] = None
    category: str = "general"
    description: Optional[str] = None
    color: Optional[str] = None
```

### Performance Features
- Dictionary-based lookups for efficiency
- Optimized task filtering
- Indexed task validation
- Efficient sorting mechanisms
- Smart data structures

### Code Quality
- Type-checked with proper annotations
- Comprehensive docstrings
- Error handling with specific exceptions
- Clear function signatures
- Consistent code style

## 📋 Usage Guide

### Task Priority Levels
```python
class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
```

### Task Display Format
```
1. ✅ 🔴 Example Task [category] 📅 2025-11-15
```

Icons:
- ✅ Completed task
- ❌ Pending task
- 🔴 High priority
- 🟡 Medium priority
- 🟢 Low priority

### Data Management
- Automatic backups with timestamps
- JSON storage format
- Data validation on save/load
- Error recovery mechanisms
- Backup restoration

## 💾 File Structure

- `todo.py` - Main application file
- `tasks.json` - Task storage file
- `.backups/` - Backup directory
- `tasks_export.csv` - CSV export file (when used)
- `tasks_export.txt` - Text export file (when used)

## 🔧 Development Standards

### Documentation
All functions follow PEP 257 docstring conventions:
```python
def function_name(param: type) -> return_type:
    """Short description.

    Detailed description if needed.

    Args:
        param: Parameter description.

    Returns:
        Description of return value.

    Raises:
        ExceptionType: Description of when this occurs.

    Note:
        Additional implementation notes.
    """
```

### Type Hints
All code uses proper type hints:
```python
from typing import List, Dict, Optional

def example_function(tasks: List[Task]) -> Optional[Dict[str, int]]:
    # Function implementation
```

## 🛠️ Future Improvements

1. Multiple todo lists
2. Subtasks support
3. Task reminders
4. Recurring tasks
5. Collaboration features
6. Task prioritization algorithm
7. Data visualization
8. Import functionality
9. Task templates
10. Task dependencies

## 🤝 Contributing

When contributing, please:
1. Follow PEP 8 style guide
2. Include proper type hints
3. Write comprehensive docstrings
4. Add tests for new features
5. Update documentation

## 📝 License

This project is open source and available under the MIT License.

## 🔨 Development Setup

1. Clone the repository
2. Ensure Python 3.7+ is installed
3. No additional dependencies required
4. Run `python todo.py`

## ✅ Code Quality Checks

The codebase maintains high quality through:
- Type checking compliance
- PEP 8 style guide adherence
- PEP 257 docstring conventions
- Comprehensive error handling
- Consistent code formatting
