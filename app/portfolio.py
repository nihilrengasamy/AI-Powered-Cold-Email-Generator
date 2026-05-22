import pandas as pd
from pathlib import Path


class Portfolio:
    def __init__(self, file_path=None):
        self.file_path = file_path or Path(__file__).parent / "resource" / "my_portfolio.csv"
        self.data = pd.read_csv(self.file_path)

    def load_portfolio(self):
        return None

    def query_links(self, skills):
        skill_terms = self._normalize_terms(skills)
        ranked_rows = []

        for _, row in self.data.iterrows():
            tech_terms = self._normalize_terms(row["Techstack"])
            score = len(skill_terms.intersection(tech_terms))
            if score:
                ranked_rows.append((score, row["Links"]))

        ranked_rows.sort(reverse=True)
        links = [link for _, link in ranked_rows[:2]]

        if not links:
            links = self.data["Links"].head(2).tolist()

        return [[{"links": link} for link in links]]

    @staticmethod
    def _normalize_terms(value):
        if isinstance(value, list):
            value = ",".join(str(item) for item in value)

        return {
            term.strip().lower()
            for term in str(value).replace("/", ",").replace("|", ",").split(",")
            if term.strip()
        }
