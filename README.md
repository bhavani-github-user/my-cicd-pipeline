# 🚀 Full CI/CD Pipeline Project with Jenkins, Docker, Kubernetes & Ngrok

This project showcases an end-to-end **CI/CD pipeline** using:

- 🐍 Flask (Python web app)
- 🐳 Docker (for containerization)
- ☸️ Kubernetes (Minikube for orchestration)
- 🧪 Jenkins (for automated CI/CD)
- 🌐 ngrok (for public URL exposure)

You’ll learn how a simple app goes from:
**GitHub ➡️ Jenkins ➡️ Docker ➡️ Kubernetes ➡️ Web Browser** — all automated! 🔁

---

## 🌐 Live Demo

🟢 Public ngrok URL:  
👉 👉 [https://cb3b-157-50-195-168.ngrok-free.app](https://cb3b-157-50-195-168.ngrok-free.app)
---

## 🔄 CI/CD Pipeline Flow (Jenkins + Kubernetes)

```text
[GitHub] 
   ⬇ (Push Code)
[Jenkins] 
   ⬇ (Builds Docker Image)
[Docker]
   ⬇ (Pushes Image to Minikube)
[Kubernetes]
   ⬇ (Deploys Pod)
[Port-Forward / Ngrok]
   ⬇ 
[User accesses app in browser]
