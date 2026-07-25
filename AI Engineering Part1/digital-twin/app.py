import os
from openai import OpenAI
import gradio as gr
from pprint import pprint
import uuid
import chromadb
import re
import json
import requests
import random
from pathlib import Path


# -------------------------------
# Setup
# -------------------------------

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

client = OpenAI()


# -------------------------------
# Document
# -------------------------------

document_professional_overview = """
Professional Summary

I am an AI Engineer, Lead Developer, and Software Architect with more than 17 years of experience designing and delivering enterprise software applications, Generative AI solutions, retrieval-augmented generation systems, connected-vehicle platforms, APIs, and cloud-native distributed systems.

My current focus is on Generative AI, enterprise conversational search, and RAG-based applications. I have hands-on experience with Python, FastAPI, OpenAI APIs, large language models, embeddings, vector databases, prompt engineering, tool calling, hybrid search, response citations, AI evaluation, and conversational user interfaces.

My broader software engineering background includes deep expertise in Java, J2EE, Spring Boot, reactive programming, microservices, GraphQL, REST APIs, distributed messaging, AWS, Google Cloud Platform, serverless computing, and enterprise application modernization.

Throughout my career, I have translated business requirements into secure, scalable, and maintainable technical architectures. I have led cross-functional development teams, modernized legacy systems, designed high-volume distributed platforms, mentored engineers, and delivered production-ready solutions across automotive, storage, retail, security, and enterprise technology environments.

My experience combines enterprise architecture and engineering leadership with practical AI implementation. This allows me to design AI solutions that are not only innovative but also secure, observable, scalable, and suitable for production deployment.

Current Roles
AI Engineer and Solutions Architect

Selectiva Systems
2025–Present | San Jose, California | Hybrid

At Selectiva Systems, I architect and prototype Generative AI and retrieval-augmented generation solutions that provide conversational access to enterprise information.

These solutions are designed to retrieve information from sources such as:

Enterprise websites
Internal documents
CRM platforms
ERP systems
Data warehouses
Operational databases
REST and GraphQL APIs
Cloud data platforms
Knowledge repositories

I design end-to-end RAG pipelines covering the complete lifecycle of enterprise information retrieval and response generation.

My RAG architecture work includes:

Data-source discovery and connector design
Website crawling and document ingestion
Content extraction and normalization
Text cleaning and preprocessing
Document chunking
Embedding generation
Vector database storage
Metadata enrichment and filtering
Semantic search
Keyword-based retrieval
Hybrid search
Query transformation
Context selection
Prompt orchestration
Large language model response generation
Source citations and traceability
User feedback collection
Retrieval and response evaluation

I have developed conversational AI proofs of concept using Python, FastAPI, OpenAI APIs, ChromaDB, and Gradio. I structure these applications using modular components for ingestion, retrieval, generation, feedback, observability, and evaluation.

I also define secure customer-hosted deployment patterns for cloud, Kubernetes, private-network, and on-premises environments.

My architecture designs consider:

Role-based access control
Data isolation
Authentication and authorization
API security
Secrets management
Audit logging
Monitoring and observability
Personally identifiable information protection
Responsible-AI guardrails
Customer-controlled deployment
Secure access to enterprise data

I collaborate with business leaders, product stakeholders, architects, and engineering teams to convert AI opportunities into implementable solutions.

My responsibilities include developing:

Functional flows
AI use-case definitions
High-level architecture
Detailed technical designs
Implementation roadmaps
Proof-of-concept plans
Retrieval-quality criteria
Evaluation strategies
Security and deployment recommendations
Technologies

Python, FastAPI, OpenAI APIs, Generative AI, RAG, large language models, embeddings, ChromaDB, vector databases, semantic search, hybrid search, prompt engineering, tool calling, Gradio, REST APIs, Docker, Kubernetes, AWS, and Google Cloud Platform.

Lead Developer

Hyundai AutoEver America through Selectiva Systems
April 2022–Present | Irvine, California | Hybrid

At Hyundai AutoEver America, I lead a development team responsible for building microservices and APIs that enable secure, near-real-time communication between connected vehicles, customer-facing web portals, smartphone applications, and backend enterprise systems.

I design and develop vehicle telematics server modules that process communication between in-vehicle systems and external applications.

The platform supports interactions among:

Connected vehicles
Vehicle head units
Mobile applications
Customer web portals
Telematics servers
Backend services
Notification systems
Enterprise applications

My responsibilities include defining data flows, API contracts, integration strategies, and communication patterns across these systems.

I focus on ensuring:

High system throughput
Low-latency communication
Scalability
Availability
Fault tolerance
Secure API access
Reliable distributed messaging
Observability
Operational maintainability

I have contributed to the planning and execution of multiple project releases, from initial requirement analysis through development, testing, production deployment, and post-release support.

I work closely with:

Business stakeholders
Product teams
Quality-assurance engineers
Operations teams
Cloud and infrastructure teams
Security teams
Application developers

I have improved platform scalability and resilience through architecture reviews, caching strategies, asynchronous processing, and distributed messaging technologies such as Kafka, ActiveMQ, and Redis.

As a technical lead, I also:

Mentor junior and mid-level developers
Conduct code and design reviews
Define development standards
Guide troubleshooting and root-cause analysis
Promote API-security best practices
Improve application logging
Strengthen system monitoring and observability
Support release planning and production readiness
Technologies

Java 11, Java 17, Spring Boot, Spring Reactive, MongoDB, Redis, Kafka, ActiveMQ, microservices, REST APIs, and AWS.

Previous Professional Experience
Senior Full Stack Engineer

NetApp through Selectiva Systems
September 2019–April 2022

At NetApp, I worked as a Senior Full Stack Engineer on the development of a next-generation API framework.

I designed and developed multiple GraphQL APIs that provided structured and flexible access to enterprise storage-related data and services.

I also built REST APIs using AWS Lambda-based microservices. These serverless applications were deployed using AWS CloudFormation.

My work included:

Designing GraphQL schemas
Developing GraphQL resolvers
Building REST APIs
Creating AWS Lambda functions
Developing Java and Node.js services
Integrating services within VPN-enabled AWS virtual private clouds
Configuring API Gateway
Creating automated deployment pipelines
Validating and testing APIs
Supporting cloud deployments

I used Postman, Swagger UI, and cURL to validate API behavior, request structures, responses, authentication, and error handling.

I also implemented Jenkins pipelines for automated builds and deployments.

Technologies

Java, Node.js, GraphQL, REST APIs, MongoDB Atlas, AWS Lambda, AWS CloudFormation, AWS API Gateway, microservices, serverless architecture, Bitbucket, Jenkins, Swagger UI, Postman, and cURL.

Specialist Senior Developer

Kohl’s Mainframe-to-Cloud Migration Project through Deloitte
May 2018–September 2019

At Deloitte, I worked on a major modernization initiative for Kohl’s that migrated legacy mainframe applications to modern Java and cloud-based technologies.

The project involved converting COBOL-based applications to Java using the innoWake modernization platform.

My responsibilities included:

Analyzing legacy mainframe applications
Supporting COBOL-to-Java migration
Designing modern application modules
Refactoring converted code
Improving maintainability
Optimizing database queries
Building transaction-signing integrations
Implementing authentication-related functionality
Coordinating module delivery
Supporting testing and client acceptance

I designed and delivered multiple modules and project phases that achieved full client acceptance.

Technologies

Java, J2EE, Vaadin, Angular 2, Google Cloud Platform, DB2, Oracle Database, COBOL modernization, and innoWake.

Senior Software Developer

innoWake License Management through Deloitte
June 2017–May 2018

At Deloitte, I developed an enterprise license-management portal for innoWake.

The application was built using Java, Spring Boot, and Angular-based technologies.

My responsibilities included:

Developing the license-management portal
Building REST APIs
Implementing service-layer components
Developing business-logic components
Supporting presentation-layer integration
Implementing authentication and authorization
Creating JWT-based security
Writing unit tests
Supporting automated builds and deployment

I implemented Spring Security with JSON Web Token authentication to secure application access and API communication.

Technologies

Java, J2EE, Spring Boot, microservices, Spring Security, JWT, Hibernate, Angular 2, REST APIs, Mockito, and Jenkins.

Software Developer

Dell SonicWall – SSL VPN Secure Mobile Access
March 2011–April 2017

At Dell SonicWall, I worked on SSL VPN and secure mobile-access products.

I developed user-interface features for the Connect Tunnel application using Core Java and Java Swing.

I also developed command-line clients for macOS and Linux environments.

My responsibilities included:

Developing secure-access client features
Building Java Swing user interfaces
Developing command-line clients
Supporting macOS and Linux platforms
Designing application modules
Building Spring-based web components
Developing JSP-based interfaces
Integrating application persistence
Troubleshooting client and server issues

I contributed to modules within workplace and appliance-management systems using Spring, JSP, JPA, jQuery, and embedded database technologies.

Technologies

Java, J2EE, Core Java, Java Swing, Spring 3.0, JPA, jQuery, JSP, H2 Database, macOS, Linux, SSL VPN, and secure remote access.

Software Engineer – Product Development

Symphony Services – iRise Definition Center
October 2009–March 2011

At Symphony Services, I worked on product development for the iRise Definition Center and Reader applications.

I developed application modules using Spring, Core Java, Java Swing, Hibernate, and jQuery.

My responsibilities included:

Developing Definition Center modules
Developing Reader application features
Building service-layer components
Integrating application services with H2 Database
Integrating content with the Apache Jackrabbit repository
Supporting desktop and web-based user interfaces
Implementing internationalization
Troubleshooting product issues
Supporting product releases

I implemented internationalization features across the iRise Studio and Reader products, enabling the applications to support multiple languages and regional configurations.

Technologies

Java, J2EE, Core Java, Spring 2.5, Hibernate, Java Swing, jQuery, H2 Database, Apache Jackrabbit, and internationalization.

Core Areas of Expertise
Generative AI and RAG

I have hands-on experience designing and implementing Generative AI and retrieval-augmented generation applications.

My experience includes:

Enterprise conversational AI
Document question answering
Website-based RAG systems
Content ingestion
Text extraction
Chunking strategies
Embedding generation
Vector databases
Semantic search
Metadata filtering
Hybrid retrieval
Prompt engineering
Tool calling
Source citations
Retrieval evaluation
Response evaluation
AI feedback loops
Responsible-AI controls
Software Architecture

I have extensive experience designing secure, scalable, and maintainable software architectures.

My architecture experience includes:

Microservices
Distributed systems
Event-driven architecture
Serverless applications
REST APIs
GraphQL APIs
Reactive systems
Cloud-native applications
Kubernetes deployments
Customer-hosted applications
On-premises deployment
Legacy modernization
High-availability systems
Fault-tolerant systems
Engineering Leadership

I have experience leading development teams and coordinating technical delivery across multiple functions.

My leadership responsibilities include:

Technical planning
Architecture reviews
Code reviews
Release planning
Developer mentoring
Stakeholder collaboration
Production-readiness reviews
Cross-team coordination
Technical troubleshooting
Quality and security enforcement
Cloud and Platform Engineering

I have worked with cloud-native and enterprise deployment models across AWS and Google Cloud Platform.

My cloud experience includes:

AWS Lambda
API Gateway
CloudFormation
Virtual private clouds
Cloud-hosted microservices
Serverless applications
Containerized applications
Docker
Kubernetes
Private-cloud deployments
Customer-hosted deployments
Primary Technical Skills
AI and Python

Python, FastAPI, OpenAI APIs, Generative AI, large language models, RAG, embeddings, vector databases, ChromaDB, semantic search, hybrid search, prompt engineering, tool calling, Gradio, AI evaluation, and citation-backed response generation.

Java and Enterprise Development

Java, J2EE, Spring Framework, Spring Boot, Spring Reactive, Spring Security, Hibernate, JPA, Java Swing, JSP, Vaadin, and Mockito.

APIs and Integration

REST APIs, GraphQL, API Gateway, Swagger, OpenAPI, Postman, cURL, authentication, authorization, JWT, distributed integration, and enterprise-system connectivity.

Data and Messaging

MongoDB, MongoDB Atlas, Redis, Kafka, ActiveMQ, DB2, Oracle Database, H2 Database, vector databases, and Apache Jackrabbit.

Cloud and DevOps

AWS, Google Cloud Platform, AWS Lambda, CloudFormation, Docker, Kubernetes, Jenkins, Bitbucket, serverless architecture, CI/CD, monitoring, logging, and observability.

Professional Value Proposition

I bring a combination of long-term enterprise software experience and modern AI engineering skills.

My background allows me to understand both the experimental and production aspects of AI development. I can prototype a Generative AI use case, design its RAG pipeline, define its APIs, secure its enterprise integrations, plan its deployment architecture, and guide the engineering team toward production implementation.

I am particularly effective in roles that require a combination of:

AI engineering
Solution architecture
Enterprise integration
Backend development
Technical leadership
Cloud architecture
System modernization
Stakeholder communication

My goal is to build AI systems that provide practical business value while meeting enterprise expectations for security, scalability, reliability, governance, and maintainability.
Timeline:
2009 to 2019 - Worked in bangalore, India
20019 to until now - working USA, Sanfrancisco Bay area.
"""

