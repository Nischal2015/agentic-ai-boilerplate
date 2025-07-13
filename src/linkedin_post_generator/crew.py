from crewai import Task, Agent, Crew
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool


@CrewBase
class LinkedPostGeneratorCrew:

    agents: list[BaseAgent]
    tasks: list[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def course_summarizer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["course_summarizer_agent"],  # type: ignore[index]
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
        )

    @agent
    def course_summary_tone_optimizer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["course_summary_tone_optimizer_agent"],  # type: ignore[index]
        )

    @agent
    def hashtag_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["hashtag_generator_agent"],  # type: ignore[index]
        )

    @agent
    def final_composer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["final_composer_agent"],  # type: ignore[index]
        )

    @task
    def course_summarizer_task(self) -> Task:
        return Task(
            config=self.tasks_config["course_summarizer_task"],  # type: ignore[index]
        )

    @task
    def course_summary_tone_optimizer_task(self) -> Task:
        return Task(
            config=self.tasks_config["course_summary_tone_optimizer_task"],  # type: ignore[index]
        )

    @task
    def hashtag_generator_task(self) -> Task:
        return Task(
            config=self.tasks_config["hashtag_generator_task"],  # type: ignore[index]
        )

    @task
    def final_composer_task(self) -> Task:
        return Task(
            config=self.tasks_config["final_composer_task"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )


if __name__ == "__main__":
    crew = LinkedPostGeneratorCrew()
    crew.crew().kickoff(
        inputs={
            "course_url": "https://www.coursera.org/specializations/machine-learning-introduction"
        }
    )
