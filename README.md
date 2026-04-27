# Project Repository Overview

This repository is a backup and documentation of my work during my ARTFX final year project.  
It serves both as a record of past workflows and as a reference for future projects.  
The content will continue to evolve as my experience and understanding grow.

---

## 📂 Docs

This folder contains workflow documentation and production guidelines created during the project.

### 📁 Folder Structure
- Two folder structure documents for two different projects
- Largely similar and can be used as general references

### 📁 Naming Convention
Includes naming standards for:
- Static Mesh
- Skeletal Mesh
- VFX

⚠️ Note:
- The Skeletal Mesh naming convention is tightly coupled with gameplay systems  
  and may have limited reuse value in future projects.

### 📁 Mesh Documentation
- Mesh Guide  
- Mesh Self-Check List  
- Nanite Documentation  

These cover:
- Export settings from Maya or other DCC tools
- Mesh import standards in Unreal Engine
- Mesh-related best practices tied to Unreal Engine features

---

## 🎨 Texture Guide

This section includes:

- Texture workflow guidelines for Substance Painter and Unreal Engine
- Color matching between SP and Unreal using color profile files
- Use of `.bat` files due to restricted system permissions in the school environment

### ⚠️ Notes
- After permissions are unlocked, configurations can be set manually
- **Visual results between SP and Unreal will never match perfectly**
- **Always prioritize Unreal Engine's final rendered result**

---

## 🧪 PBR Guide

- Training material created for artists at the beginning of the project
- Goals:
  - Improve understanding of Physically Based Rendering (PBR)
  - Encourage standardized asset creation through theory + practice
- Emphasizes avoiding purely intuition-based workflows

---

## 🛠 Maya

### Environment Setup
- Maya must be launched via `.bat` file, only this version includes project-specific tools
- This automatically sets required environment variables

### Tools
- FBX Export Tool:
  - Export settings are configured via MEL scripts
  - Pre-configured to meet project standards
  - Supports batch export

### Special Tool
- `export_level_info`
  - Exports transform data from scenes
  - Used for migrating scenes from Maya to Unreal Engine

---

## 🎨 Substance Painter

### Environment Workaround
- School restrictions disabled Color Management
- Resolved by modifying Color Configuration via environment variables

### Additional Issue
- Exported BaseColor maps are in Linear space and cannot be changed

### Solution
- Use a Smart Material:
  - Converts Linear to sRGB

### Other Content
- Includes texture export presets for Substance Painter
