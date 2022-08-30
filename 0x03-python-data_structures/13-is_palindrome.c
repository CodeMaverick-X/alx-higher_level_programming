#include "lists.h"
/**
 * is_palindrome - checks if a list is palindrome
 * @head: pointer to the head of the list
 * Return: 1 if is and 0 if not
 * Description: we shall find the middle of the list and
 * check if it is even or odd,  we then point to the middle
 * with a pointer mid and reverse that second part of the list
 * check if it is palindrome and then reverse it back before
 * we return
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *mid = NULL;
	listint_t *temp = *head;
	int flag;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			mid = slow->next;

			break;
		}

		if (!fast->next)
		{
			mid = slow->next->next;

			break;
		}

	}

	reverse(&mid);
	flag = check(&temp, &mid);
	reverse(&mid);

	return (flag);
}

/**
 * reverse - reverse a linked list
 * @head: pointer to the middle of the original list
 * Return: none
 */
void reverse(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL, *temp = *head;

	while (temp)
	{
		next = temp->next;
		temp->next = prev;
		prev = temp;
		temp = next;
	}
	*head = prev;
}

/**
 * check - actual check for the two halves two halves of the list
 * @head1: pointer to the head of the original list
 * @mid1: pointer to the pointer to the head of the reversed list
 *
 * Return: intiger 1 or 0
 */
int check(listint_t **head1, listint_t **mid1)
{
	listint_t *head = *head1, *mid = *mid1;
	int flag = 1;

	while (head && mid)
	{
		if (head->n == mid->n)
		{
			head = head->next;
			mid = mid->next;
		}
		else
		{
			flag = 0;
			break;
		}
	}
	return (flag);
}
