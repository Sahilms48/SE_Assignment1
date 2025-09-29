# 📊 Django Polls Application



> A sleek, interactive polling application built with Django - create, vote, and analyze polls with ease.

## ✨ [Live Demo](http://assignment1-env.eba-fvpe74pe.us-west-2.elasticbeanstalk.com/polls/)

![Django Logo](https://static.djangoproject.com/img/logos/django-logo-negative.svg)

## 📝 Description

This elegant polling system allows users to:
- 📋 Browse through available polls with an intuitive interface
- ✅ Cast their vote on questions that matter
- 📊 View real-time results with visual feedback

Built as a showcase of Django's powerful features, this application demonstrates:
- 🗄️ Robust data modeling and relationships
- 🌐 Efficient class-based views
- 🔗 Clean URL routing patterns
- 🎨 Responsive templates
- 📝 Secure form handling
- 👑 Customizable admin interface

## 🚀 Features

- **Modern Interface**: Clean design focused on usability
- **Interactive Voting**: Seamless voting experience with immediate feedback
- **Admin Dashboard**: Powerful backend for poll management
- **Mobile-Friendly**: Responsive design works on all devices

## 🏗️ Project Structure

```
polls/
├── models.py      # Data models (Question, Choice)
├── views.py       # View controllers
├── urls.py        # URL routing configuration
├── admin.py       # Admin interface setup
├── apps.py        # Application configuration
├── tests.py       # Unit tests
└── templates/     # HTML templates
    └── polls/
        ├── index.html
        ├── detail.html
        └── results.html
```

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-polls-app.git
   cd django-polls-app
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Apply migrations**
   ```bash
   cd djangotutorial
   python manage.py migrate
   ```

5. **Create admin user**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## 📖 Usage

1. **Access the admin panel**
   - Visit `/admin` and log in with your superuser credentials
   - Create new polls with multiple choice options

2. **Explore the polls**
   - Browse to the main page to see all available polls
   - Click on any poll to view details and voting options

3. **Vote and view results**
   - Select your preferred option and submit your vote
   - View real-time results with vote counts

## 💻 Technologies

- **Backend**: Python 3, Django
- **Frontend**: HTML5, CSS3
- **Database**: SQLite (development), PostgreSQL (production option)
- **Deployment**: AWS Elastic Beanstalk

## 🔗 Deployment

This application is deployed on AWS Elastic Beanstalk:
- [http://assignment1-env.eba-fvpe74pe.us-west-2.elasticbeanstalk.com/polls/](http://assignment1-env.eba-fvpe74pe.us-west-2.elasticbeanstalk.com/polls/)


---

