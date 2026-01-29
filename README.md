# SecurePass-Generator
SecurePass: Privacy-First String Generator
passgen is a lightweig
ht, open-source utility designed to generate high-entropy random strings, numbers, and symbols. Built with a "Zero-Knowledge" philosophy, it ensures that your generated data never leaves your temporary system memory.

🚀 Key Features
Variable Length: Custom slider allows for generation between 20 and 100 characters.

Cryptographically Secure: Powered by Python’s secrets module, utilizing OS-level randomness for maximum unpredictability.

Total Privacy: * No Logs: Does not write to any local files or databases.

No Cloud: Operates entirely offline; no internet permissions or telemetry.

Volatile Storage: Generated strings are wiped from memory as soon as the application is closed.

One-Click Copy: Fast clipboard integration for immediate use.

🛠️ Technical Specs
Language: Python 3.x

GUI Framework: Tkinter (Windows) / Kivy (Android)

Security Engine: secrets (PEP 506 compliant)

Binary Size: ~10MB (Standalone executable)

📥 Usage
Launch passgen.

Adjust the slider to your desired character count (20–100).

Click Generate Secure Text.

Click Copy to Clipboard and paste it into your target application.

Close the app to clear all temporary data.
