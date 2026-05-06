from agents.data_agent import DataAgent

def main():
    print("MySalesAI starting...")

    agent = DataAgent()

    # FIXED LINE
    data = agent.load_data("data/sample.csv")

    print("Data loaded successfully")
    print(data.head())

if __name__ == "__main__":
    main()