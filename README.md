# Django Multi-Portfolio: Developer Profile & Archery Trajectory

This repository contains the source code for my personal website, structured and developed using the **Django** framework. The project is designed as a modular ecosystem consisting of two main applications that are completely independent in terms of content and visual logic, while sharing the same underlying technological infrastructure.

The deployment and hosting of this web ecosystem are managed entirely locally through a **Self-Hosted** environment configured on my own home server.

---

## 🌐 Internationalization (i18n)

The project implements native multi-language support structured hierarchically into three languages:
1. **Català (Primary Language):** The default language upon loading and the root of the website.
2. **Español (Secondary):** Full translation of modules and database records.
3. **English (Third):** Localization adapted for global technical reach.

---

## 🎨 Design & Visual Identity

The graphical interface of the website strictly applies a custom color palette shared by both applications, adapting the layout blocks according to their independent structures:

* **General Background Color:** `#2c3b4d`
* **Dark Blocks Color (Header & Footer):** `#1b2632`
* **Font / Typography Color:** `#ffb162`
* **Interactive Hover State Color (Button Hover):** `#a35139`

---

## 🏗️ Architecture & Module Structure

### 1. Base System Configurations
* Base Django initialization and isolation of critical credentials (`Secret Keys`, `DB Engine`) using local environment variables.
* Setup of independent static files per application to ensure the segregation of specific styles for both the technical and sports profiles.

### 2. Developer Portfolio Module
* **Base Layout:** Inheritable global template defining the semantic structure of the developer website with its own Header (navigation focused on projects and engineering) and technical Footer.
* **Home Page:** Presentation section featuring a profile picture, full name, professional description, and an exclusive dynamic listing of the top 3 project cards filtered from the database.
* **About Me Page:** Extended biography grouping academic background, career trajectory, technologies currently being learned, and the active tech stack dynamically connected to the data model. Includes a prominent redirect link to the sports annex within the hobbies section.
* **Projects Showcase:** A comprehensive directory that fetches and renders all instances stored in the software projects database model using the same card layout.

### 3. Archery Portfolio Annex
* **Base Layout:** Exclusive base template with a customized header and footer tailored to the aesthetics and navigation of the archery career.
* **Archery Home Page:** Main athletic panel with a sports profile image, categorization, and automated chronological event division: a history of the last 3 competitions held and a roadmap of the next 3 planned tournaments.
* **About Me (Sports Profile):** Detailed archer profile showcasing the active competitive category, technical specifications of the current bow setups, official personal records/marks, and academic history.
* **Competitions Log:** A comprehensive gallery that retrospectively renders all completed competitions registered in the system.

---

## 🗄️ Data Models Schema

Data persistence is structured under three abstractions in the Django ORM, mapped for dynamic management from the admin control panel:

### Project Model (`developer_portfolio`)
* `name` (CharField) — Name of the development project.
* `image` (ImageField / URLField) — Cover image.
* `description` (TextField) — Functional description of the software.
* `tech_stack` (CharField / JSONField) — Technologies used.
* `github_link` (URLField) — Link to the source code repository.

### Skill Model (`developer_portfolio`)
* `name` (CharField) — Name of the technology (e.g., Python, React).
* `category` (CharField) — Classification for rendering purposes (Frontend, Backend, Tools).
* `icon_class` (CharField) — CSS class for icon display (Devicon/FontAwesome).

### Competition Model (`archery_portfolio`)
* `name` (CharField) — Name of the archery tournament or event.
* `description` (TextField) — Summary or notes of the event.
* `position` (IntegerField / CharField) — Final ranking position.
* `mark` (CharField / IntegerField) — Total score achieved (e.g., 680/720).
* `image_or_link` (URLField / ImageField) — Link to official results or certificates.
* `date` (DateField) — Date of the event (used to automatically separate past and upcoming events).
