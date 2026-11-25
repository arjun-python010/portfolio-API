from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

class AboutView(View):
    def get(self,request):
        data={
            "ID" : 1,
            "Name" : "Arjun",
            "Title" : "Python Django React Fullstack developer",
            "Bio" : "A Passionate Developer",
            "DOB" : "19/02/2004",
            "Email" : "arjunsuresh534@gmail.com",
            "Contact" : 9857680922,
            "GitHub_url" : "https://github.com/arjun-s",
            "Linkedin_url" :"https://linkedin.com/in/arjun-s"
        }
        return JsonResponse(data)
    
class Education(View):
    def get(self,request):
        data={
            "ID" : 101,
            "Instituion" : "Luminar",
            "Degree/Course" : "Python fullstack developer",
            "University" : "ABC University",
            "Location" : "Cochin",
            "Starting_year" : "June-2026",
            "ending_year" : "january-2027",
            "cgpa" : 7.5,
            "description" : "Completed Python course"
        }   
        return JsonResponse(data) 
    
class ProjectView(View):
    def get(self,request):
        projects=[{
            "Id" : 1,
            "title" : "DietLense",
            "short_description" : "AI-powered Food recognition app",
            "long_description" : "An application that analyzes food images and provides nutritional information",
            "technologies_used" : ["python","Django","Google GenAI SDK"],
            "live_url" : "https://dietlense.example.com",
            "image_url" : "https://example.com/dietlense.jpg",
            "github_url": "https://github.com/username/dietlense",
            "featured" : True                             
        },
            {"Id" : 2,
             "title": "Interview Prep Blog",
             "short_description": "Educational application for programming interviews.",
             "long_description":  "A platform for practicing technical interview questions and reading programming articles.",
             "technologies_used": ["Python","Django","JavaScript"],
             "live_url": "https://prep.example.com",
             "github_url": "https://github.com/username/interview-prep",
             "image_url": "https://example.com/interview.jpg",
             "featured": True  
                
            }      ]
        return JsonResponse(projects,safe=False)   
class SkillsView(View):
    def get(self,request):
        skills=[
            {
                "Id" : 1,
                "skill_name" : "Python",
                "category" : "Programming Language",
                "proficency" : "Advanced",
                "years_of_experience" : 4
            },
            {
                "Id" : 2,
                "skill_name" : "Django",
                "category" : "Backend",
                "proficiency" : "Advanced",
                "years_of_experience" : 3
            },
            {
               "Id" : 3, 
               "skill_name" : "React",
                "category" : "Frontend",
                "proficiency" : "Intermediate",
                "years_of_experience" : 3
            }
        ]
        return JsonResponse(skills,safe=False)     

# Create your views here.
