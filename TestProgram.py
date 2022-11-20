from Agent import Action, Agent


day = int(input("Enter day: "))
time = input("Enter Time (Hr:00): ")

testAgent = Agent(day, time)

print('\n'+''+testAgent.perform_action())
