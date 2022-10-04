#ifndef MATRIX
#define MATRIX

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

u_int* scan_matrix(u_int N) {
	if (N < 0) return NULL;

	int* matrix = (int*) malloc(sizeof(int) * N * N);

	int success = 1;
	for (u_int i = 0; i < N * N; ++i) {
		success = scanf("%d", matrix + i);
		if (!success) {
			printf("Invalid value\n");
			free(matrix);
			return NULL;
		}
	}

	return matrix;
}

int matrix_max(int* matrix, u_int N) {
	int max = INT_MIN;
	for (u_int i = 0; i < N * N; ++i) {
		if (matrix[i] > max) max = matrix[i];
	}
	return max;
}

u_int nrank(int n) {
	n = abs(n);
	u_int rank = 0;

	while (n > 0) {
		n /= 10;
		rank++;
	}

	return rank;
}

void print_matrix(int* matrix, u_int N) {
	int max = nrank(matrix_max(matrix, N));
	char* format = (char*) malloc(8);
	sprintf(format, " %dd ", max + 1);
	format[0] = '%';

	for (u_int i = 0; i < N * N; ++i) {
		printf(format, matrix[i]);
		if (!((i + 1) % N)) printf("\n");
	}
}

void sort_main_diagonal(int* matrix, u_int N) {
	// bubble sort
	for (u_int i = 0; i < N; ++i) {
		for (u_int j = 0; j < N - 1; ++j) {
			if (matrix[j * N + j] > matrix[(j + 1) * N + j + 1]) {
				int tmp = matrix[j * N + j];
				matrix[j * N + j] = matrix[(j + 1) * N + j + 1];
				matrix[(j + 1) * N + j + 1] = tmp;
			}
		}
	}
}

#endif