import os
import shutil
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Brian Boler - Portfolio</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    </head>
    <body class="bg-gray-100">
        <nav class="bg-white shadow-lg">
            <div class="max-w-6xl mx-auto px-4">
                <div class="flex justify-between">
                    <div class="flex space-x-7">
                        <div>
                            <a href="#" class="flex items-center py-4">
                                <span class="font-semibold text-gray-500 text-lg">Brian Boler</span>
                            </a>
                        </div>
                    </div>
                    <div class="flex items-center space-x-3">
                        <a href="#" class="py-2 px-2 font-medium text-gray-500 rounded hover:bg-gray-100 hover:text-gray-900 transition duration-300">Home</a>
                        <a href="#about" class="py-2 px-2 font-medium text-gray-500 rounded hover:bg-gray-100 hover:text-gray-900 transition duration-300">About</a>
                        <a href="#projects" class="py-2 px-2 font-medium text-gray-500 rounded hover:bg-gray-100 hover:text-gray-900 transition duration-300">Projects</a>
                        <a href="#contact" class="py-2 px-2 font-medium text-gray-500 rounded hover:bg-gray-100 hover:text-gray-900 transition duration-300">Contact</a>
                    </div>
                </div>
            </div>
        </nav>

        <main class="max-w-6xl mx-auto px-4 py-8">
            <section id="hero" class="text-center py-20">
                <h1 class="text-5xl font-bold text-gray-800 mb-4">Brian Boler</h1>
                <p class="text-xl text-gray-600 mb-8">Software Engineer & Developer</p>
                <div class="flex justify-center space-x-4">
                    <a href="#contact" class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition duration-300">Get in Touch</a>
                    <a href="#projects" class="bg-gray-200 text-gray-800 px-6 py-2 rounded-lg hover:bg-gray-300 transition duration-300">View Projects</a>
                </div>
            </section>

            <section id="about" class="py-20">
                <h2 class="text-3xl font-bold text-gray-800 mb-8 text-center">About Me</h2>
                <div class="bg-white rounded-lg shadow-lg p-8">
                    <p class="text-gray-600 mb-4">
                        I am a passionate software engineer with expertise in web development and system architecture.
                        My focus is on creating efficient, scalable, and user-friendly applications that solve real-world problems.
                    </p>
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-8">
                        <div class="text-center">
                            <i class="fas fa-code text-4xl text-blue-500 mb-2"></i>
                            <h3 class="font-semibold">Web Development</h3>
                        </div>
                        <div class="text-center">
                            <i class="fas fa-mobile-alt text-4xl text-blue-500 mb-2"></i>
                            <h3 class="font-semibold">Responsive Design</h3>
                        </div>
                        <div class="text-center">
                            <i class="fas fa-database text-4xl text-blue-500 mb-2"></i>
                            <h3 class="font-semibold">Database Design</h3>
                        </div>
                        <div class="text-center">
                            <i class="fas fa-cloud text-4xl text-blue-500 mb-2"></i>
                            <h3 class="font-semibold">Cloud Services</h3>
                        </div>
                    </div>
                </div>
            </section>

            <section id="projects" class="py-20">
                <h2 class="text-3xl font-bold text-gray-800 mb-8 text-center">Projects</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <div class="bg-white rounded-lg shadow-lg overflow-hidden">
                        <div class="p-6">
                            <h3 class="font-bold text-xl mb-2">Project 1</h3>
                            <p class="text-gray-600">Description of project 1 and its key features.</p>
                        </div>
                    </div>
                    <div class="bg-white rounded-lg shadow-lg overflow-hidden">
                        <div class="p-6">
                            <h3 class="font-bold text-xl mb-2">Project 2</h3>
                            <p class="text-gray-600">Description of project 2 and its key features.</p>
                        </div>
                    </div>
                    <div class="bg-white rounded-lg shadow-lg overflow-hidden">
                        <div class="p-6">
                            <h3 class="font-bold text-xl mb-2">Project 3</h3>
                            <p class="text-gray-600">Description of project 3 and its key features.</p>
                        </div>
                    </div>
                </div>
            </section>

            <section id="contact" class="py-20">
                <h2 class="text-3xl font-bold text-gray-800 mb-8 text-center">Contact Me</h2>
                <div class="bg-white rounded-lg shadow-lg p-8">
                    <div class="flex justify-center space-x-8">
                        <a href="#" class="text-gray-600 hover:text-blue-500 transition duration-300">
                            <i class="fab fa-github text-4xl"></i>
                        </a>
                        <a href="#" class="text-gray-600 hover:text-blue-500 transition duration-300">
                            <i class="fab fa-linkedin text-4xl"></i>
                        </a>
                        <a href="#" class="text-gray-600 hover:text-blue-500 transition duration-300">
                            <i class="fas fa-envelope text-4xl"></i>
                        </a>
                    </div>
                </div>
            </section>
        </main>

        <footer class="bg-gray-800 text-white py-8">
            <div class="max-w-6xl mx-auto px-4 text-center">
                <p>&copy; 2024 Brian Boler. All rights reserved.</p>
            </div>
        </footer>
    </body>
    </html>
    """

if __name__ == '__main__':
    # Create dist directory if it doesn't exist
    os.makedirs('dist', exist_ok=True)
    
    # Write index.html
    with open('dist/index.html', 'w') as f:
        f.write(app.test_client().get('/').data.decode()) 