document_education = """
# Education and Learning Journey

## Education Summary

My educational journey reflects persistence, adaptability, and a long-standing interest in mathematics, computing, and technology.

I completed my early education in a Kannada-medium school before transitioning to English-medium education during high school. This was a challenging change because I had to adjust not only to more advanced subjects but also to learning and communicating in a different language.

Despite the initial difficulty, I adapted to the new environment, performed well academically, completed an engineering degree in Computer Science, and later earned a master’s degree focused on Computer Science and Data Science from the University of Illinois Urbana-Champaign.

My academic journey, combined with more than 18 years of software industry experience, has helped me build a strong foundation in software engineering, enterprise architecture, cloud computing, data science, and artificial intelligence.

---

# Master’s Education

## Master’s in Computer Science and Data Science

**University of Illinois Urbana-Champaign, commonly known as UIUC**
**August 2022–May 2025**

I completed my master’s education in Computer Science and Data Science at the University of Illinois Urbana-Champaign.

I pursued the program while continuing my professional career, which required balancing graduate-level coursework, professional responsibilities, technical leadership, and personal commitments.

The program strengthened my understanding of modern computer science and data-oriented technologies. It also supported my transition from traditional enterprise software architecture into AI engineering, Generative AI, machine learning, data science, and retrieval-augmented generation.

My graduate education complemented my existing industry experience in Java, APIs, microservices, distributed systems, cloud computing, and enterprise application architecture.

The program helped me develop a stronger academic and technical foundation in areas related to:

* Computer science
* Data science
* Data analysis
* Algorithms
* Software engineering
* Machine learning
* Artificial intelligence
* Cloud-based systems
* Data-driven problem-solving
* Scalable application development

Completing a master’s degree after many years in the software industry was an important milestone in my career. It demonstrated my commitment to continuous learning and helped me connect my practical engineering experience with newer developments in data science and artificial intelligence.

---

# Undergraduate Education

## Bachelor of Engineering in Computer Science and Engineering

**St. Joseph Engineering College, Mangalore**
**Affiliated with Visvesvaraya Technological University, commonly known as VTU**
**October 2005–June 2009**

I completed my Bachelor of Engineering in Computer Science and Engineering from St. Joseph Engineering College in Mangalore.

The college was affiliated with Visvesvaraya Technological University, commonly abbreviated as VTU.

My engineering education established the foundation for my career in software development and technology. During the program, I studied subjects related to computer programming, software engineering, data structures, databases, operating systems, computer networks, algorithms, and application development.

I was particularly interested in logical problem-solving and subjects that involved mathematics, programming, and structured analysis.

During the seventh semester of my engineering program, I received a job offer from ITC Infotech through campus placement.

However, because of the global economic recession in 2009, the onboarding process was delayed, and I did not receive a joining call for an extended period.

Instead of continuing to wait, I actively explored other opportunities. I attended an interview with Symphony Services, successfully completed the selection process, and received a job offer.

I joined Symphony Services after completing my engineering degree, beginning my professional career in software product development.

This experience taught me an important early-career lesson: even after achieving a goal, external circumstances can change the outcome. It is important to remain proactive, adaptable, and willing to create alternative opportunities.

---

# Pre-University Education

## Pre-University Course

**Shri Mahaveera College, Moodbidri**
**June 2003–April 2005**

I completed my Pre-University Course, commonly known as PUC, at Shri Mahaveera College in Moodbidri.

In Karnataka, the Pre-University Course generally represents the 11th and 12th grades of education.

I selected the PCMS combination during my PUC studies.

PCMS stands for:

* Physics
* Chemistry
* Mathematics
* Statistics

Mathematics was my favorite subject because I enjoyed logical reasoning, numerical problem-solving, formulas, and structured thinking.

Chemistry was my weakest subject and required more effort compared with mathematics, statistics, and other analytical subjects.

Choosing Mathematics and Statistics during PUC contributed to the analytical foundation that later helped me in computer science, software development, system design, data science, and artificial intelligence.

---

# High School Education

## High School

**Jain High School, Moodbidri**
**June 2000–April 2003**

I completed my high school education at Jain High School in Moodbidri.

I joined Jain High School after studying in a Kannada-medium school until the seventh standard.

The transition from Kannada-medium education to English-medium education was one of the most challenging stages of my academic journey.

Until that point, most of my subjects had been taught in Kannada. After moving to an English-medium school, I had to learn new academic concepts while also improving my understanding of English terminology, classroom instruction, textbooks, and written communication.

Initially, it was difficult to understand and express technical and academic concepts in English. However, through consistent effort, practice, and determination, I gradually adjusted to the new learning environment.

This transition strengthened my adaptability and gave me the confidence to handle unfamiliar situations.

It also influenced how I approach learning today. When I encounter a new technology, domain, or technical concept, I am comfortable starting with limited familiarity, working through the initial difficulty, and gradually developing confidence and expertise.

---

# Primary School Education

## Primary and Middle School

**Jyothinagara School, Moodbidri**
**Until 2000**

I completed my early schooling through the seventh standard at Jyothinagara School in Moodbidri.

Jyothinagara School was a Kannada-medium school, and my early education was primarily conducted in Kannada.

Studying in a Kannada-medium school gave me a strong connection to my native language and local community.

During these years, I performed well academically and developed a strong interest in mathematics.

Mathematics appealed to me because it was based on logic and problem-solving and was less dependent on language proficiency. It became one of the subjects in which I felt most confident.

My early education helped develop the discipline, curiosity, and learning habits that supported me throughout high school, engineering, graduate education, and my professional career.

---

# Academic Interests

## Mathematics

Mathematics was my favorite subject throughout school and pre-university education.

I enjoyed:

* Solving numerical problems
* Understanding formulas
* Applying logical reasoning
* Identifying patterns
* Breaking complex problems into smaller steps
* Arriving at clear and verifiable answers

My interest in mathematics naturally supported my later interest in computer programming and software engineering.

Both mathematics and programming require structured thinking, logical analysis, accuracy, and the ability to solve problems step by step.

My mathematical foundation has also helped me understand concepts related to:

* Algorithms
* Data structures
* Statistics
* Data science
* Machine learning
* Embeddings
* Vector similarity
* Software performance
* Distributed systems

## Statistics

I studied Statistics as part of my PCMS combination during my Pre-University Course.

Statistics introduced me to data-oriented thinking and the interpretation of numerical information.

This background later became relevant to my graduate studies in Data Science and my continuing work in artificial intelligence, evaluation, retrieval quality, and data-driven systems.

## Chemistry

Chemistry was my weakest academic subject.

Compared with mathematics and statistics, chemistry required a different type of learning, including memorizing reactions, properties, and scientific concepts.

Although it was challenging, working through the subject taught me that not every area of study will align naturally with my strengths.

It reinforced the importance of consistency, preparation, and additional effort when working in a difficult subject area.

---

# Professional Certification

## Oracle Certified Java Developer

**2011**

I earned an Oracle Java certification in 2011.

The certification validated my knowledge of Java programming and object-oriented software development during the early stage of my professional career.

At that time, Java was one of the primary technologies used in my software development work.

Preparing for the certification strengthened my understanding of:

* Core Java
* Object-oriented programming
* Java syntax and language fundamentals
* Classes and interfaces
* Inheritance and polymorphism
* Exception handling
* Collections
* Application development principles

The certification complemented my professional experience and helped strengthen the Java foundation that I later applied to enterprise applications, Spring-based systems, microservices, APIs, cloud platforms, and distributed architectures.

---

# Transition from Education to Professional Career

During the seventh semester of my engineering degree, I received a campus-placement offer from ITC Infotech.

Receiving a job offer before completing my degree was an important achievement and gave me confidence that my academic preparation had positioned me well for a career in software engineering.

However, the 2009 economic recession affected hiring and onboarding across the technology industry. Although I had received an offer, I did not receive a joining call for a significant period.

Rather than depending entirely on the existing offer, I began applying and interviewing for other opportunities.

I interviewed with Symphony Services, successfully completed the selection process, and received another job offer.

I began my software career with Symphony Services in October 2009, working on product development for the iRise Definition Center.

This experience became an important part of my professional story because it demonstrated:

* Proactive decision-making
* Career resilience
* Adaptability during uncertainty
* Willingness to explore alternatives
* Confidence in interviewing
* Persistence during difficult economic conditions

---

# Educational Challenges and Personal Growth

The most significant challenge in my education was transitioning from a Kannada-medium government-school environment to an English-medium high school.

The change affected nearly every part of the learning process.

I had to adjust to:

* English-language textbooks
* English classroom instruction
* New academic terminology
* Written examinations in English
* Communicating ideas in a different language
* A new school environment

The transition was difficult initially, but I continued working on my language skills and academic understanding.

Over time, I became comfortable studying technical subjects in English and later completed an engineering degree, a professional technology certification, and a master’s degree from a leading university in the United States.

This journey has shaped my belief that a difficult beginning does not determine the final outcome.

With persistence, discipline, and a willingness to learn, it is possible to overcome educational and professional barriers.

---

# Continuous Learning Journey

My education did not end with my engineering degree.

Throughout my software career, I have continued learning new programming languages, frameworks, architectural patterns, cloud platforms, and engineering practices.

My learning journey has included:

* Java and enterprise application development
* Spring and Spring Boot
* REST and GraphQL APIs
* Microservices
* Cloud computing
* AWS and Google Cloud Platform
* Distributed messaging
* Telematics systems
* Data science
* Python
* FastAPI
* Generative AI
* Large language models
* Embeddings
* Vector databases
* Retrieval-augmented generation
* Prompt engineering
* Tool calling
* AI evaluation

Completing my master’s education between 2022 and 2025 was part of this continuous-learning mindset.

I am currently applying my academic knowledge, enterprise-development experience, and architecture background to build practical Generative AI and RAG solutions.

---

# Education Timeline

## 2022–2025

Completed a master’s education in Computer Science and Data Science at the University of Illinois Urbana-Champaign.

## 2005–2009

Completed a Bachelor of Engineering in Computer Science and Engineering from St. Joseph Engineering College, Mangalore, affiliated with Visvesvaraya Technological University.

## 2003–2005

Completed the Pre-University Course at Shri Mahaveera College, Moodbidri, with the PCMS combination: Physics, Chemistry, Mathematics, and Statistics.

## 2000–2003

Completed high school at Jain High School, Moodbidri, after transitioning from Kannada-medium to English-medium education.

## Until 2000

Completed schooling through the seventh standard at Jyothinagara School, a Kannada-medium school in Moodbidri.

## 2011

Earned an Oracle Java certification.

---

# Key Educational Milestones

My major educational and early-career milestones include:

* Studying through the seventh standard in a Kannada-medium school
* Transitioning to English-medium education during high school
* Developing a strong interest in mathematics
* Selecting Physics, Chemistry, Mathematics, and Statistics during PUC
* Completing an engineering degree in Computer Science
* Receiving a campus-placement offer during the seventh semester
* Overcoming hiring uncertainty during the 2009 recession
* Beginning my software career with Symphony Services
* Earning an Oracle Java certification in 2011
* Returning to formal education after extensive industry experience
* Completing a master’s degree focused on Computer Science and Data Science
* Transitioning into AI engineering and Generative AI architecture

---

# Educational Value Proposition

My educational background combines foundational learning, professional certification, advanced graduate education, and continuous self-development.

My journey is not defined only by the institutions I attended. It is also defined by the transitions and challenges I overcame.

I moved from Kannada-medium education to English-medium education, from mathematics and statistics to computer science, from traditional Java development to cloud-native architecture, and from enterprise software engineering to Generative AI and RAG systems.

This journey has made me:

* Adaptable
* Persistent
* Curious
* Comfortable with continuous learning
* Strong in logical problem-solving
* Able to learn complex technical subjects
* Sensitive to the challenges faced by people learning in a new language or environment

My educational experience continues to influence how I approach technology, leadership, mentoring, and professional growth.
"""

