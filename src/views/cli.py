from src.storage.log_repository import LogRepository
from src.services.summarizer import Summarizer

def main():
    print("Welcome to EchoBot!")
    repository = LogRepository()  # Default file: chat_log.json
    summarizer = Summarizer(repository)

    while True:
        print("\nPlease choose an option:")
        print("1. Add a conversation summary")
        print("2. View recent summaries")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == "1":
            summary_text = input("Enter the summary of your conversation: ")
            summarizer.create_summary(summary_text)
            print("Summary saved successfully!")
        elif choice == "2":
            limit = int(input("How many summaries would you like to view? "))
            summaries = summarizer.retrieve_summaries(limit)
            print(f"\nDisplaying the last {len(summaries)} summaries:")
            for i, entry in enumerate(summaries, start=1):
                print(f"{i}. [{entry.timestamp}] {entry.summary}")
        elif choice == "3":
            print("Exiting EchoBot. See you next time!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
