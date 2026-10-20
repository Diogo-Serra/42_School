<div align="center">
  
<p align="center">
  <img src="https://github.com/Diogo-Serra/42-project-badges/blob/main/covers/banner42.png" alt="Banner">
</p>

---

### About

This repository documents my journey through the **42 Common Core**, from foundational C projects to advanced Unix, and now Python programming with the new common core update.  
Each project follows the school's philosophy: *learn by doing, fail fast, and build resilience through autonomy.*

---

### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg" width="24" height="24" alt="C"/> C Curriculum

<div align="center">
  <a href="https://github.com/Diogo-Serra/42_School/tree/main/get_next_line">
    <img src="https://github.com/Diogo-Serra/42-project-badges/blob/main/badges/volunteerm.png" alt="Reloaded"/>
  </a>
  <a href="https://github.com/Diogo-Serra/42_School/tree/main/libft">
    <img src="https://github.com/Diogo-Serra/42-project-badges/blob/main/badges/libftm.png" alt="Libft"/>
  </a>
  <a href="https://github.com/Diogo-Serra/42_School/tree/main/Born2beRoot">
    <img src="https://github.com/Diogo-Serra/42-project-badges/blob/main/badges/born2beroote.png" alt="Born2beroot"/>
  </a>
  <a href="https://github.com/Diogo-Serra/42_School/tree/main/ft_printf">
    <img src="https://github.com/Diogo-Serra/42-project-badges/blob/main/badges/ft_printfe.png" alt="ft_printf"/>
  </a>
  <br/>
  <a href="https://github.com/Diogo-Serra/42_School/tree/main/reloaded">
    <img src="https://github.com/Diogo-Serra/42-project-badges/blob/main/badges/get_next_linee.png" alt="get_next_line"/>
  </a>
  <a href="https://github.com/Diogo-Serra/42_School/tree/main/push_swap">
    <img src="https://github.com/Diogo-Serra/42-project-badges/blob/main/badges/push_swape.png" alt="push_swap"/>
  </a>
  <a href="https://github.com/Diogo-Serra/Codexion">
    <img src="https://github.com/Diogo-Serra/42-project-badges/blob/main/badges/philosophersn.png" alt="Codexion (formerly Philosophers)"/>
  </a>
</div>

---

### Codexion — threads, mutexes & scheduling

**Codexion** (formerly *Philosophers*) is a concurrency simulation written in C. Coders sit around a circular co-working hub and need **two adjacent USB dongles** to compile quantum code. Each coder is a POSIX thread, so the real subject of the project is coordinating shared state without deadlocks, starvation, or data races.

<div align="center">
  <a href="https://github.com/Diogo-Serra/Codexion">
    <img src="https://img.shields.io/badge/C-POSIX_Threads-00599C?style=for-the-badge&logo=c&logoColor=white" alt="C / POSIX Threads"/>
  </a>
  <a href="https://github.com/Diogo-Serra/Codexion">
    <img src="https://img.shields.io/badge/Scheduler-FIFO_%7C_EDF-6A5ACD?style=for-the-badge" alt="FIFO / EDF"/>
  </a>
</div>

- **Threads:** one thread per coder plus a dedicated monitor thread for burnout detection.
- **Synchronization:** per-dongle mutexes and condition variables, a logging mutex, and a scheduler mutex guarding the shared termination state.
- **Arbitration:** FIFO and Earliest-Deadline-First scheduling backed by a binary-heap priority queue; dongles are granted in a fixed order to break the circular wait.
- **Timing rules:** a dongle cooldown between uses and a burnout deadline that stops the simulation within 10 ms.
- **Output:** timestamped, serialized logs for dongle pickup, compiling, debugging, refactoring, and burnout.

```sh
make
./codexion 5 800 200 200 200 7 100 edf
#          coders burnout compile debug refactor required cooldown scheduler
```

[Source code](https://github.com/Diogo-Serra/Codexion) · [Project notes in this repo](https://github.com/Diogo-Serra/42_School/tree/main/Codexion)

---

<div align="center">

### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="24" height="24" alt="Python"/> Python Curriculum

<div align="center">
  <a href="https://github.com/Diogo-Serra/42_School/tree/main/python_modules">
    <img src="https://img.shields.io/badge/Python_Modules-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Modules"/>
  </a>
  <a href="https://github.com/Diogo-Serra/42_School/tree/main/A-Maze-ing">
    <img src="https://img.shields.io/badge/A--Maze--ing-blue?style=for-the-badge&logo=python&logoColor=white" alt="A-Maze-ing"/>
  </a>
  <br/>
  <a href="https://github.com/Diogo-Serra/Fly-in">
    <img src="https://img.shields.io/badge/Fly--in-blue?style=for-the-badge&logo=python&logoColor=white" alt="Fly-in"/>
  </a>
    <a href="https://github.com/Diogo-Serra/Call_Me_Maybe">
    <img src="https://img.shields.io/badge/Call--me--maybe-blue?style=for-the-badge&logo=python&logoColor=white" alt="Call Me Maybe"/>
  </a>
</div>

<p align="center">
  <b>Python Modules</b>: Progressive exercises and concepts in Python.<br>
  <b>A-Maze-ing</b>: Maze generation and validation in Python.<br>
  <b>Fly-in</b>: Drone fleet routing system with pathfinding across zone networks.<br>
  <b>Call_me_maybe</b>: Decoding engine that turns natural-language prompts into function calls for LLMs.<br>
</p>

---

### Tech & Tools

![Tech & Tools](https://skillicons.dev/icons?i=c,python,bash,cmake,git,vim,vscode,linux,apple,pytorch,docker&theme=dark)

<img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face"/>
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow"/>
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn"/>
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
<img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white" alt="Matplotlib"/>

---

### Connect

<a href="https://www.linkedin.com/in/diogoserra90/"><img src="https://img.shields.io/badge/LinkedIn-Diogo--Serra-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>

</div>
