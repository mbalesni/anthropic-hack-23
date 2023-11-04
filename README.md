# anthropic-hack-23


Goal: Develop a voice assistant to for remote closely-supervised software development tasks on a Mac, such as navigating and editing code in VS Code, with real-time user feedback guiding its actions.

Vision: you go on a run while guiding an agent through running an experiment on your laptop.

## Todos:

Saturday 12.07pm:
- [ ] Play around with Claude via LangChain [Maria]
- [ ] Research text-to-speeach and speech-to-text options [Maria?]
- [X] Find existing agents that do similar stuff without voice. Understand how they interface with the OS and what they're missing from the goal vision [Mikita]
    - Found [open-interpreter](https://github.com/KillianLucas/open-interpreter) — they already implement the core loop that we want, similar to ChatGPT Code Execution. Was able to do a small task and push the code for it to git through just talking and accepting GPT-4 actions. Haven't looked into how they interface with the OS yet.
- [ ] Understand how the phone can communicate with the laptop (some VNC-like thing?) [Mikita]

