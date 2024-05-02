import gymnasium as gym
from stable_baselines3 import SAC, TD3, A2C, DQN, DDPG, HER, PPO
import os
import argparse

# Create directories to hold models and logs
model_dir = "models"
log_dir = "logs"
os.makedirs(model_dir, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)

def train(env, sb3_algo, policy_type, learning_rate=None):
    """
    Trains a model using the specified algorithm and policy type.

    Args:
        env (gym.Env): The gym environment to train on.
        sb3_algo (str): The algorithm to use. Must be one of 'SAC', 'TD3', 'A2C', 'DQN', 'DDPG', 'HER', or 'PPO'.
        policy_type (str): The policy type to use. Must be one of 'MlpPolicy', 'CnnPolicy', or 'MultiInputPolicy'.
        learning_rate (float, optional): The learning rate to use. Defaults to None.
    """

    # Check that the policy type is valid
    if policy_type not in ['MlpPolicy', 'CnnPolicy', 'MultiInputPolicy']:
        print('Policy type not found')
        return

    # Check that the algorithm is valid
    if sb3_algo not in ['SAC', 'TD3', 'A2C', 'DQN', 'DDPG', 'HER', 'PPO']:
        print('Algorithm not found')
        return

    # Set up the arguments to create the model
    if learning_rate is None:
        arguments = {
            'env': env,
            'policy': policy_type,
            'verbose': 1,
            'device': 'cuda',
            'tensorboard_log': log_dir
        }
    else:
        arguments = {
            'env': env,
            'policy': policy_type,
            'learning_rate': learning_rate,
            'verbose': 1,
            'device': 'cuda',
            'tensorboard_log': log_dir
        }

    # Create the model
    algorithms = {'SAC': SAC, 'TD3': TD3, 'A2C': A2C, 'DQN': DQN, 'DDPG': DDPG, 'HER': HER, 'PPO': PPO}
    model = algorithms[sb3_algo](**arguments)

    TIMESTEPS = 25000
    iters = 0
    while True:
        iters += 1
        model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False)
        model.save(f"{model_dir}/{sb3_algo}_{policy_type}_{TIMESTEPS*iters}")

def test(env, sb3_algo, path_to_model):
    algorithms = {'SAC': SAC, 'TD3': TD3, 'A2C': A2C, 'DQN': DQN, 'DDPG': DDPG, 'HER': HER, 'PPO': PPO}
    #Loading the model for test purpose
    model = algorithms[sb3_algo].load(path_to_model, env=env)

    obs = env.reset()[0]
    done = False
    extra_steps = 500
    while True:
        action, _ = model.predict(obs)
        obs, _, done, _, _ = env.step(action)

        if done:
            extra_steps -= 1

            if extra_steps < 0:
                break


if __name__ == '__main__':

    # Parse command line inputs
    import argparse

    # Parse command line inputs
    parser = argparse.ArgumentParser(description='Train or test model.')
    parser.add_argument('--gymenv', required=True, help='Gymnasium environment i.e. Humanoid-v4')
    parser.add_argument('--sb3_algo', required=True, help='StableBaseline3 RL algorithm i.e. SAC, TD3')
    parser.add_argument('--policy_type', required=True, help='Policy type to use i.e. MlpPolicy, CnnPolicy, MultiInputPolicy')
    parser.add_argument('--learning_rate', type=float, required=False, help='Learning rate')
    parser.add_argument('-t', '--train', action='store_true', help='Train the model')
    parser.add_argument('-s', '--test', metavar='path_to_model', help='Test the model with the provided model path')
    args = parser.parse_args()



    if args.train:
        gymenv = gym.make(args.gymenv, render_mode=None)
        train(gymenv, args.sb3_algo, args.policy_type, learning_rate=args.learning_rate)

    if(args.test):
        if os.path.isfile(args.test):
            gymenv = gym.make(args.gymenv, render_mode='human')
            test(gymenv, args.sb3_algo, path_to_model=args.test)
        else:
            print(f'{args.test} not found.')