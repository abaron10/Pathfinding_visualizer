

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Pathfinding visualizer</h3>
 
</p>

<p align="center">
    <img src="https://user-images.githubusercontent.com/64280930/150973888-253fefea-eaff-48d2-8222-c60a0c0a570f.png"  width="300">
  </a>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
 This project focuses on the use of search algorithms (A*) applied to heuristic and informed graphs. The goal of this is to find the shortest path between two points, where the start marker is orange and the end marker is purple.
 <p align="center">
    <img src="https://user-images.githubusercontent.com/64280930/150982811-b3ca139c-e6d4-4128-93b3-74f1844711a5.png"  width="700">
  </a>
</p>


### A* Algorithm
A* (pronounced "A-star") is a graph traversal and path search algorithm, which is often used in many fields 
of computer science due to its completeness, optimality, and optimal efficiency.One major practical drawback is its O(b^d) space complexity,
as it stores all generated nodes in memory. Thus, in practical travel-routing systems, 
it is generally outperformed by algorithms which can pre-process the graph to attain better performance,as well as memory-bounded approaches; however, A* is still the best solution in many cases.

### Time Complexity
The time complexity of A* depends on the heuristic. In the worst case of an unbounded search space,
the number of nodes expanded is exponential in the depth of the solution (the shortest path) d: O(bd), 
where b is the branching factor (the average number of successors per state).This assumes that a goal state exists at all, 
and is reachable from the start state; if it is not, and the state space is infinite, the algorithm will not terminate.

The heuristic function has a major effect on the practical performance of A* search, since a good heuristic allows A* to prune away many 
of the bd nodes that an uninformed search would expand. Its quality can be expressed in terms of the effective branching factor b*,
which can be determined empirically for a problem instance by measuring the number of nodes generated by expansion, N, and the depth of the solution,
then solving:

<p align="center">
    <img src="https://user-images.githubusercontent.com/64280930/150975417-13610a1f-9d5d-4390-858b-2414830eca3e.png"  width="300">
  </a>
</p>


Good heuristics are those with low effective branching factor (the optimal being b* = 1).

The time complexity is polynomial when the search space is a tree, there is a single goal state, and the heuristic function h meets the following condition:

<p align="center">
    <img src="https://user-images.githubusercontent.com/64280930/150975509-9a7fb920-8288-40a0-abff-6316de3e753a.png"  width="300">
  </a>
</p>


where h* is the optimal heuristic, the exact cost to get from x to the goal. In other words, the error of h will not grow faster than the 
logarithm of the "perfect heuristic" h* that returns the true distance from x to the goal.

The space complexity of A* is roughly the same as that of all other graph search algorithms, as it keeps all generated nodes in memory. In practice, this turns out to be the biggest drawback of A* search, leading to the development of memory-bounded heuristic searches, such as Iterative deepening A*, memory bounded A*, and SMA*.

### Relations to other algorithms
What sets A* apart from a greedy best-first search algorithm is that it takes the cost/distance already traveled, g(n), into account.

Some common variants of Dijkstra's algorithm can be viewed as a special case of A* where the heuristic h(n) = 0 for all nodes;in turn, both Dijkstra and A* are special cases of dynamic programming.A* itself is a special case of a generalization of branch and bound.


### Built With

* [Pygame](https://www.pygame.org/news)
* [Python](https://www.python.org/)


<!-- GETTING STARTED -->
## Getting Started



### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/abaron10/Pathfinding_visualizer.git
   ```

  2. Create virtual environment
   ```
    virtualenv vnv
   ```
  3. Activate virtualenv
  ```
  source vnv/bin/activate
  ```
  4. On root, run the project
  ```
  python3 Visualizer.py
  ```

### Visualizer controls
| Button             | Task                |
|-----------------------|----------------------------|
| Left Click | Create / Set a new start-end-barrier node |
| Middle Click| Reset Grid |
| Right Click | Undo start-end-barrier node |

<p align="center">
    <img src="https://user-images.githubusercontent.com/64280930/150977892-d41152dd-5585-4d78-a1a5-ea4fd461e82e.png"  width="600">
  </a>
</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch 
3. Commit your Changes 
4. Push to the Branch 
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

https://www.linkedin.com/in/andres-baron-sandoval-76ab96186/ - af.baron10@uniandes.edu.co

Project Link: [https://github.com/abaron10/Pathfinding_visualizer](https://github.com/abaron10/Pathfinding_visualizer)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Pygame](https://www.pygame.org/news)
* [Python](https://www.python.org/)
* Algorithms
* Computer Science





