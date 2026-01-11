"""
Lab 01: Python Dictionary - Auto-grading Tests
Course: CSI403 - Full Stack Program Development

This file contains tests for auto-grading the Lab 01 exercises.
Students should not modify this file.
"""

import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestExercise1:
    """Test Exercise 1: Create a Dictionary (20 points)"""
    
    def test_dengue_exists(self, student_namespace):
        """Test that dengue dictionary exists"""
        assert 'dengue' in student_namespace, "Variable 'dengue' not found"
    
    def test_dengue_is_dict(self, student_namespace):
        """Test that dengue is a dictionary"""
        assert isinstance(student_namespace.get('dengue'), dict), "'dengue' should be a dictionary"
    
    def test_dengue_name(self, student_namespace):
        """Test dengue name value"""
        dengue = student_namespace.get('dengue', {})
        assert dengue.get('name') == 'Dengue Fever', "name should be 'Dengue Fever'"
    
    def test_dengue_thai_name(self, student_namespace):
        """Test dengue thai_name value"""
        dengue = student_namespace.get('dengue', {})
        assert dengue.get('thai_name') == 'ไข้เลือดออก', "thai_name should be 'ไข้เลือดออก'"
    
    def test_dengue_symptoms(self, student_namespace):
        """Test dengue symptoms value"""
        dengue = student_namespace.get('dengue', {})
        assert dengue.get('symptoms') == 'high fever, headache', "symptoms should be 'high fever, headache'"
    
    def test_dengue_treatment(self, student_namespace):
        """Test dengue treatment value"""
        dengue = student_namespace.get('dengue', {})
        assert dengue.get('treatment') == 'rest, fluids', "treatment should be 'rest, fluids'"


class TestExercise2:
    """Test Exercise 2: Add a New Key (20 points)"""
    
    def test_prevention_key_exists(self, student_namespace):
        """Test that prevention key was added"""
        dengue = student_namespace.get('dengue', {})
        assert 'prevention' in dengue, "Key 'prevention' not found in dengue dictionary"
    
    def test_prevention_value(self, student_namespace):
        """Test prevention value"""
        dengue = student_namespace.get('dengue', {})
        assert dengue.get('prevention') == 'mosquito repellent', "prevention should be 'mosquito repellent'"
    
    def test_dengue_has_5_keys(self, student_namespace):
        """Test that dengue dictionary has 5 keys after adding prevention"""
        dengue = student_namespace.get('dengue', {})
        assert len(dengue) == 5, "dengue dictionary should have 5 keys"


class TestExercise3:
    """Test Exercise 3: Access Values (20 points)"""
    
    def test_disease_symptoms_exists(self, student_namespace):
        """Test that disease_symptoms variable exists"""
        assert 'disease_symptoms' in student_namespace, "Variable 'disease_symptoms' not found"
    
    def test_disease_symptoms_value(self, student_namespace):
        """Test disease_symptoms value"""
        assert student_namespace.get('disease_symptoms') == 'high fever, headache', \
            "disease_symptoms should be 'high fever, headache'"


class TestExercise4:
    """Test Exercise 4: Create List of Dictionaries (20 points)"""
    
    def test_diseases_exists(self, student_namespace):
        """Test that diseases list exists"""
        assert 'diseases' in student_namespace, "Variable 'diseases' not found"
    
    def test_diseases_is_list(self, student_namespace):
        """Test that diseases is a list"""
        assert isinstance(student_namespace.get('diseases'), list), "'diseases' should be a list"
    
    def test_diseases_has_3_items(self, student_namespace):
        """Test that diseases list has 3 items"""
        diseases = student_namespace.get('diseases', [])
        assert len(diseases) == 3, "diseases list should have exactly 3 items"
    
    def test_first_disease_rubella(self, student_namespace):
        """Test first disease is Rubella"""
        diseases = student_namespace.get('diseases', [{}])
        assert diseases[0].get('name') == 'Rubella', "First disease should be 'Rubella'"
        assert diseases[0].get('symptoms') == 'fever, rash', "Rubella symptoms should be 'fever, rash'"
    
    def test_second_disease_cholera(self, student_namespace):
        """Test second disease is Cholera"""
        diseases = student_namespace.get('diseases', [{}, {}])
        assert diseases[1].get('name') == 'Cholera', "Second disease should be 'Cholera'"
        assert diseases[1].get('symptoms') == 'severe diarrhea', "Cholera symptoms should be 'severe diarrhea'"
    
    def test_third_disease_gerd(self, student_namespace):
        """Test third disease is GERD"""
        diseases = student_namespace.get('diseases', [{}, {}, {}])
        assert diseases[2].get('name') == 'GERD', "Third disease should be 'GERD'"
        assert diseases[2].get('symptoms') == 'heartburn', "GERD symptoms should be 'heartburn'"


class TestExercise5:
    """Test Exercise 5: Loop Through Data (20 points)"""
    
    def test_disease_names_exists(self, student_namespace):
        """Test that disease_names variable exists"""
        assert 'disease_names' in student_namespace, "Variable 'disease_names' not found"
    
    def test_disease_names_is_list(self, student_namespace):
        """Test that disease_names is a list"""
        assert isinstance(student_namespace.get('disease_names'), list), "'disease_names' should be a list"
    
    def test_disease_names_correct(self, student_namespace):
        """Test disease_names contains correct values"""
        expected = ['Rubella', 'Cholera', 'GERD']
        assert student_namespace.get('disease_names') == expected, f"disease_names should be {expected}"


# Pytest fixture to execute notebook and provide namespace
@pytest.fixture(scope="session")
def student_namespace():
    """Execute the student notebook and return the namespace with variables."""
    import nbformat
    from nbconvert.preprocessors import ExecutePreprocessor
    
    notebook_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'exercise',
        'Lab01_Exercise.ipynb'
    )
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Create a preprocessor
    ep = ExecutePreprocessor(timeout=60, kernel_name='python3')
    
    # Execute the notebook
    try:
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
    except Exception as e:
        print(f"Warning: Notebook execution error: {e}")
    
    # Extract variables from executed cells
    namespace = {}
    for cell in nb.cells:
        if cell.cell_type == 'code':
            # Skip verification cells
            if 'assert' in cell.source and 'Passed' in cell.source:
                continue
            try:
                exec(cell.source, namespace)
            except Exception as e:
                pass
    
    return namespace


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