document_personal_interests="""
# Personal Interests, Sports, Arts, and Volunteering

## Personal Interests Summary

My interests outside work include sports, hiking, running, music, arts, community activities, and volunteering.

I have always enjoyed learning activities through direct experience. Many of my interests, including badminton, running, cricket, hiking, singing, and music, began without formal training. I developed them gradually through self-learning, regular practice, participation in events, interaction with experienced people, and a willingness to try new challenges.

Sports and outdoor activities have played an important role in my life. They have helped me develop discipline, teamwork, leadership, adaptability, resilience, and a strong sense of community.

My major interests include:

* Cricket
* Badminton
* Pickleball
* Running
* Hiking and trekking
* Singing
* Violin
* Drawing and creative activities
* Environmental and community volunteering

---

# Sports

## Cricket

Cricket has been an important part of my life since childhood.

I started playing cricket informally as gully cricket. Like many cricket enthusiasts in India, I learned the game by playing with friends in streets, open grounds, and neighborhood spaces.

Over time, I participated in office cricket tournaments and continued playing weekend cricket with friends and colleagues.

I had a break from regular cricket between approximately 2019 and 2024. After settling in the United States, I started playing again in the San Francisco Bay Area.

I currently play weekend cricket as part of Cherke Cricket. We usually play using a hard tennis ball, and the group regularly organizes weekend matches.

Cherke Cricket is not only a sporting activity for me but also a community. It provides an opportunity to stay active, maintain friendships, organize games, coordinate teams, and participate in friendly competition.

I have also played in organized Bay Area cricket leagues, including:

* CricBay
* NACL

Playing league cricket has given me experience with more structured matches, team combinations, match planning, field placements, batting orders, bowling strategies, and competitive game situations.

Cricket has helped me strengthen several qualities that are also useful in my professional life:

* Teamwork
* Leadership
* Decision-making
* Planning
* Communication
* Handling pressure
* Adapting to changing situations
* Supporting players with different experience levels

---

## Badminton

Badminton is one of the sports I have played for the longest period of time.

I started playing badminton at around eight years of age. I did not initially receive professional coaching and learned the sport mostly through observation, practice, and self-learning.

During my school years, I represented my school in badminton competitions and progressed to the district level.

I did not focus heavily on badminton during high school, pre-university college, or engineering because of academic priorities and other activities.

After beginning my professional career, I returned to badminton more seriously in approximately 2013.

I briefly received professional coaching for around two to three months. Although the formal training period was short, I continued playing consistently and improving through regular practice.

After moving to the San Francisco Bay Area, I continued playing badminton. I had the opportunity to play with people from several Asian countries where badminton is widely played at a competitive level.

Playing with people from different sporting backgrounds helped me improve my:

* Footwork
* Shot selection
* Court positioning
* Defensive play
* Doubles coordination
* Game awareness
* Ability to adjust to different playing styles

Badminton has taught me that consistent practice and exposure to stronger players can significantly improve performance, even without long-term formal coaching.

---

## Pickleball

I was introduced to pickleball in 2023.

Because of my prior experience with badminton and other racket sports, I was able to understand the basics of pickleball within a few weeks.

I quickly became interested in the sport because it combines elements of badminton, tennis, table tennis, positioning, strategy, and quick decision-making.

I began playing more regularly and later participated in DUPR-rated games in 2025.

At the time this document was prepared, my DUPR rating was approximately 2.93. This rating is expected to change as I continue playing rated matches and improving my game.

DUPR stands for Dynamic Universal Pickleball Rating. It is a rating system used to estimate a pickleball player's skill level based on match performance.

My pickleball learning journey has included:

* Understanding kitchen and non-volley-zone rules
* Developing serve and return consistency
* Learning doubles positioning
* Improving dinking
* Practicing third-shot drops
* Developing court awareness
* Playing DUPR-rated matches
* Adjusting to players with different skill levels

Pickleball has become one of my newer recreational and competitive interests.

---

## Other Sports

During my school years, I participated in several other sports and traditional games.

These included:

* Soccer, also known as football
* Volleyball
* Kho-Kho
* Kabaddi
* Running and sprinting
* Table tennis

After beginning my professional career, I continued playing soccer, volleyball, and table tennis periodically.

My participation in these sports varied depending on work schedules, available facilities, and the people around me.

Playing different sports helped me become comfortable learning new rules, adjusting to different team environments, and understanding different styles of competition.

---

# Running

## Early Running Experience

My earliest running experience came from school competitions.

I used to participate in sprint events and represented my school at different levels. I did not receive professional running training during that period.

My early interest in running was based mainly on natural ability, enthusiasm, and participation in school-level sporting events.

---

## Long-Distance Running

I started focusing on long-distance running in approximately 2016.

One of the main reasons I began running longer distances was to improve my fitness and endurance for hiking and trekking.

I initially started with 5-kilometer runs and gradually increased my distance to 10 kilometers.

Over time, I participated in multiple 10K running events.

One of my favorite running events was the Hampi Heritage Run, where I completed a distance of approximately 12.5 kilometers.

The event was particularly memorable because it combined running with the historic and scenic environment of Hampi.

I also trained with Runners High and briefly trained under Ashwini Bhat.

This training helped me better understand:

* Running form
* Endurance development
* Training plans
* Pacing
* Recovery
* Strength preparation
* Progressive distance building

---

## Running Break and Return

I took a long break from running between approximately 2017 and 2024.

When I later decided to restart, I began preparing for a 5K distance.

I used a free Garmin coaching plan to follow a more structured running schedule.

However, my return to running was affected by recurring Achilles tendon inflammation and injury-related issues.

These injuries interrupted my training multiple times and eventually stopped my running progress.

Although I have not yet returned to consistent long-distance running, the experience taught me the importance of:

* Gradual progression
* Recovery
* Strength training
* Mobility
* Proper footwear
* Avoiding overtraining
* Listening to the body
* Managing recurring injuries carefully

Running remains an activity I value, even though my participation has been limited by injury.

---

# Hiking and Trekking

## Early Hiking Experiences

I participated in several hikes between approximately 2008 and 2013, although I was not yet hiking on a consistent basis.

My first major hike was in 2008, when I visited Gadaikallu, also known as Jamalabad Fort, with my brother and one of his colleagues.

This experience introduced me to the enjoyment of climbing hills, exploring natural environments, and completing physically challenging outdoor journeys.

---

## Bangalore Trekking Club

I began hiking more seriously after joining Bangalore Trekking Club, commonly known as BTC.

From approximately 2013 until 2019, before moving to the United States for work, I regularly participated in BTC hiking and trekking activities.

During this period, I joined hikes almost every weekend or every alternate weekend.

The activities included:

* Single-day hikes
* Night hikes
* Weekend treks
* Two-day treks
* Camping
* Fast treks
* Multi-day Himalayan expeditions
* Environmental volunteering
* Community-service activities

BTC became an important part of my personal life because it combined outdoor adventure, physical fitness, leadership, travel, friendship, community participation, and social service.

---

## Hiking Organizer

I became a trekking organizer with Bangalore Trekking Club in approximately 2014.

I initially started by organizing single-day hikes around Karnataka.

Some of the hikes I organized included:

* Horagina Betta
* Ramadevara Betta
* Savandurga
* Makalidurga
* Nijagal Betta
* Skandagiri

Many of these trips included night hiking and camping on top of or near the mountain.

During these trips, we would sometimes:

* Hike during the night
* Set up a campsite
* Gather around a campfire where permitted
* Prepare noodles
* Make coffee or tea
* Rest at the summit
* Watch the sunrise
* Return home the following morning

Skandagiri was one of my favorite locations among the shorter hikes.

The night trek, summit experience, early-morning atmosphere, and sunrise made it especially memorable.

---

## Two-Day and Weekend Treks

After gaining experience organizing day hikes, I gradually started organizing more challenging two-day treks.

These included destinations such as:

* Kudremukh
* Kodachadri
* Kumara Parvatha
* Kalasa
* Tadiandamol
* Yettina Bhuja
* Nishani Motte
* Mullayanagiri
* Kemmannagundi

These treks required more planning than single-day hikes.

The organizer responsibilities often included:

* Route planning
* Transportation coordination
* Participant registration
* Food planning
* Accommodation or camping arrangements
* Local guide coordination
* Safety planning
* Time management
* Fitness assessment
* Group communication
* Emergency preparation

We also organized fast treks to some locations.

In a fast-trek format, we attempted to complete an entire multi-day trekking route within approximately 24 hours.

These events required strong endurance, disciplined time management, lightweight planning, and close coordination among participants.

---

## Himalayan Expeditions

After organizing several hikes in Karnataka, a co-organizer and I initiated annual multi-day trekking expeditions in the Himalayas.

These trips became some of the most memorable hiking experiences of my life.

The Himalayan treks I participated in or helped organize included:

* Valley of Flowers
* Roopkund
* Junargali
* Animal Pass
* Kashmir Great Lakes

Roopkund was my favorite Himalayan trek.

The expedition was memorable because of its changing landscapes, high-altitude conditions, physical challenge, mountain views, group experience, and the sense of accomplishment that came with completing the trek.

Himalayan trekking taught me:

* Mental resilience
* Physical endurance
* Leadership under difficult conditions
* Risk awareness
* Group coordination
* Respect for nature
* Adapting to altitude and weather
* Preparing for uncertainty
* Supporting participants during challenging moments

---

## Hiking in the United States

After moving to the United States, I continued exploring hiking destinations.

I have visited multiple hiking locations in and around the San Francisco Bay Area.

I have also hiked in other parts of the United States, including:

* Lake Tahoe
* Yosemite National Park
* Zion National Park
* The Los Angeles region
* Other locations in California and surrounding areas

Hiking in the United States exposed me to different landscapes, including coastal trails, forests, lakes, desert terrain, granite mountains, valleys, and national parks.

Although my hiking frequency changed after relocating, hiking continues to be one of my strongest personal interests.

---

# Music and Arts

## Singing and Vocal Music

I have enjoyed singing since childhood.

During my school years, I regularly participated in singing competitions and cultural events.

I won multiple awards in school-level competitive events.

At approximately nine years of age, I joined Karnataka classical music classes.

However, I was able to continue for only around two months at that time.

In 2017, I resumed vocal music training and attended classes for several months.

Although my training was not continuous, singing has remained an important personal interest.

My experience with singing includes:

* School competitions
* Cultural programs
* Competitive events
* Informal performances
* Karnataka classical vocal training
* Self-practice

Singing helped me develop confidence, stage presence, rhythm, listening skills, and an appreciation for music.

---

## Guitar

I learned guitar for approximately three months.

I wanted to explore a musical instrument and understand whether guitar was something I would enjoy pursuing over the long term.

After trying it for a few months, I realized that I did not enjoy it enough to continue seriously.

Although I stopped learning guitar, the experience helped me understand that exploring an activity is valuable even when it does not become a long-term interest.

---

## Violin

Violin is an instrument I had wanted to learn for many years.

My interest began after watching a movie related to the violin around the year 2000.

The movie created a lasting interest in the instrument, but I did not have an opportunity to begin learning at that time.

I finally fulfilled this long-standing goal by starting violin classes in July 2025.

I continue to learn violin.

Beginning violin lessons after thinking about it for approximately 25 years was personally meaningful.

It reinforced my belief that it is never too late to start learning something that has remained an important personal goal.

My violin journey currently focuses on:

* Basic posture
* Holding the violin and bow
* Bow control
* Finger placement
* Producing a clear sound
* Understanding notes
* Rhythm
* Practice discipline
* Developing patience

Learning violin has been challenging, but it has also been rewarding because progress requires attention, repetition, consistency, and patience.

---

## Drawing and Creative Activities

During my school years, I regularly participated in drawing competitions and fancy-dress events.

I won multiple awards in these activities.

These competitions gave me opportunities to express creativity outside academic subjects.

My participation included:

* Drawing
* Coloring
* Fancy dress
* School cultural competitions
* Creative presentations

These experiences helped me become more confident in public participation and encouraged me to explore different forms of creativity.

---

# Volunteering and Community Activities

## Volunteering with Bangalore Trekking Club

My involvement with Bangalore Trekking Club extended beyond hiking and outdoor adventure.

Through BTC, I participated in and helped organize multiple environmental, health, and community-service activities.

These volunteering experiences allowed me to contribute to communities while working alongside people who shared similar interests in nature, public service, and social responsibility.

---

## Hill Cleanup Drives

I volunteered in multiple hill-cleanup drives.

These activities involved collecting waste left behind by visitors and hikers.

The goals were to:

* Protect natural environments
* Reduce plastic and litter
* Improve hiking trails
* Encourage responsible trekking
* Raise environmental awareness
* Preserve hills for future visitors

Participating in cleanup drives strengthened my belief that outdoor enthusiasts have a responsibility to protect the places they visit.

---

## Lake Cleanup Drives

I also participated in lake-cleanup activities.

These drives focused on removing waste from lake surroundings and improving awareness about local environmental conservation.

The experience highlighted the impact of plastic waste, unmanaged garbage, and public neglect on natural water resources.

---

## Sapling Plantation Drives

I participated in sapling-plantation activities intended to support environmental restoration and increase green cover.

These events required coordination among volunteers, selection of suitable locations, planting, and awareness about long-term maintenance.

---

## Seed-Ball Activities

I participated in making seed balls as part of environmental volunteering.

Seed balls are generally created by combining seeds with soil, clay, or other natural materials.

They can be distributed in suitable areas to support plant growth and ecological restoration.

The activity was both educational and community-oriented.

---

## Medical Camps

I helped organize health and medical camps for people living in remote villages.

These camps were intended to improve access to basic medical support for communities that may not have easy access to hospitals, clinics, or regular health services.

Organizing these camps involved activities such as:

* Identifying remote communities
* Coordinating with doctors and volunteers
* Planning transportation
* Arranging basic facilities
* Communicating with local residents
* Managing participants
* Supporting camp operations

These experiences helped me better understand the importance of accessible healthcare and community collaboration.

---

## Blood-Donation Camps

As part of BTC community activities, we organized blood-donation camps approximately every three to six months.

These events required coordination with blood banks, hospitals, donors, volunteers, and participating organizations.

The objectives included:

* Encouraging regular blood donation
* Creating awareness
* Supporting hospitals and blood banks
* Mobilizing community participation
* Helping people in urgent medical need

Participating in these camps was meaningful because a relatively small contribution from a donor could directly help save or support another person's life.

---

# Leadership Through Personal Interests

My hobbies have also provided opportunities to develop leadership outside the workplace.

As a trekking organizer and sports participant, I have taken responsibility for:

* Planning activities
* Coordinating participants
* Organizing logistics
* Communicating instructions
* Managing different personalities
* Supporting beginners
* Handling unexpected situations
* Encouraging participation
* Maintaining safety
* Building a sense of community

These experiences are closely connected to my professional leadership style.

I believe leadership is not only about assigning tasks. It also involves preparation, responsibility, communication, empathy, risk management, and ensuring that everyone feels included.

---

# Personal Qualities Reflected Through My Interests

My sports, music, hiking, and volunteering experiences reflect several personal qualities.

## Adaptability

I have learned different sports, moved between countries, adjusted to new groups, and explored activities without always having formal training.

## Persistence

I returned to cricket after a long break, restarted running, resumed music education, and began learning violin many years after first becoming interested in it.

## Curiosity

I enjoy exploring new sports, locations, technologies, music, and learning experiences.

## Leadership

Organizing hikes, volunteering events, sports activities, and community programs has strengthened my leadership abilities.

## Teamwork

Cricket, badminton doubles, pickleball, trekking, and volunteering all require coordination and mutual support.

## Community Orientation

Many of my interests involve groups and communities rather than only individual achievement.

## Willingness to Learn

I am comfortable beginning as a learner, observing experienced people, practicing consistently, and gradually improving.

---

# Personal Interests Timeline

## Childhood and School Years

* Started playing badminton at approximately eight years of age
* Participated in cricket, sprinting, soccer, volleyball, Kho-Kho, Kabaddi, and table tennis
* Represented my school in badminton up to the district level
* Represented my school in running competitions
* Participated in singing competitions
* Won awards in singing, drawing, and fancy dress
* Briefly attended Karnataka classical music classes
* Developed an interest in violin around the year 2000

## 2008–2013

* Completed early hikes, including Gadaikallu or Jamalabad Fort
* Continued playing sports recreationally
* Participated in office and weekend cricket

## 2013–2019

* Returned to badminton more seriously
* Received brief badminton coaching
* Joined Bangalore Trekking Club
* Became a trekking organizer in 2014
* Organized single-day, two-day, night, fast, and Himalayan treks
* Participated in environmental and community volunteering
* Started long-distance running in approximately 2016
* Completed multiple 10K events and the Hampi Heritage Run
* Resumed vocal music classes in 2017

## 2019–2024

* Took a break from regular cricket and running
* Continued exploring outdoor and recreational activities after moving to the United States
* Hiked in the Bay Area and other parts of the United States

## 2023–Present

* Started playing pickleball
* Learned the sport within a few weeks
* Continued cricket, badminton, pickleball, and hiking activities

## 2024–Present

* Returned to regular cricket through Cherke Cricket
* Played in Bay Area leagues such as CricBay and NACL
* Restarted preparation for 5K running using Garmin coaching
* Experienced recurring Achilles tendon inflammation

## 2025–Present

* Started participating in DUPR-rated pickleball games
* Recorded a DUPR rating of approximately 2.93 at the time of writing
* Began violin lessons in July 2025
* Continued learning violin

---

# Personal Interests Value Proposition

My interests demonstrate that I value a balanced life that includes professional growth, physical activity, creativity, exploration, community participation, and continuous learning.

Sports have taught me teamwork and resilience.

Hiking has taught me endurance, planning, leadership, and respect for nature.

Music has taught me patience and discipline.

Volunteering has helped me understand community responsibility and the importance of contributing beyond personal goals.

These activities have shaped how I approach work and life. I enjoy setting goals, learning through experience, collaborating with people, overcoming challenges, and remaining active both mentally and physically.
"""

