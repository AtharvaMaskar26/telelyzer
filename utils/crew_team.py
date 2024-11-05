from crewai import Agent, Task, Crew

script_adherence_agent = Agent(
    role="Customer Support Script Adherence Supervisor", 
    goal="Check if the agent has followed the script in a given transcript.", 
    backstory="You are recruited by Choice Tech Lab to monintor customer support agents and if thy are adhereing to the given script in any call."
)

call_recording_rater_agent = Agent(
    role="Customer Call Recording Supervisor.", 
    goal="Rate customer support call recordings based on lead generation", 
    backstory="You are recruited by Choice Tech Lab to monitor customer support agents and review call recodings."
)

def analyze_call(transcript: str, script: str) -> dict:
    script_adherence_task = Task(
        description=f"From the given transcript: {transcript} and the given script, your job is to check if the customer support agent has followed the given script: {script}", 
        expected_output=f"Rate on a scale of 1 - 5, how well the customer support agent has stuck to the script. No extra text.", 
        agent=script_adherence_agent
    )

    call_recording_rater_task = Task(
        description=f"From the given transcript: {transcript} rate how engaged the customer was with the agent.", 
        expected_output="Rate the call on a scale of 1 - 5 only and no extra text.",
        agent=call_recording_rater_agent
    )

    script_crew = Crew(
        tasks=[script_adherence_task], 
        agents=[script_adherence_agent], 
        verbose=True
    )   

    call_rating_crew = Crew(
        tasks=[call_recording_rater_task], 
        agents=[call_recording_rater_agent],
        verbose=True
    )

    script_crew_result = script_crew.kickoff()
    call_rating_result = call_rating_crew.kickoff()

    return script_crew_result.raw, call_rating_result.raw