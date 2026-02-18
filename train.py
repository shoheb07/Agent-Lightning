from agentlightning import LightningTrainer
from simple_agent import SimpleAgent
from reward import reward_function


def main():
    # Initialize agent
    agent = SimpleAgent()

    # Create trainer
    trainer = LightningTrainer(
        agent=agent,
        reward_fn=reward_function
    )

    # Training dataset
    training_data = [
        {"input": "What is 2+2?", "expected_output": "4"},
        {"input": "Who is Newton?", "expected_output": "Newton is the father of classical mechanics."},
        {"input": "Calculate 2+2", "expected_output": "4"},
    ]

    # Train agent
    trainer.train(training_data)

    print("Training completed successfully!")


if __name__ == "__main__":
    main()