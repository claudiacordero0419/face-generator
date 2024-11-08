import matplotlib.pyplot as plt
import numpy as np


def generate_face(color, emotion):
  fig, ax = plt.subplots()
  ax.set_aspect('equal')
  ax.axis('off')

  # Head
  head = plt.Circle((0.5, 0.5), 0.4, color=color, ec='black')
  ax.add_artist(head)

  # Eyes
  left_eye = plt.Circle((0.35, 0.6), 0.05, color='white', ec='black')
  right_eye = plt.Circle((0.65, 0.6), 0.05, color='white', ec='black')
  ax.add_artist(left_eye)
  ax.add_artist(right_eye)

  # Pupils
  if emotion == 'happy':
    left_pupil = plt.Circle((0.35, 0.6), 0.02, color='black')
    right_pupil = plt.Circle((0.65, 0.6), 0.02, color='black')
  elif emotion == 'sad':
    left_pupil = plt.Circle((0.35, 0.6), 0.02, color='black', fc='white')
    right_pupil = plt.Circle((0.65, 0.6), 0.02, color='black', fc='white')
  else:
    left_pupil = plt.Circle((0.35, 0.6), 0.02, color='black')
    right_pupil = plt.Circle((0.65, 0.6), 0.02, color='black')

  ax.add_artist(left_pupil)
  ax.add_artist(right_pupil)

  # Mouth
  if emotion == 'happy':
    mouth = plt.Circle((0.5, 0.4), 0.1, color='none', ec='black')
    ax.add_artist(mouth)
    ax.plot([0.4, 0.5, 0.6], [0.35, 0.3, 0.35], color='black')
  elif emotion == 'sad':
    mouth = plt.Circle((0.5, 0.4), 0.1, color='none', ec='pink')
    ax.add_artist(mouth)
    ax.plot([0.4, 0.5, 0.6], [0.35, 0.4, 0.35], color='pink')
  else:
    mouth = plt.Rectangle((0.4, 0.4), 0.2, 0.05, color='pink')
    ax.add_artist(mouth)

  plt.xlim(0, 1)
  plt.ylim(0, 1)
  plt.show()


# Example usage:
skin_colors = ['#f8d9cc', '#ebb280', '#dbac7f',
               '#c68642', "#8d5524", "#ffdbac", "#e0ac69", 
               "#946a3e", "c49869"]  # Example skin colors
emotions = ['happy', 'sad', 'neutral']  # Example emotions

for color in skin_colors:
  for emotion in emotions:
    generate_face(color, emotion)
