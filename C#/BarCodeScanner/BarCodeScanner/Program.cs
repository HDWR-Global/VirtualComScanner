using System.IO.Ports;

var serialPort = new SerialPort("COM3");

serialPort.Open();

Console.WriteLine("Zeskanuj kod kreskowy:");

while (true)
{
    Console.WriteLine($"Zeskanowany kod: {serialPort.ReadLine()}");
}
