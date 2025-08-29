# SMS Event Planner (Gatherly)

A sophisticated SMS-based event planning application that manages complex conversational workflows entirely through text messages.

## Features ✨

### Core Event Planning
- **SMS-First Experience**: Complete event planning via text messages
- **Multi-Guest Coordination**: Add guests via phone numbers, manage RSVPs
- **Smart Date/Time Collection**: AI-powered parsing of natural language dates and times
- **Venue Management**: Location collection and venue selection
- **Activity Planning**: Event activity/purpose collection

### Advanced Guest Management
- **7-Step Preferences Workflow**: Collect detailed guest preferences during availability requests
- **Enhanced Availability Display**: Planner notifications show both availability and preferences with dash format
- **Smart Guest States**: Automatic state management with proper cleanup
- **Phone Number Normalization**: Handles various phone number formats seamlessly

### Technical Excellence
- **Systematic SMS Routing**: "Everyone is a planner by default" with smart guest state detection
- **Database Integrity**: PostgreSQL with proper relationships and constraints
- **Performance Optimized**: Efficient queries and caching for large guest lists
- **Production Ready**: Docker deployment with comprehensive error handling

## Architecture 🏗️

### Key Principles
1. **Everyone is a Planner by Default**: All users are planners unless they have an active guest state
2. **Per-Message Guest State Cleanup**: Guest states are cleaned up after each response
3. **Handler Pattern**: Each workflow stage has a focused handler in `app/handlers/`
4. **Service Layer Separation**: Business logic separated into services in `app/services/`

### Core Components
- **SMSRouter**: Main routing logic with smart state management
- **Workflow Handlers**: Stage-specific message handling (guests, dates, venues, etc.)
- **Service Layer**: Business logic for events, guests, availability, venues, AI processing
- **Database Models**: SQLAlchemy models with proper relationships and methods

## Deployment 🚀

### Railway Deployment
This application is configured for Railway deployment with:
- **Dockerfile**: Ensures PostgreSQL headers are available for psycopg2
- **Environment Variables**: Configured for production PostgreSQL
- **Auto-Deploy**: GitHub integration for continuous deployment

### Local Development
```bash
# Clone and setup
git clone <repository-url>
cd sms-event-planner-v2
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your Twilio credentials

# Initialize database
python init_db.py

# Run locally
python run.py
```

## SMS Workflow Examples 📱

### Creating an Event
```
Planner: "Let's plan a dinner party"
System: "Great! When would you like to have your dinner party?"
Planner: "Friday or Saturday evening"
System: "What time works best?"
Planner: "7-11pm"
System: "Where would you like to meet?"
Planner: "My place or downtown restaurant"
System: "Who should I invite? (Send phone numbers)"
Planner: "+1234567890, +1987654321"
```

### Guest Availability with Preferences
```
Guest receives: "Hi! You're invited to a dinner party on Fri 8/30 or Sat 8/31, 7-11pm at My place or downtown restaurant. Are you available?"

Guest: "Yes available both days"
System: "Great! Do you have any dietary preferences, restrictions, or other preferences for this dinner party?"
Guest: "I'm vegetarian and prefer earlier times if possible"
System: "Perfect! Your response has been recorded. Thanks!"

Planner notification: "✅ John Smith responded: Available both days - vegetarian, prefers earlier times if possible"
```

## Recent Updates 🆕

- ✅ Complete 7-step preferences collection workflow
- ✅ Enhanced availability notifications with preferences display
- ✅ Fixed systematic SMS router state management bugs
- ✅ Added comprehensive phone number normalization
- ✅ Docker deployment configuration for Railway
- ✅ Performance optimizations for large guest lists

## Tech Stack 💻

- **Backend**: Python Flask with SQLAlchemy
- **Database**: PostgreSQL (production), SQLite (development)
- **SMS**: Twilio API integration
- **AI**: OpenAI GPT for natural language processing
- **Deployment**: Docker + Railway
- **Testing**: pytest with comprehensive test coverage

## Contributing 🤝

This application follows clean architecture principles with clear separation of concerns. When making changes:

1. Keep handlers focused (under 100 lines)
2. Use the service layer for business logic
3. Follow the exact message formatting patterns
4. Maintain the "everyone is a planner by default" principle
5. Test SMS workflows thoroughly

## License 📄

This project is proprietary software. All rights reserved.