# -------------------------------
# System Message
# -------------------------------

system_message = """ You are a digital twin of Gaurav Kamath. When people talk to you,
you respond AS Gaurav — in first person, using his voice, personality, knowledge,
professional experience, learning mindset, and communication style.

Important: If you don't have enough information to answer a question, be honest and say you don't know. 
Do not make up information about Gaurav's exact projects, employers, certifications, volunteering organizations, or dates.
The only factual information you can use is the information provided in the system message.
you cannot get any more facts about Gaurav from the internet or any other source.
When responding as Gaurav:
- Speak in first person as Gaurav.
- Use simple and clear language.
- Be practical and implementation-oriented.
- Think like a software architect.
- Explain technical concepts step by step.
- Use examples, commands, and code when useful.
- Be honest when information is missing.
- Do not invent facts about Gaurav's exact projects, employers, certifications, volunteering
  organizations, or dates unless they are provided in the retrieved context.
- Keep answers helpful, safe, and grounded.
- Represent Gaurav as a hands-on Software Architect with automotive telematics experience,
  strong Java/Spring backend knowledge, academic grounding in Computer Science, growing
  interest in Data Science and AI, and a friendly community-focused personality.

IMPORTANT: Whenever you don't know something about Gaurav,
Always use the send_notification tool to alert the Real Gaurav - do this Automatically without asking the user.
  
When answering technical questions:
First restate the problem in simple words. Then explain the concept. Then show a practical
example. Then mention common mistakes or edge cases. Finally, give a clean recommended
approach.

When answering coding questions:
Explain what each line does. Show expected output or state changes where possible. Point
out bugs or ordering issues. Provide a corrected version. Avoid overcomplicating the answer.

When answering architecture questions:
Identify the main components. Explain the data flow. Mention dependencies and failure
points. Discuss scaling, caching, latency, retries, observability, security, and deployment
impact. Provide a simple text-based diagram if useful.

When answering Git or GitHub questions:
Give exact terminal commands. Explain whether the user is inside an existing repo, creating
a new repo, pushing a branch, pushing a specific folder, or fixing a remote issue. Keep
commands safe and explain destructive operations clearly before suggesting them.

When answering RAG or AI assistant questions:
Explain using simple terms. Connect the answer to practical implementation. Discuss documents,
chunking, embeddings, vector search, retrieval, prompt construction, model response,
evaluation, and guardrails. Recommend an MVP-first architecture when appropriate.

When drafting messages:
Make the message polished, natural, and human. Keep it suitable for WhatsApp, LinkedIn,
email, or workplace chat depending on the context. Avoid sounding robotic or overly formal.
If humor is requested, keep it light and friendly.

Your role is not just to answer questions. Your role is to represent Gaurav's professional
voice: a practical Software Architect with automotive telematics experience, strong backend
engineering knowledge, academic grounding in Computer Science, growing interest in AI and
Data Science, a hands-on learning mindset, and a community-focused personality."""


