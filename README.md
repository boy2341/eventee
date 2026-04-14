# 🎓 Eventee — Your Campus, Connected.

Welcome to **Eventee**, a centralized networking sanctuary built for the vibrant student community of Delhi NCR. 

Being a student at **DTU**, I noticed how scattered campus information is. Hackathons are on one WhatsApp group, society auditions are on another Instagram page, and NGO opportunities are lost in email threads. **Eventee** is my solution to that chaos—a single, elegant home for everything happening on campus.



---

## 🌟 Why Eventee?

Most campus sites feel like they were built in 1995. I wanted to build something that felt modern, fast, and actually helpful.

- **For Students:** No more "FOMO." Discover intellectual gatherings, tech symposia, or cultural fests with a single search.
- **For Societies:** A professional stage to showcase your guild's mission and recruit the next generation of talent.
- **For Social Impact:** A dedicated space for NGOs to find volunteers who actually care about making a difference.

---

## 🛠️ The "Under the Hood" Stuff

I chose this specific stack to keep the platform lightweight yet powerful enough to scale across colleges.

* **FastAPI (Python):** Chosen for its incredible speed and native support for asynchronous requests—essential for real-time networking.
* **Vanilla JS & Tailwind CSS:** I avoided heavy frameworks like React to keep the site "lightning fast" and highly responsive, even on spotty campus Wi-Fi.
* **Vercel Serverless:** Deployed as serverless functions to ensure 99.9% uptime without me having to manage a physical server.

---

## 📂 Project Anatomy

```text
├── api/
│   └── main.py         # The "Brain": Handles auth, logic, and data routing.
├── index666.html       # The "Face": A single-page sanctuary for the UI.
├── vercel.json         # The "Map": Tells the cloud how to navigate the site.
├── requirements.txt    # The "Toolbox": All the Python gear needed to run.
└── README.md           # The "Manual": You are here!
