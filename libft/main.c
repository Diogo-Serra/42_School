/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 18:05:25 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/21 19:10:52 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	main(void)
{
	char 	s1[] = "Hello";
	char 	*s2;
	int		num = 42;
	char	s3[] = "Hello";

	size_t result;

	result = ft_atoi(s1);
	printf("atoi - OK\n");

	ft_bzero(s1, ft_strlen(s1));
	printf("bzero - OK\n");

	s2 = (char *)ft_calloc(ft_strlen(s1), sizeof(char));
		if (!s2)
			printf("Error on calloc\n");
		printf("calloc - OK\n");
	free(s2);

	result = ft_isalnum('4');
/*	if (result == 1)
		printf("Yes\n");
	else
		printf("No\n");*/
	printf("isalnum - OK\n");
	
	result = (size_t)ft_isalpha('A');
	printf("isalpha - OK\n");
	
	result = (size_t)ft_isascii('A');
	printf("isascii - OK\n");

	result = (size_t)ft_isdigit('A');
	printf("isdigit - OK\n");
	
	result = (size_t)ft_isprint('A');
	printf("isprint - OK\n");

	s2 = ft_itoa(num);
	printf("itoa - OK\n");

	s2 = ft_memchr(s3, 'l', ft_strlen(s3));
	printf("memchr - OK\n");

	result = (int)ft_memcmp(s1, s3, ft_);

	
	return (0);
}