# -------------------------------
# Chunking function
# -------------------------------

def chunk_text(text, chunk_size=500, overlap=50):
    """
    Split text into overlapping chunks, snapping cuts to natural boundaries
    (paragraph break > newline > sentence end > space) when possible.
    """
    chunks = []
    start = 0
    text_length = len(text)
    halfway = chunk_size // 2
    sentence_end_re = re.compile(r'[.!?](?=\s|$)')

    while start < text_length:
        end = start + chunk_size

        if end >= text_length:
            chunks.append(text[start:text_length])
            break

        window = text[start:end]
        min_cut = start + halfway
        cut = None

        for pattern, is_regex in [
            (r'\n\s*\n', True),   # paragraph break
            ('\n', False),        # newline
            (sentence_end_re, True),  # sentence end
            (' ', False),         # space
        ]:
            if is_regex:
                regex = pattern if isinstance(pattern, re.Pattern) else re.compile(pattern)
                matches = list(regex.finditer(window))
                if matches:
                    candidate = start + matches[-1].end()
                    if candidate >= min_cut:
                        cut = candidate
                        break
            else:
                idx = window.rfind(pattern)
                if idx != -1:
                    candidate = start + idx + len(pattern)
                    if candidate >= min_cut:
                        cut = candidate
                        break

        if cut is None:
            cut = end

        chunks.append(text[start:cut])
        start = cut - overlap

    return chunks

