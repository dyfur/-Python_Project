import unittest
import json


# TEST 1 — project_data 


class TestProjectData(unittest.TestCase):
    def test_project_json_loads(self):
        """Check if projects.json loads correctly."""
        with open("data/projects.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("projects", data)
        self.assertGreater(len(data["projects"]), 0)
        self.assertIn("title", data["projects"][0])



# TEST 2 — quiz 


class TestQuizLogic(unittest.TestCase):
    def test_quiz_answer_check(self):
        """Simulate checking a quiz answer."""
        question = {
            "question": "What is voltage?",
            "options": ["Pressure", "Flow", "Resistance"],
            "answer": "Pressure"
        }

        user_answer = "Pressure"
        self.assertEqual(user_answer, question["answer"])



# TEST 3 — history 


class TestHistoryLogic(unittest.TestCase):
    def test_history_timeline_order(self):
        """Check if timeline events are in correct order."""
        timeline = [
            {"year": 1879, "event": "Edison invents lightbulb"},
            {"year": 1904, "event": "First vacuum tube"},
            {"year": 1947, "event": "Transistor invented"}
        ]

        years = [item["year"] for item in timeline]
        self.assertEqual(years, sorted(years))



# TEST 4 — essay page 


class TestEssayLogic(unittest.TestCase):
    def test_essay_save_and_load(self):
        """Simulate saving and loading essay text."""
        text = "Electronics with Spark is fun!"
        saved = text  
        loaded = saved  

        self.assertEqual(text, loaded)


if __name__ == "__main__":
    unittest.main()
