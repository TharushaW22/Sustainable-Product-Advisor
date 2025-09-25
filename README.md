# Sustainable-Product-Advisor
Sustainable Product Advisor

Sustainable Product Advisor is a multi-agent system that helps users discover eco-friendly products, calculate their eco scores, and identify recycling options.
The system is built with four agents:

	Recommendation Agent – Orchestrates the workflow and integrates results.

	Product Info Agent – Fetches detailed product information from external websites.

	Eco Score Calculator Agent – Evaluates the sustainability of products and assigns eco scores.

	Recycling Agent – Suggests recycling and disposal options.

	🏗️ System Architecture
Diagram


![System Diagram](https://i.postimg.cc/02B6tQvc/System-Diagram-2.png)


Explanation

Users interact through a web or app interface.

	The Recommendation Agent serves as the central hub, receiving queries and coordinating with other agents.

	The Product Info Agent retrieves product details from websites such as Patagonia and H&M.

	The Eco Score Calculator Agent analyzes a product's sustainability based on its materials and production practices, then assigns an eco score.

	The Recycling Agent recommends recycling and disposal methods from government and brand-specific recycling programs.

	The Recommendation Agent integrates all results and recommends alternative products, and presents a structured output to the user.


Responsible AI: The system ensures fairness, transparency, and privacy.

🤝 Agent Roles & Communication Flow

	Recommendation Agent → Orchestrates the flow and combines results.

	Product Info Agent → Retrieves product details from external websites.

	Eco Score Calculator Agent → Assigns an eco score with clear reasoning.

	Recycling Agent → Provides recycling and disposal options.

Flow:
User → Recommendation Agent → Product Info Agent → Eco Score Calculator Agent → Recycling Agent → Recommendation Agent → User
