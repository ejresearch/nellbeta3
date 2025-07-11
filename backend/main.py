# backend/main.py - COMPLETE REWRITE WITH ALL PHASE 1 ROUTERS

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 🧩 Import top-level routers
from backend.api import (
    project_manager,
    sql_api,
    buckets,
    graph,
    project_versions,
    templates,  # ✅ ADDED: Template system
    export      # ✅ ADDED: Export system
)

# 🧠 Import submodule routers
from backend.api.brainstorming import routes as brainstorming_routes
from backend.api.writing import routes as writing_routes
from backend.api.academic import routes as academic_routes  # ✅ ADDED: Academic system

app = FastAPI(
    title="Nell Beta API",
    description="Modular API for creative and research projects — screenwriting, textbooks, and beyond.",
    version="0.1.0"
)

# 🌐 CORS (update `allow_origins` for production!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Healthcheck
@app.get("/healthcheck", tags=["Health"])
def healthcheck():
    return {"status": "ok"}

# 🎯 PHASE 1 ADDITIONS - Template and Export Systems
app.include_router(templates.router, prefix="/templates", tags=["Templates"])
app.include_router(export.router, prefix="/projects/{project_name}/export", tags=["Export"])

# 🎓 Academic Writer (Phase 2 - Already implemented)
app.include_router(academic_routes.router, prefix="/academic", tags=["Academic Writing"])

# 🔧 Project lifecycle
app.include_router(project_manager.router, prefix="/projects", tags=["Project Manager"])
app.include_router(project_versions.router, prefix="/projects/{project_name}/versions", tags=["Table Versions"])

# 📄 SQL Table Editor (Reference Documents) - ENHANCED
app.include_router(sql_api.router, prefix="/projects/{project_name}/tables", tags=["Reference Tables"])

# 🧠 Brainstorming (LightRAG)
app.include_router(brainstorming_routes.router, prefix="/projects/{project_name}/brainstorm", tags=["Brainstorm"])

# ✍️ Writing Module (Final Drafts) - WITH PERPLEXITY SUPPORT
app.include_router(writing_routes.router, prefix="/projects/{project_name}/write", tags=["Writing"])

# 🪣 Bucket Manager (Vector Store)
app.include_router(buckets.router, prefix="/projects/{project_name}/buckets", tags=["Buckets"])

# 🔗 Graph Operations (Neo4j)
app.include_router(graph.router, prefix="/projects/{project_name}/graph", tags=["Graph"])

# 🚀 API is now complete with all Phase 1-2.2 functionality
# Available endpoints:
# - Templates: /templates/*
# - Export: /projects/{name}/export/*
# - Enhanced Tables: /projects/{name}/tables/*
# - Academic Writing: /academic/*
# - All existing functionality preserved
