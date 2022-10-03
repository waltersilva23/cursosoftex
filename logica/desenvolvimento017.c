#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int main(void)
{
  float *ponteiro; 
  int i, num_componentes, opcao, novo_num, adic;
  
  num_componentes = 22;
  
  ponteiro = (float *) malloc(num_componentes * sizeof(float));

  printf("\nEsse vetor tem o tamanho 22\n");
  
  for (i = 0; i < num_componentes; i++)
  {
    printf("\nDigite o valor para a posicão %d do vetor: ", i+1);
    scanf("%f",&ponteiro[i]);
  }
  
  printf("\nDeseja adicionar numeros?");
  printf("\n1 - sim");
  printf("\n2 - nao\n");
  scanf("%d", &opcao);

  if (opcao == 1)
  {
    printf("Quantos numeros? ");
    scanf("%d", &novo_num);
    
    adic = novo_num + num_componentes;

    ponteiro = (float *) realloc(ponteiro, adic * sizeof (float));
    for (i = i; i < adic; i++)
  {
    printf("\nDigite o valor para a posicao %d do vetor: ", i+1);
    scanf("%f",&ponteiro[i]);
  }
  }
  else
  {
    adic = num_componentes;
  }

  printf("\n*********** Valores do vetor dinamico ************\n\n");
  
  for (i = 0;i < adic; i++)
  {
    printf("%.2f\n",ponteiro[i]);
  }
  
  free(ponteiro);
  
  getch();
  return 0;
}