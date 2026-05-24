# Image Rater

My Python program allows users to rate multiple images and receive statistics about them.


| Project Overview |

I used a simple graphical interface (Tkinter GUI) that allows users to:

- Browse images stored inside a folder
- Give each image a rating from 0 to 10
- Receive statistics at the end
- Save the results into a JSON file


| Features |

- Dynamic graphical interface
- Rating system
- Multiple statistics (mean, max, min, number of images used)
- Automatic export of results into a JSON file
- Modular architecture with separated logic


| Tech Stack |

- Python (everything is based on it)
- Tkinter (GUI)
- Pillow for image handling


| Project Structure |

src/
| gui.py
| image_loader.py
| rating.py
| stats.py
| storage.py



| How to Run the Program |

In the terminal, type:


pip install -r requirements.txt

Then run:


python src/gui.py



| Example Output |

{
  "images": [
    {"path": "image1.jpg", "rating": 8}
  ],
  "stats": {
    "mean": 8,
    "min": 8,
    "max": 8,
    "count": 1
  }
}



| Personal Notes |

I created this project while focusing on:

- Clean code
- An organized modular system
- Separation of responsibilities



| Possible Future Improvements |

- Folder selection through the GUI (file dialog)
- Better UI/UX
- Improved image previews
- More export formats (CSV, etc.)






|| About This Project ||

This is my first Python project, created while I was in high school (seconde).
I made it to improve my programming skills, learn new concepts, and understand how a real Python project is organized.


| My Working Method |

I used ChatGPT a lot during this project because I didn't know how to organize a real project at first , and it taught me many things during the development process.

I used it as a learning tool,  not as a shortcut.

Every time I did not know how to do something or did not understand a concept:

- I asked for detailed explanations
- I did not continue the project until I fully understood the concept
- I made sure I was able to reproduce the logic by myself without help

This approach allowed me to truly understand the concepts and programming logic instead of just copying code blindly.


| What I Learned |

- How to organize a project with multiple modules
- How to build a simple GUI with Tkinter
- How to manage different application states
- How to handle errors and edge cases
- How to write cleaner and more maintainable code

| Conclusion |

I am realllyyy happy with my first project, it taught me many things about organizing real projects and helped me discover many new programming concepts .

This project is an important step in my learning journey !!!!

Thank you a lot for reading




