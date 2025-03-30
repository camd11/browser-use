import asyncio
import sys
import os
from browser_use import Agent

# Try to import optional dependencies
try:
    from dotenv import load_dotenv
    # Load environment variables (for API keys)
    load_dotenv()
    from langchain_openai import ChatOpenAI
    DEPENDENCIES_INSTALLED = True
except ImportError:
    DEPENDENCIES_INSTALLED = False

# Check if OpenAI API key is set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class GoogleDocsResumeEditor:
    def __init__(self):
        self.agent = None
    
    async def edit_resume_in_google_docs(self):
        """Open Google Docs in a browser and help edit a resume"""
        try:
            # Initialize the language model
            llm = ChatOpenAI(
                model='gpt-4o',
                temperature=0.0,
            )
            
            # Get resume information from user
            resume_info = self.collect_resume_info()
            
            # Create the task description with the collected information
            task = f"""
            Help the user edit their resume in Google Docs by following these steps:
            1. Navigate to docs.google.com
            2. Wait for the user to manually log in (don't try to enter credentials)
            3. Once logged in, help them open their work-in-progress resume document
            4. Help the user fill in their resume with the following information:
               - Name: {resume_info['name']}
               - Contact: {resume_info['contact']}
               - Summary: {resume_info['summary']}
               - Experience: {resume_info['experience']}
               - Education: {resume_info['education']}
               - Skills: {resume_info['skills']}
            5. Provide suggestions to improve the resume's content and formatting
            6. Make it look professional with proper formatting and structure
            
            IMPORTANT: Do NOT attempt to enter login credentials. Just navigate to docs.google.com and
            wait for the user to manually log in. Once they're logged in, continue with the task.
            """
            
            print("\nStarting browser and navigating to Google Docs...")
            
            # Initialize the agent with the task and language model
            self.agent = Agent(task=task, llm=llm)
            
            # Run the agent
            await self.agent.run()
            
        except ImportError as e:
            print(f"Error: {e}")
            print("Required packages not found. Please install them with:")
            print("pip install python-dotenv langchain-openai")
            return
        except Exception as e:
            print(f"\nAn error occurred during the resume editing process: {e}")
            print("If this is an API key issue, make sure your OpenAI API key is set in the .env file.")
            return

async def main():
    print("Google Docs Resume Editor")
    print("=========================")
    
    # Check if OpenAI API key is set
    if not OPENAI_API_KEY:
        print("Error: OpenAI API key not found.")
        print("Please set your OpenAI API key in the .env file or as an environment variable.")
        print("Example .env file content: OPENAI_API_KEY=your-api-key-here")
        return
    
    print("This tool will open a browser and help you edit your resume in Google Docs.")
    print("\nIMPORTANT INSTRUCTIONS:")
    print("1. A browser will open and navigate to Google Docs")
    print("2. You'll need to manually log in to your Google account")
    print("3. After logging in, the AI will help you open and edit your resume")
    print("4. You can press Ctrl+C at any time to pause or exit")
    
    input("\nPress Enter to continue...")
    
    editor = GoogleDocsResumeEditor()
    await editor.edit_resume_in_google_docs()
    
    print("\nResume editing session completed.")

if __name__ == "__main__":
    try:
        # Run the async main function
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)