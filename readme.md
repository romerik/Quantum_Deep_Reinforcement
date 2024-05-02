# Quantum Deep Reinforcement Learning

This repository contains implementations of deep reinforcement learning algorithms trained on Mujoco Humanoid-v4 3D environments and Quantum Parametrized Circuit.

## Deep Reinforcement Learning (Mujoco)

### Folder Structure

```bash
.
├── Deep_Reinforcement_Learning_Mujoco
│   ├── logs
│   │   ├── A2C_0
│   │   ├── DDPG_0
│   │   ├── PPO_0
│   │   ├── SAC_0
│   │   └── TD3_0
│   ├── models
│   │   ├── SAC_1000000.zip
│   │   ├── SAC_100000.zip
│   │   ├── SAC_1025000.zip
│   │   ├── SAC_250000.zip
│   │   ├── SAC_500000.zip
│   │   └── SAC_750000.zip
│   ├── requirements.txt
│   └── train_test_mujoco_drl.py
├─
```


### Content
- `logs`: Contains training logs for different reinforcement learning algorithms.
- `models`: Contains saved weights for the SAC (Soft Actor-Critic) reinforcement learning algorithm.
- `requirements.txt`: List of Python dependencies required to run the code.
- `train_test_mujoco_drl.py`: Script for training and testing deep reinforcement learning models on Mujoco Humanoid-v4 3D environments.

## Quantum Parametrized Circuit

### Folder Structure

```bash
├── Quantum_Parametrized_Circuit
│   ├── circuit.png
│   ├── episodes_rewards.txt
│   ├── gym_walker.gif
│   ├── humanoid_test.py
│   ├── main.py
│   ├── model.png
│   ├── models
│   │   └── model_10.h5
│   ├── requirements.txt
│   └── walker_2D_episodes_reward.png
└──
```


### Content
- `circuit.png`: Image representation of the quantum parametrized circuit.
- `episodes_rewards.txt`: Text file containing rewards obtained during training.
- `gym_walker.gif`: GIF file showing the walker in the 2D environment.
- `humanoid_test.py`: Script for testing the Quantum Parametrized Circuit on Mujoco Humanoid-v4 3D environment.
- `main.py`: Main script for training and testing the Quantum Parametrized Circuit.
- `model.png`: Image representation of the trained model.
- `models`: Directory containing saved model weights.
- `requirements.txt`: List of Python dependencies required to run the code.
- `walker_2D_episodes_reward.png`: Image showing rewards obtained during training in the 2D walker environment.

## Usage
1. Clone the repository:

```bash
git clone https://github.com/your_username/your_repository.git
```

2. Install dependencies:

```bash
cd your_repository
pip install -r Deep_Reinforcement_Learning_Mujoco/requirements.txt
pip install -r Quantum_Parametrized_Circuit/requirements.txt
```

3. Train and test the deep reinforcement learning models using train_test_mujoco_drl.py.

4. Train and test the Quantum Parametrized Circuit using main.py.

# Contributors
- Romerik Lokossou (rlokosso@andrew.cmu.edu)
- Birhanu Shimelis Girma (bgirmash@andrew.cmu.edu)


```bash
Feel free to adjust and expand upon this template to better suit your project's specific details and requirements!
```