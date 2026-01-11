# Lab 01: Python Dictionary - Storing Disease Information

## 🎯 Learning Objectives

By the end of this lab, you will be able to:
- Create and manipulate Python dictionaries
- Access, add, and modify dictionary values
- Create a list of dictionaries
- Loop through dictionaries to display data

## ⏰ Time Allocation (3 hours)

| Activity | Duration |
|----------|----------|
| 🎯 Lecture & Slides | 30 min |
| 📖 Tutorial Notebook | 60 min |
| ☕ Break | 15 min |
| ✍️ Exercise Notebook | 45 min |
| 📤 Submit & Auto-grade | 15 min |
| 💬 Q&A | 15 min |

## 📁 Files in This Lab

```
template-lab01-dictionary/
├── README.md                    # This file
├── slides/
│   └── Lab01_Slides.tex        # Lecture slides (LaTeX Beamer)
├── tutorial/
│   └── Lab01_Tutorial.ipynb    # Learn step-by-step
├── exercise/
│   └── Lab01_Exercise.ipynb    # Complete the exercises
├── data/
│   └── diseases.md             # Sample disease data
└── tests/
    └── test_lab01.py           # Auto-grading tests
```

## 🚀 Getting Started

### Step 1: Open Tutorial Notebook
Start with `tutorial/Lab01_Tutorial.ipynb` to learn the concepts.

### Step 2: Complete Exercises
After finishing the tutorial, open `exercise/Lab01_Exercise.ipynb` and complete all 5 exercises.

### Step 3: Submit Your Work
```bash
git add .
git commit -m "Complete Lab 01"
git push
```

### Step 4: Check Your Score
Go to the **Actions** tab in your GitHub repository to see your auto-grading results.

## 📚 Key Concepts

### What is a Dictionary?
A dictionary stores data as **key-value pairs**, like a real dictionary where:
- **Key** = the word you look up
- **Value** = the definition

```python
# Example: Disease information
disease = {
    "name": "Rubella",           # key: "name", value: "Rubella"
    "symptoms": "fever, rash",   # key: "symptoms", value: "fever, rash"
    "treatment": "rest"          # key: "treatment", value: "rest"
}
```

### Why Use Dictionaries in RAG Systems?
In RAG (Retrieval-Augmented Generation) systems, we store documents as dictionaries:
- Easy to organize metadata
- Fast lookup by key
- Flexible structure for different document types

## 🏆 Grading

| Exercise | Points |
|----------|--------|
| Exercise 1: Create a dictionary | 20 |
| Exercise 2: Add a new key | 20 |
| Exercise 3: Access values | 20 |
| Exercise 4: Create list of dictionaries | 20 |
| Exercise 5: Loop through data | 20 |
| **Total** | **100** |

## 💡 Tips

- Read the tutorial carefully before starting exercises
- Test your code by running each cell
- Check the expected output format
- Don't hesitate to ask for help!

## 📖 Reference

- [Python Dictionary Documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- Disease data from: Generic-RAG/md_corpus/

---
**Course:** CSI403 - Full Stack Program Development  
**Lab:** 01 - Python Dictionary
