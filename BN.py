import random
import numpy as np
import matplotlib.pyplot as plt

def buffon_needle(L, D, N):
    hit = 0
    for _ in range(N):
        theta = np.pi * random.random() / 2
        if D*random.random() <= L*np.sin(theta):
            hit += 1
    return (2*L*N)/(D*hit)

L = float(input('Masukkan panjang jarum (dalam cm): '))
D = float(input('Masukkan jarak antar garis (dalam cm): '))
N = int(input('Masukkan banyaknya percobaan: '))

if __name__ == "__main__":
    prob = buffon_needle(L, D, N)

    # Membuat scatterplot untuk menampilkan banyaknya percobaan
    fig, ax = plt.subplots(figsize=(10, L))
    for i in range(N):
        # Menentukan posisi jarum secara acak
        x = random.uniform(0, L)*2
        y = random.uniform(0, L)*2
        theta = np.pi * random.random() / 2

        x1 = x - (L) * np.cos(theta - np.pi/2)
        x2 = x + (L) * np.cos(theta - np.pi/2)
        y1 = y - (L) * np.sin(theta - np.pi/2)
        y2 = y + (L) * np.sin(theta - np.pi/2)
        
        # Menentukan warna jarum berdasarkan apakah jarum memotong garis atau tidak
        if D*random.random() <= L*np.sin(theta):
            color = 'red'
        else:
            color = 'blue'
            
        ax.plot([x1, x2], [y1, y2], color=color)
        
    # Membuat legend berdasarkan kategori warna
    for color in ['red', 'blue']:
        ax.plot([], [], color=color, label='Memotong garis' if color == 'red' else 'Tidak memotong garis')
    ax.legend()
    
    # Menambahkan garis vertikal dan horizontal pada jarak antar garis D
    for i in range(0, N, int(D)):
        ax.axvline(i, color='gray', linestyle='--')
    for i in range(0, N, int(D)):
        ax.axhline(i, color='gray', linestyle='--')

    ax.set_xlabel('Percobaan')
    ax.set_title('Simulasi Buffon Needle: L = {} cm, D = {} cm, N = {}'.format(L, D, N))
    ax.text(0.8, 0.9, 'Probabilitas = {:.4f}'.format(prob), transform=ax.transAxes)
    plt.show()