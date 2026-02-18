import re
import json

# # Open and read the text file
# with open("Jobs.txt", "r", encoding="utf-8") as file:
#     content = file.read()

# # Regex patterns
# job_pattern = re.compile(r"^\d+\.\s(.+)", re.MULTILINE)  # Matches job titles (e.g., "1. Cybersecurity Engineer")
# req_pattern = re.compile(r"Requirements:\n((?:- .+\n)+)", re.MULTILINE)  # Matches list under "Requirements:"
# resp_pattern = re.compile(r"Responsibilities:\n((?:- .+\n)+)", re.MULTILINE)  # Matches list under "Responsibilities:"

# # Find all matches
# job_titles = job_pattern.findall(content)
# requirements = [re.findall(r"- (.+)", match) for match in req_pattern.findall(content)]
# responsibilities = [re.findall(r"- (.+)", match) for match in resp_pattern.findall(content)]

# # Combine into structured data
# jobs = []
# for i in range(len(job_titles)):
#     job = {
#         "title": job_titles[i],
#         "requirements": requirements[i] if i < len(requirements) else [],
#         "responsibilities": responsibilities[i] if i < len(responsibilities) else []
#     }
#     jobs.append(job)

# # Print extracted jobs
# for job in jobs:
#     print(job)

# # Save to JSON if needed
# with open("jobs.json", "w", encoding="utf-8") as f:
#     json.dump(jobs, f, indent=4)

# print("Jobs have been extracted and saved to jobs.json")

# #Method 2
# # Open and read the text file
# with open("Jobs.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()

# # Initialize variables
# jobs = []
# current_job = {}
# section = None

# # Process each line
# for line in lines:
#     line = line.strip()  # Remove leading/trailing spaces
   
#     if not line:
#         continue  # Skip empty lines

#     # Detect job titles (assuming they are numbered)
#     if line[0].isdigit() and "." in line:
#         if current_job:
#             jobs.append(current_job)  # Save previous job before starting a new one
#         current_job = {"title": line.split(". ", 1)[1], "requirements": [], "responsibilities": []}
#         section = None  # Reset section tracker

#     # Detect "Requirements" section
#     elif "Requirements:" in line:
#         section = "requirements"

#     # Detect "Responsibilities" section
#     elif "Responsibilities:" in line:
#         section = "responsibilities"

#     # Collect list items under each section
#     elif section and line.startswith("-"):
#         current_job[section].append(line[2:])  # Remove leading "- "

# # Append the last job
# if current_job:
#     jobs.append(current_job)

# # Print jobs list
# for job in jobs:
#     print(job)

# # Save to JSON if needed
# import json
# with open("jobs.json", "w", encoding="utf-8") as f:
#     json.dump(jobs, f, indent=4)

# print("Jobs have been extracted and saved to jobs.json")


