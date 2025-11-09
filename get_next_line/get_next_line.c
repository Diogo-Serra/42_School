/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:08 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/09 18:19:13 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

/* static char	*load_storage(char **storage)
{
	
} */

static int	ft_count_reads(int fd, const char *buffer)
{
	size_t		readBytes;
	int	reads;

	reads = 0;
	readBytes = 0;
	while ((readBytes = read(fd, &buffer, BUFFER_SIZE)) > 0)
		reads++;
	return (reads);
}

/* static int	ft_save_storage(int fd, const char *buffer, char *storage)
{
	size_t		readBytes;
	int	reads;

	reads = 0;
	readBytes = 0;
	while ((readBytes = read(fd, &buffer, BUFFER_SIZE)) > 0)
		reads++;
	return (reads);
} */

char *get_next_line(int fd)
{
	char		buffer[BUFFER_SIZE + 1];
	static char	**storage;
	size_t		readBytes;
	int			reads;
	int			i;

	reads = ft_count_reads(fd, buffer);
	i = 0;
	storage = ft_calloc(reads + 1, sizeof(char *));
	if (!storage)
		return (NULL);
	printf("read %d time(s)\n", reads);
	return (storage[i]);
}

int main(void)
{
    char    *out;
    int     fd;

    fd = open("test.txt", O_RDONLY);
    out = get_next_line(fd);
    free (out);
	return (0);
}
