import cv2 as cv
from matplotlib import pyplot as plt
import sys
import os

# img = cv.imread('img1.png', 3)

# color = ('b', 'g', 'r')

# for i,c in enumerate(color):
# 	hist = cv.calcHist([img], [i], None, [256], [0,256])
# 	plt.plot(hist, color = c)
# 	plt.xlim([0,256])

# plt.show()
# cv.waitKey(0)

def histogram(dir_name, method_num):

	files = [entry for entry in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, entry))]
	num_files = len(list(files))
	if (num_files != 25):
		print("[nome_diretório] deve conter exatos 25 arquivos")
	else:
		for file1 in files:
			img1 = cv.imread(os.path.join(dir_name, file1))
			hist_img1 = cv.calcHist([img1], [0,1,2], None, [8,8,8], [0,256,0,256,0,256])
			cv.normalize(hist_img1, hist_img1, 0, 255, cv.NORM_MINMAX)
			for file2 in files:
				if (file1 != file2):
					img2 = cv.imread(os.path.join(dir_name, file2))
					hist_img2 = cv.calcHist([img2], [0,1,2], None, [8,8,8], [0,256,0,256,0,256])
					cv.normalize(hist_img2, hist_img2, 0, 255, cv.NORM_MINMAX)
					sc = 0
					if (method_num == 2):
						sc = cv.compareHist(hist_img1, hist_img2, cv.HISTCMP_CORREL)
					elif (method_num == 3):
						sc = cv.compareHist(hist_img1, hist_img2, cv.HISTCMP_CHISQR)
					elif (method_num == 4):
						sc = cv.compareHist(hist_img1, hist_img2, cv.HISTCMP_INTERSECT)
					elif (method_num == 5):
						sc = cv.compareHist(hist_img1, hist_img2, cv.HISTCMP_BHATTACHARYYA)
					print(sc)
		

def main():

	if (len(sys.argv) == 3):
		match sys.argv[1]:
			case "1":
				print("Método escolhido: Distância Euclidiana")
			case "2":
				print("Método escolhido: Correlação")
			case "3":
				print("Método escolhido: Chi-Square")
			case "4":
				print("Método escolhido: Intersection")
			case "5":
				print("Método escolhido: Bhattacharyya")
			case _:
				print("[num_método] deve ser um número de 1 a 5")
		n = int(sys.argv[1])
		if (n >= 1) and (n <= 5):
			histogram(sys.argv[2], n)
	else:
		print("Forma de uso: python3 histograma.py [num_método] [nome_diretório]")

if __name__ == "__main__":
	main()