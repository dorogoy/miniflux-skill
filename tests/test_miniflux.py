import os
import subprocess
import pytest


def test_script_exists():
    """Test that miniflux.sh script exists and is executable."""
    script_path = os.path.join(os.path.dirname(__file__), '..', 'scripts', 'miniflux.sh')
    assert os.path.exists(script_path), f"Script not found: {script_path}"
    assert os.access(script_path, os.X_OK), f"Script not executable: {script_path}"


def test_script_has_required_functions():
    """Test that script has required functions."""
    script_path = os.path.join(os.path.dirname(__file__), '..', 'scripts', 'miniflux.sh')
    
    with open(script_path, 'r') as f:
        script_content = f.read()
    
    # Check for key functions
    required_functions = ['api_get', 'api_post', 'api_patch', 'api_delete']
    for func in required_functions:
        assert func in script_content, f"Missing function: {func}"


def test_skill_documentation_exists():
    """Test that SKILL.md and README.md exist."""
    base_dir = os.path.dirname(__file__)
    
    assert os.path.exists(os.path.join(base_dir, '..', 'SKILL.md')), "SKILL.md not found"
    assert os.path.exists(os.path.join(base_dir, '..', 'README.md')), "README.md not found"


def test_skill_documentation_has_required_sections():
    """Test that SKILL.md has required sections."""
    skill_md_path = os.path.join(os.path.dirname(__file__), '..', 'SKILL.md')
    
    with open(skill_md_path, 'r') as f:
        content = f.read()
    
    required_sections = [
        '## Setup',
        '## Configuration',
        '## Usage',
        '## Commands Reference'
    ]
    
    for section in required_sections:
        assert section in content, f"Missing section in SKILL.md: {section}"


def test_readme_exists_and_has_content():
    """Test that README.md has content."""
    readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
    
    with open(readme_path, 'r') as f:
        content = f.read()
    
    assert len(content) > 100, "README.md is too short"
    assert '# Miniflux' in content, "README.md should have title"
