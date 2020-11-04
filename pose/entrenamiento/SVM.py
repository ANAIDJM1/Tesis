import argparse
import sys
import os
import pickle
import shutil

from sklearn import svm
from sklearn.metrics import accuracy_score

sys.path.insert(0, '/home/any/Imágenes/tesis/')
from pose.entrenamiento.ReadData import Leer_data_files, separar_data


def parse_args():
	parser = argparse.ArgumentParser(description = 'Entrenamiento SVM')
	#se tiene que dar archivos .csv individuales basados en e ID detallados en las poses en determinacionPosicion.py
	parser.add_argument('csv_files', help = 'La coma separa la lista de la ruta de los archivos .cvs', type = str)
	parser.add_argument('--output-path', dest = 'output_path', type = str, default = None,
						help = 'Ruta del folder donde se almacenan los modelos entrenados')
	parser.add_argument('--train-test-split', dest = 'train_test_split', default = 0.85, type = float,
					    help = 'Radio de entrenamiento del test dataset(0-1)')
	parser.add_argument('--max-samples', dest = 'max_samples', type = int, default = 800,
						help = 'Maximo numero de muestras por clase permitido')
	args = parser.parse_args()
	return args

def aplica_SVM(train_data, test_data, output_at):
	X_train, y_train = train_data
	X_test, y_test = test_data

	clf = svm.SVC() #aqui realiza el entrenamiento por SVM, y se puede definir un kernel tipo lineal, sigmoide, poly..
	clf.fit(X_train, y_train)  

	y_test_pred = clf.predict(X_test)
	test_acc = accuracy_score(y_test, y_test_pred)
	print('SVM Test - Confianza o Precision (Accuracy): {:.5f}'.format(test_acc))

	shutil.rmtree(output_at, ignore_errors = True)
	os.mkdir(output_at)
	with open('{}/svc.pickle'.format(output_at), 'wb') as handle:
		pickle.dump(clf, handle, protocol = pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
	args = parse_args()

	data_files = [os.path.abspath(p.strip()) for p in args.csv_files.split(',')]
	X_data, y_data = Leer_data_files(data_files, args.max_samples)
	train_data, test_data = separar_data(X_data, y_data, args.train_test_split)

	# Si no se menciona el folder de salida, entonces se crea uno
	# Se limpia y se crea de nuevo.
	output_at = 'checkpoint' if args.output_path is None else os.path.abspath(args.output_path)

	aplica_SVM(train_data, test_data, output_at)