/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 18:05:25 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/22 00:06:48 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	main(void)
{
	char 	s1[] = "Hello";
	char	s2[] = "Hello";
	char	s3[] = "HellO";
	char	s4[50];
	int		num = 42;
	char 	*p1;
	//char 	*p2;
	//size_t result;

	ft_atoi(s1);
	printf("atoi - OK\n");

	ft_bzero(s1, ft_strlen(s1));
	printf("bzero - OK\n");

	p1 = (char *)ft_calloc(ft_strlen(s1), sizeof(char));
		if (!p1)
			printf("Error on calloc\n");
		printf("calloc - OK\n");
	free(p1);

	ft_isalnum('4');
/*	if (result == 1)
		printf("Yes\n");
	else
		printf("No\n");*/
	printf("isalnum - OK\n");
	ft_isalpha('A');
	printf("isalpha - OK\n");
	(size_t)ft_isascii('A');
	printf("isascii - OK\n");
	(size_t)ft_isdigit('A');
	printf("isdigit - OK\n");
	ft_isprint('A');
	printf("isprint - OK\n");
	
	ft_itoa(num);
	printf("itoa - OK\n");
	
	ft_memchr(s3, 'l', ft_strlen(s3));
	printf("memchr - OK\n");

	(size_t)ft_memcmp(s2, s3, ft_strlen(s2));
	printf("memcmp - OK\n");
	
	ft_memcpy(s4, s3, ft_strlen(s3));
	printf("memcpy - OK\n");

	


	return (0);
}
