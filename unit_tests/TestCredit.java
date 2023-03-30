/*
To run this test, IntelliJ IDEA is recommended to use.
 */


import org.junit.Test;
import static org.junit.Assert.*;

public class TestCredit {

    @Test
    public void testGUIWorks() {
        CreditGUI.main(null);
    }

    @Test
    public void testValidCard() {
        assertTrue(CreditGUI.isValid(4111111111111111L, "VISA"));
        assertTrue(CreditGUI.isValid(378282246310005L, "AMEX"));
        assertTrue(CreditGUI.isValid(5555555555554444L, "MASTERCARD"));
    }

    @Test
    public void testNotValidCard() {
        assertFalse(CreditGUI.isValid(1234567890L, "VISA"));
        assertFalse(CreditGUI.isValid(1234567890L, "AMEX"));
        assertFalse(CreditGUI.isValid(1234567890L, "MASTERCARD"));
    }

    @Test
    public void testGetCardType() {
        assertEquals("VISA", CreditGUI.getType(4111111111111111L));
        assertEquals("AMEX", CreditGUI.getType(378282246310005L));
        assertEquals("MASTERCARD", CreditGUI.getType(5555555555554444L));
        assertEquals("INVALID", CreditGUI.getType(1234567890L));
    }

    @Test
    public void testChecksum() {
        assertTrue(CreditGUI.checksum(4111111111111111L));
        assertTrue(CreditGUI.checksum(378282246310005L));
        assertTrue(CreditGUI.checksum(5555555555554444L));
        assertFalse(CreditGUI.checksum(1234567890L));
    }
}
