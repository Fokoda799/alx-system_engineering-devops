#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Function to run an infinite loop
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t child_pid;

	while (1)
	{
		child_pid = fork();

		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
		}
	}

	infinite_while();
	return (0);
}

