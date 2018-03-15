#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include "key.h"



int main(void) {

    init();

    while (1) {   }    // Loop forever

    return 0;   /* never reached */
}

void init()
{
    // Initialize I/O Ports
    DDRC &= ~(1<<PC4);
    DDRB |= (1<<PB2);
    DDRB |= (1<<PB1);
    //PORTC |= (1<<PC4);      // Pull-Up

    // Enable Interrupts
    PCICR |= (1<<PCIE1);        // Enable interrupt
    PCMSK1 |= (1<<PCINT12);     // Interrupt at PC4

    // Timer
    TCCR1A |= (1<<WGM11) | (1<<WGM10);       // Set Timer1 to fPWM
    // Compare Output Mode to "Clear on Match and OC1B at Bottom"
    TCCR1A |= (1<<COM1B1);
    TCCR1A &= ~(1<<COM1B0);
    // Set "fPWM with Top at OCR1A and Thresh at OCR1B"
    TCCR1B |= (1<<WGM12) | (1<<WGM13);
    // Prescaler = 64
    TCCR1B |= (1<<CS11) | (1<<CS10);
    // 20ms period
    OCR1A = 5000;
    // PWM
    OCR1B = open[0];

    sei();
}

// Interrupt function
ISR(PCINT1_vect)
{
    if ((PINC & (1<<PC4)) == 0)
        // Open when receives a zero
        OCR1B = open[1];
    else
        // Close
        OCR1B = open[0];
}
