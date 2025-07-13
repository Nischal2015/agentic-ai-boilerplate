import asyncio

from src.linkedin_post_generator.crew import LinkedPostGeneratorCrew


async def main():
    await LinkedPostGeneratorCrew().crew().kickoff_async(
        inputs={
            "course_url": "https://www.coursera.org/specializations/machine-learning-introduction"
        }
    )


if __name__ == "__main__":
    asyncio.run(main())