# -----------------------------------------
# RAG: Chunk, Embed, & Store in Chroma DB
# -----------------------------------------

documents = [
    {"text": document_professional_overview, "source":"Gaurav General Info"},
    {"text": document_education, "source": "Gaurav's Education"},
    {"text": document_personal_interests, "source": "Gaurav's Hiking expedition"}
]

chunks = []
ids = []
metadatas = []

for doc in documents:
    # Prepare the lists
    chunks_ = chunk_text(doc["text"], 500, 50)
    ids_ = [str(uuid.uuid4()) for _ in range(len(chunks_))]
    metadatas_ = [{"source": doc["source"], "chunk_index":i} for i in range(len(chunks_))]

    # Add the main lists
    chunks.extend(chunks_)
    ids.extend(ids_)
    metadatas.extend(metadatas_)

# print for logs
print(f"Created {len(chunks)} chunks \n")

for i, chunk in enumerate(chunks):
    #print(f" --- Chunk {i+1} | {len(chunk)} chars --- ")
    print(f"Chunk {i} (ID: {ids[i]}, Source: {metadatas[i]['source']}, Index: {metadatas[i]['chunk_index']})")
    print(chunk)
    print()

# Generate Embeddings for all Chunks
response = client.embeddings.create(
    model = "text-embedding-3-small",
    input = chunks
)

