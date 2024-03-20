import cv2 as cv
from matplotlib import pyplot as plt
import sys
import os

def histogram(files, dir_name, method_num, conf_mat):

	num_files = len(list(files))
	if (num_files != 25):
		print("[nome_diretório] deve conter exatos 25 arquivos")
	else:
		for i,file1 in enumerate(files):
			img1 = cv.imread(os.path.join(dir_name, file1))
			hist_img1 = cv.calcHist([img1], [0,1,2], None, [8,8,8], [0,256,0,256,0,256])
			cv.normalize(hist_img1, hist_img1, 0, 255, cv.NORM_MINMAX)
			sc = []
			for j,file2 in enumerate(files):
				if (file1 != file2):
					img2 = cv.imread(os.path.join(dir_name, file2))
					hist_img2 = cv.calcHist([img2], [0,1,2], None, [8,8,8], [0,256,0,256,0,256])
					cv.normalize(hist_img2, hist_img2, 0, 255, cv.NORM_MINMAX)
					if (method_num == 1):
						sc.append(0.0)
					elif (method_num == 2):
						sc.append(cv.compareHist(hist_img1, hist_img2, cv.HISTCMP_CORREL))
					elif (method_num == 3):
						sc.append(cv.compareHist(hist_img1, hist_img2, cv.HISTCMP_CHISQR))
					elif (method_num == 4):
						sc.append(cv.compareHist(hist_img1, hist_img2, cv.HISTCMP_INTERSECT))
					elif (method_num == 5):
						sc.append(cv.compareHist(hist_img1, hist_img2, cv.HISTCMP_BHATTACHARYYA))
				else:
					if (method_num == 1):
						sc.append(0.0)
					elif (method_num == 2):
						sc.append(1.0)
					elif (method_num == 3):
						sc.append(float("inf"))
					elif (method_num == 4):
						sc.append(float("inf"))
					elif (method_num == 5):
						sc.append(float("inf"))
			conf_mat.append(sc)

def accuracy(files, conf_mat, ac):

	for i in len(files):
		similar = []
		for j in len(files):
			if (i != j) and (conf_mat[i][j] >= 0.91):
				similar.append(files[j])


def main():

	if (len(sys.argv) == 3):
		if (sys.argv[1] == "1"):
			print("Método escolhido: Distância Euclidiana")
		elif (sys.argv[1] == "2"):
			print("Método escolhido: Correlação")
		elif (sys.argv[1] == "3"):
			print("Método escolhido: Chi-Square")
		elif (sys.argv[1] == "4"):
			print("Método escolhido: Intersection")
		elif (sys.argv[1] == "5"):
			print("Método escolhido: Bhattacharyya")
		else:
			print("[num_método] deve ser um número de 1 a 5")
		n = int(sys.argv[1])
		files = [entry for entry in os.listdir(sys.argv[2]) if os.path.isfile(os.path.join(sys.argv[2], entry))]
		if (n >= 1) and (n <= 5):
			conf_mat = []
			histogram(files, sys.argv[2], n, conf_mat)
			print("Matriz de confusão:")
			for i in range(25):
				for j in range(25):
					print(conf_mat[i][j])
				print()
			ac = []
			accuracy(files, conf_mat)
	else:
		print("Forma de uso: python3 histograma.py [num_método] [nome_diretório]")

if __name__ == "__main__":
	main()