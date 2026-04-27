*-Chinese Below-*

*-中文在下方-*

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

---

# 项目仓库说明

本仓库是我在 ARTFX 毕业项目期间部分工作的备份与整理。  
这些内容不仅记录了我当时的工作流程，也作为后续项目的参考资料。  
未来随着经验和认知的提升，我也会持续对仓库内容进行更新和优化。

---

## 📂 Docs

该目录包含毕业项目相关的工作流文档与规范说明：

### 📁 Folder Structure
- 为两个不同项目编写的美术资源目录结构规范
- 内容整体相似，可作为通用参考

### 📁 Naming Convention
- 包含三类命名规范：
  - Static Mesh
  - Skeletal Mesh
  - VFX
- ⚠️ 其中 Skeletal Mesh 命名规范与 Gameplay 机制强相关，后续参考价值有限

### 📁 Mesh 相关文档
- Mesh Guide  
- Mesh Self-Check List  
- Nanite 文档  

主要内容包括：
- 从 Maya 或其他 DCC 软件导出 Mesh 的设置规范
- Unreal Engine 中导入 Mesh 的规范
- 与 Unreal Engine 特性相关的 Mesh 使用规范

---

## 🎨 Texture Guide

该部分主要说明：

- Substance Painter 与 Unreal Engine 的贴图规范
- 使用 Color Profile 文件对齐 SP 与 Unreal 的颜色表现
- 使用 `.bat` 文件的原因：
  - 学校锁定了系统配置权限
  - 通过 `.bat` 临时修改环境变量

### ⚠️ 注意事项
- 后期在获得权限后，可通过手动方式配置环境变量
- **SP 与 Unreal 的显示效果不可能完全一致**
- **一切以 Unreal Engine 最终渲染效果为准**

---

## 🧪 PBR Guide

- 项目初期为美术同学准备的培训资料
- 目标：
  - 帮助理解 PBR（Physically Based Rendering）原理
  - 结合理论与实践，规范资产制作流程
- 强调避免仅凭直觉制作资产

---

## 🛠 Maya

### 环境说明
- 必须通过 `.bat` 文件启动 Maya
- 启动后会自动配置环境变量
- 只有通过该方式启动的 Maya 才包含项目工具

### 工具内容
- FBX 导出工具：
  - 导出相关设置通过 MEL 脚本进行配置
  - 已内置项目规范配置
  - 支持批量导出

### 特殊工具
- `export_level_info`
  - 用于导出场景 Transform 信息
  - 用于 Maya 场景迁移至 Unreal Engine 的特殊需求

---

## 🎨 Substance Painter

### 环境问题与解决方案
- 学校锁定了 Color Management
- 通过修改环境变量中的 Color Configuration 进行绕过

### 额外问题
- 导出的 BaseColor 为 Linear Space 且无法修改

### 解决方案
- 使用 Smart Material：
  - 将 Linear 转换为 sRGB

### 其他内容
- 存储了 SP 的贴图导出预设
