# Distributed Time-Varying Gaussian Regression via Kalman Filtering (DistKP)

This repository provides a clean and well-documented Python implementation of **DistKP**, a distributed algorithm for **time-varying Gaussian process regression**, as introduced in our paper:

> **Distributed Time-Varying Gaussian Regression via Kalman Filtering**  
> *Nicola Taddei, Riccardo Maggioni, Jaap Eising, Giulia De Pasquale, Dörfler Florian*  
> [paper link](https://arxiv.org/abs/2504.14900)

The implementation is designed to be **accessible, educational, and extensible**, with simulations and detailed explanations provided via **Jupyter notebooks**.

## 🚀 Overview

**DistKP** enables agents in a distributed network to collaboratively estimate a **time-varying function** using **Gaussian Processes** and **Kalman filtering** techniques. It is particularly suited for robotics applications such as:

- **Environmental monitoring**
- **Swarm robotics**
- **Distributed learning in dynamic environments**

### Key Features

- ✅ Modular and readable implementation in Python  
- ✅ Simulation-ready with Jupyter notebooks  
- ✅ Reproducible experiments from the paper  
- ✅ Educational annotations and visualizations  
- ✅ No obscure dependencies – runs with NumPy, SciPy, and Matplotlib  

## 🧠 Algorithm: DistKP

DistKP uses a **state-space GP representation** to model the time-varying behavior of Gaussian processes, leveraging **Kalman filtering** for efficient inference and **message-passing** for distributed communication. Each agent locally processes data and shares limited information with neighbors, enabling scalable regression over time.


## 📓 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Nicola-Taddei/DistributedGP.git
cd DistributedGP
```


### 2. Install dependencies

You can use a virtual environment (e.g., ```venv``` or ```conda```) and then install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Run the notebooks

```bash
jupyter notebook notebooks/
```

## 📁 Repository structure
```
DistKP/
├── notebooks/           # Jupyter notebooks with step-by-step explanations and experiments
├── requirements.txt     # Minimal dependencies
└── README.md
```

We provide two notebooks:
1. **01_introduction.ipynb**: a minimal version of the algorithm.
2. **02_experiments.ipynb**: reproduces the results from the paper.


## 📊 Reproducing the Results

To reproduce the simulation results from the paper, check out the notebook **02_experiments.ipynb**. It includes:

* Convergence plots
* Comparison with centralized and baseline methods

## 🤖 Applications in Robotics

DistKP is ideal for roboticists working with:

* Multi-robot exploration and mapping
* Distributed sensor networks
* Online learning in non-stationary environments

## 📚 Citation

If you find this repository useful in your research, please cite our paper:

```
@misc{taddei2025distributedtimevaryinggaussianregression,
      title={Distributed Time-Varying Gaussian Regression via Kalman Filtering}, 
      author={Nicola Taddei and Riccardo Maggioni and Jaap Eising and Giulia De Pasquale and Florian Dorfler},
      year={2025},
      eprint={2504.14900},
      archivePrefix={arXiv},
      primaryClass={eess.SY},
      url={https://arxiv.org/abs/2504.14900}, 
}
```

## 🤝 Contributing

Contributions are welcome! Whether it's fixing typos, improving documentation, or extending the code – feel free to open a pull request or reach out.
### 📬 Contact

For questions or feedback, you can reach us at: [*taddein@ethz.ch*] and [*rmaggioni@ethz.ch*]