jobs = [
    {
        "id":"0",
        "title": "AI Engineer",
        "salary":"$100,000",
        "mode":"online",
        "requirements": [
            "Bachelor's degree in Computer Science, Mathematics, or related field",
            "3+ years of experience in data science",
            "Certifications in programming languages like python and R"
        ],
        "responsibilities": [
            "Design and implement secure AI models",
            "Build optimal learniing algorithms",
            "Develop incident response plans and procedures",
            "Collaborate with development teams to ensure secure coding practices",
            "Stay up-to-date with emerging threats and technologies"
        ]
    },
    {
        "id":"1",
        "title": "Cybersecurity Engineer",
        "salary":"$100,000",
        "mode":"online",
        "requirements": [
            "Bachelor's degree in Computer Science, Cybersecurity, or related field",
            "3+ years of experience in cybersecurity",
            "Certifications like CompTIA Security+ or CISSP"
        ],
        "responsibilities": [
            "Design and implement secure network architectures",
            "Conduct vulnerability assessments and penetration testing",
            "Develop incident response plans and procedures",
            "Collaborate with development teams to ensure secure coding practices",
            "Stay up-to-date with emerging threats and technologies"
        ]
    },
    {
        "id":"2",
        "title": "Data Scientist",
        "salary":"$150,000",
        "mode":"onsite",
        "requirements": [
            "Bachelor's degree in Computer Science, Statistics, or related field",
            "2+ years of experience in data science",
            "Proficiency in programming languages like Python, R, or SQL",
            "Experience with machine learning algorithms and data visualization tools"
        ],
        "responsibilities": [
            "Collect and analyze large datasets to identify trends and patterns",
            "Develop predictive models and machine learning algorithms",
            "Create data visualizations to communicate insights to stakeholders",
            "Collaborate with business teams to drive data-driven decision-making",
            "Stay up-to-date with emerging trends and technologies in data science"
        ]
    },
    {
        "id":"3",
        "title": "IT Project Manager",
        "salary":"$200,000",
        "mode":"online",
        "requirements": [
            "Bachelor's degree in Computer Science, Business Administration, or related field",
            "3+ years of experience in IT project management",
            "Certifications like PMP or Agile",
            "Strong leadership and communication skills"
        ],
        "responsibilities": [
            "Oversee IT projects from planning to delivery",
            "Manage project budgets, timelines, and resources",
            "Coordinate with cross-functional teams to ensure project success",
            "Identify and mitigate project risks and issues",
            "Communicate project status and progress to stakeholders"
        ]
    },
    {
        "id":"4",
        "title": "Software Engineer",
        "salary":"$250,000",
        "mode":"onsite",
        "requirements": [
            "Bachelor's degree in Computer Science or related field",
            "2+ years of experience in software development",
            "Proficiency in programming languages like Java, Python, or C++",
            "Experience with software development methodologies like Agile or Scrum"
        ],
        "responsibilities": [
            "Design, develop, and test software applications",
            "Collaborate with cross-functional teams to identify and prioritize project requirements",
            "Participate in code reviews and contribute to the improvement of the codebase",
            "Troubleshoot and resolve software issues and bugs",
            "Stay up-to-date with emerging trends and technologies in software development"
        ]
    },
    {
        "id":"5",
        "title": "UX Designer",
        "salary":"$300,000",
        "mode":"onsite",
        "requirements": [
            "Bachelor's degree in Design, Human-Computer Interaction, or related field",
            "2+ years of experience in UX design",
            "Proficiency in design tools like Sketch, Figma, or Adobe XD",
            "Experience with user research and testing methodologies"
        ],
        "responsibilities": [
            "Conduct user research to inform design decisions",
            "Create wireframes, prototypes, and high-fidelity designs for software applications",
            "Collaborate with cross-functional teams to ensure design alignment with project goals",
            "Participate in design critiques and contribute to the improvement of the design process",
            "Stay up-to-date with emerging trends and technologies in UX design"
        ]
    },
    {
        "id":"6",
        "title": "DevOps Engineer",
        "salary":"$120,000",
        "mode":"online",
        "requirements": [
            "Bachelor's degree in Computer Science or related field",
            "3+ years of experience in DevOps or system administration",
            "Experience with CI/CD tools like Jenkins, GitLab CI, or GitHub Actions",
            "Proficiency in containerization technologies like Docker and Kubernetes"
        ],
        "responsibilities": [
            "Design and maintain CI/CD pipelines",
            "Automate infrastructure provisioning and deployment",
            "Monitor system performance and troubleshoot issues",
            "Collaborate with development teams to improve deployment processes",
            "Implement security best practices in infrastructure"
        ]
    },
    {
        "id":"7",
        "title": "Cloud Architect",
        "salary":"$180,000",
        "mode":"online",
        "requirements": [
            "Bachelor's degree in Computer Science or related field",
            "5+ years of experience in cloud computing",
            "Certifications in AWS, Azure, or Google Cloud",
            "Strong understanding of cloud security and compliance"
        ],
        "responsibilities": [
            "Design scalable and secure cloud architectures",
            "Evaluate and recommend cloud services and solutions",
            "Lead cloud migration projects",
            "Optimize cloud costs and performance",
            "Provide technical guidance to development teams"
        ]
    },
    {
        "id":"8",
        "title": "Mobile Developer",
        "salary":"$130,000",
        "mode":"onsite",
        "requirements": [
            "Bachelor's degree in Computer Science or related field",
            "2+ years of experience in mobile app development",
            "Proficiency in Swift/Kotlin or React Native/Flutter",
            "Experience with mobile app deployment and testing"
        ],
        "responsibilities": [
            "Develop and maintain mobile applications for iOS and Android",
            "Implement responsive and intuitive user interfaces",
            "Integrate mobile apps with backend services and APIs",
            "Optimize app performance and user experience",
            "Stay current with mobile development trends and best practices"
        ]
    },
    {
        "id":"9",
        "title": "Full Stack Developer",
        "salary":"$140,000",
        "mode":"online",
        "requirements": [
            "Bachelor's degree in Computer Science or related field",
            "3+ years of full stack development experience",
            "Proficiency in frontend frameworks like React, Vue, or Angular",
            "Experience with backend technologies like Node.js, Python, or Java"
        ],
        "responsibilities": [
            "Develop both frontend and backend components of web applications",
            "Design and implement RESTful APIs",
            "Work with databases and data modeling",
            "Ensure application security and performance",
            "Collaborate with designers and product managers"
        ]
    },
    {
        "id":"10",
        "title": "QA Engineer",
        "salary":"$95,000",
        "mode":"onsite",
        "requirements": [
            "Bachelor's degree in Computer Science or related field",
            "2+ years of experience in software testing",
            "Experience with test automation frameworks",
            "Knowledge of testing methodologies and best practices"
        ],
        "responsibilities": [
            "Design and execute test plans and test cases",
            "Develop and maintain automated test scripts",
            "Identify, document, and track software defects",
            "Collaborate with developers to resolve issues",
            "Ensure software quality standards are met"
        ]
    },
    {
        "id":"11",
        "title": "Product Manager",
        "salary":"$160,000",
        "mode":"online",
        "requirements": [
            "Bachelor's degree in Business, Computer Science, or related field",
            "4+ years of product management experience",
            "Strong analytical and problem-solving skills",
            "Experience with agile methodologies"
        ],
        "responsibilities": [
            "Define product vision and strategy",
            "Gather and prioritize product requirements",
            "Work with cross-functional teams to deliver products",
            "Analyze market trends and customer feedback",
            "Track product metrics and KPIs"
        ]
    },
    {
        "id":"12",
        "title": "Database Administrator",
        "salary":"$110,000",
        "mode":"onsite",
        "requirements": [
            "Bachelor's degree in Computer Science or related field",
            "3+ years of database administration experience",
            "Proficiency in SQL and database management systems",
            "Experience with database backup and recovery"
        ],
        "responsibilities": [
            "Install, configure, and maintain database systems",
            "Monitor database performance and optimize queries",
            "Implement database security measures",
            "Perform regular backups and disaster recovery",
            "Troubleshoot database issues and provide support"
        ]
    },
    {
        "id":"13",
        "title": "Machine Learning Engineer",
        "salary":"$170,000",
        "mode":"online",
        "requirements": [
            "Master's degree in Computer Science, Mathematics, or related field",
            "3+ years of experience in machine learning",
            "Proficiency in Python and ML frameworks like TensorFlow or PyTorch",
            "Strong understanding of statistics and algorithms"
        ],
        "responsibilities": [
            "Design and implement machine learning models",
            "Train and evaluate ML algorithms",
            "Deploy models to production environments",
            "Optimize model performance and accuracy",
            "Collaborate with data scientists and engineers"
        ]
    },
    {
        "id":"14",
        "title": "Network Engineer",
        "salary":"$105,000",
        "mode":"onsite",
        "requirements": [
            "Bachelor's degree in Computer Science or related field",
            "3+ years of network engineering experience",
            "Certifications like CCNA or CCNP",
            "Knowledge of network protocols and security"
        ],
        "responsibilities": [
            "Design and implement network infrastructure",
            "Configure and maintain network devices",
            "Monitor network performance and troubleshoot issues",
            "Implement network security measures",
            "Document network configurations and procedures"
        ]
    }
]

def job_model(job_id):
    requirements = []
    responsibilities = []
    job = jobs[job_id]
    id = job['id']
    title = job['title']
    salary = job['salary']
    mode = job['mode']
    for req in job['requirements']:  
        requirements.append(req) 
    for res in job['responsibilities']:
        responsibilities.append(res)
    return id,title,salary,mode,requirements,responsibilities
id,title,salary,mode,requirements,responsibilities = job_model(0)
# print(job_model(0)[0])
# print(id)
# print(title)
# print(salary)
# print(mode)
# print(requirements)
# print(responsibilities)


def save_applications(application):
    with open('jobs.json','a') as f:
        if application == "":
            json.dump("Null Application")
        json.dump(application,f)
    return "Saved successfully"

# print(save_applications("jobs"))
            