embeddings = [item.embedding for item in response.data]

# Verify embeddings
print(f"Generated {len(embeddings)} embeddings")
print(f"Each embedding has {len(embeddings[0])} dimensions")

# Intialize the Chroma DB
chroma_client = chromadb.PersistentClient(path= "./chroma_db_twin")
#intialize ChromaDB Client (In Memory Storage)
# chroma_client = chromadb.client()

# Empty the collection before adding the new data.
collection = chroma_client.get_or_create_collection(name="digital-twin")
if collection.get()["ids"]:
    collection.delete(collection.get()["ids"]) 

#prepare the data for storage
collection.add(
    ids=ids,
    embeddings=embeddings,
    documents=chunks,
    metadatas=metadatas
)

pprint(collection.get(include=["metadatas", "documents", "embeddings"]))

# -------------------------------
# Tools
# -------------------------------
tools = []

pushover_user= os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_url = "https://api.pushover.net/1/messages.json"

print(f"PUSHOVER_USER: {pushover_user}")
print(f"PUSHOVER_TOKEN: {pushover_token}")

# Pushover API - Create send_notification function
def send_notification(message: str):
    if pushover_token is None or pushover_user is None:
        return "Notificstion failed: pushover not configured"
    payload = {
        "user": pushover_user,
        "token": pushover_token,
        "message": message
    }
    requests.post(pushover_url, data=payload)
    return f"Notification sent: {message}"


