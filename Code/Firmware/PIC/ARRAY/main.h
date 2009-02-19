#ifndef MAIN_H
#define MAIN_H

#define SLAVE
#define ADC_DELAY	1000			// Delay between readings in microseconds.
#define ARS_SAMPLES	8

void	high_isr 		(void);
void	high_vec 		(void);
void 	low_vec  		(void);
void 	low_isr  		(void);

void	read_antennas	(void);
void	read_ars		(void);
void	interrupt		(char);
void	cal_ars			(void);
void	cal_ant			(void);
void	line_follow		(void);
void	corner_detection(void);
void	line_detection	(void);

union int_byte
{
	unsigned int lt;
	unsigned char bt[2];
};	