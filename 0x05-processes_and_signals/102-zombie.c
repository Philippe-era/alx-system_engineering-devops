#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


/**
 * infinite_while – Run an infinite loop displaying information
 * Return: Always 0 succeeded 
 */
int infinite_while(void)
{

	int check = 1;
	while (check)
	{
		sleep(check);
	}
	return (0);
}

/**
 * main – zombies will be created processes
 * Return: Always 0. succeedded
 */
int main(void)
{
	pid_t part_destiny;
	char num_check= 0;

	while (num_check< 5)
	{
		part_destiny = fork();
		if (part_destiny > 0)
		{
			printf("Zombie process created, PART_DESTINY:%d\n", part_destiny);
			sleep(1);
			num_check++;
		}
		else
			exit(0);
	}

	infinite_while();
	return (EXIT_SUCCESS);
}