send_notification_function = {
    "name": "send_notification",
    #"description": "Send a push notifcation to the real-world version of you via pushover on phone. use this if the user need to alert the real-world version of you.",
    "description": "send a push notification to the real Gaurav. Use this when: \
        1. someone wants to get in touch, hire or collaborate\
            - ask for their name and contact details first, then send notification to Kirill with the name and contaact details.\
        2. You don't know the answer to a question about Gaurav - Send Automatically without asking, including the question so he can add this info later",
    "parameters": {
        "type": "object",
        "properties": {
            "message": {
                "type": "string",
                "description": "The notifiication message to send to the user device"
            }
        },
        "required": ["message"]
    }
}

# Add pushover to the list of tools for the LLM.
tools.append({
    "type": "function",
    "function": send_notification_function
})


# Simulate a rolling a single six-sided die.
def dice_roll():
    result = random.randint(1,6)
    return result

# Describe the function for the LLM.
roll_dice_function = {
    "name": "dice_roll",
    "description": "Simiulate rolling a single six-sided die and return the result. use this when user wants to roll a die or when you want to generate a random number between 1 and 6.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

# Add the function to the tools list
tools.append({
    "type": "function",
    "function": roll_dice_function
})


# -------------------------------
# Tool Handler
# -------------------------------
def handle_tool_call(tool_calls):
    tool_results = []

    for tool_call in tool_calls:
        function_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        # print(f"Calling funtion: {function_name}")

        # Route the tool call to the appropropriate function based on the function name
        if function_name == "send_notification":
        # Actually send the notification using the tool
            content = send_notification(args["message"])
            #content =  f"Notification sent: {args['message']}"
            #print(f" Sent notification: {args['message']}")
        elif function_name == "dice_roll":
            # Call the second function here
            result = dice_roll()
            content = f"Dice rolled: {result}"
        else:
            content = f"Unknown function: {function_name}"

        tool_call_result = {
            "role": "tool",
            "content": content,
            "tool_call_id": tool_call.id 
        }
        #print(f"Tool call result: {tool_call_result}")
        tool_results.append(tool_call_result)
    
    # return what to add to our "context" (about tool call results), a dictionary.
    return tool_results


# -------------------------------
# Main Response function
# -------------------------------

def respond_ai(message, history):

    # RAG: Embed the query
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=[message]
    )
    embeddings = response.data[0].embedding

    # RAG: Search Chroma DB
    results = collection.query(
        query_embeddings=embeddings,
        #n_results=3,
        #include=["documents", "metadatas", "embeddings"]
    )

    # RAg: stitch retrieved Chunks together to create the context for the response
    context = "\n---\n".join(results["documents"][0])

    # Print logs for Debugging 
    print("Retrieved Chunks \n")
    for a, b in zip(results["documents"][0], results["metadatas"][0]):
        print(f"Document {b["source"]} Chunk{b['chunk_index']}: \n{a}\n ")
    
    # Update System message with context
    system_message_enhanced = system_message + "\n\n Context:\n" + context

    # Build message for this run
    messages = [{"role": "system", "content": system_message_enhanced}] + history + [{"role": "user", "content": message}]  
    #print("Messages sent to the model: \n" + system_message_enhanced  )  # Debugging line to see the messages being sent to the model
    
    response = client.chat.completions.create(
        model= "gpt-4.1-mini",
        messages=messages,
        tools=tools
    )

    message = response.choices[0].message

    # Check if model wants to call a tool
    while message.tool_calls:
        pprint(message.tool_calls)
        # Handle tool call
        tool_result = handle_tool_call(message.tool_calls)
        # add message to "context"
        messages.append(message)
        # Add info about the tool call response to the "context", i.e. messages.
        messages.extend(tool_result)

        response = client.chat.completions.create(
            model= "gpt-4.1-mini",
            messages=messages,
            tools=tools
        )
        message = response.choices[0].message
        # may be consider adding a protection from infinite loops.

    return(message.content)

# -------------------------------
# Launch Gradio
# -------------------------------


APP_DIR = Path(__file__).resolve().parent
AVATAR_PATH = APP_DIR / "pgk.jpeg"

gr.ChatInterface(
    fn=respond_ai,
    title = "Gaurav's Digital Twin",
    chatbot = gr.Chatbot(avatar_images=(None, str(AVATAR_PATH))),
    description= "Chat with AI version of Gaurav Kamath. What would you like to explore?",
    examples=["Professional Profile", "Education, Learning, and Career Journey", "Personal Interests and Personality"]
).launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7861)))