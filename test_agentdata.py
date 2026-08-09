# test_agentdata.py
"""
Tests for AgentData module.
"""

import unittest
from agentdata import AgentData

class TestAgentData(unittest.TestCase):
    """Test cases for AgentData class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AgentData()
        self.assertIsInstance(instance, AgentData)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AgentData()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
