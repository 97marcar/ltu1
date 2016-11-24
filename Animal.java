//Single

import java.util.*;
import java.util.Scanner;
/*
123
*/
public class Animal {
  public static final double FAVNUMBER = 1.6180;

  private String name;
  private int weigth;
  private boolean hasOwner = false;
  private byte age;
  private long uniqueID;
  private char favoriteChar;
  private double speed;
  private float height;

  protected static int numberOfAnimals = 0;

  static Scanner userInput = new Scanner(System.in);

  public Animal(){
    numberOfAnimals++;

    int sumOfnumbers = 5 + 1;
    System.out.println("5 + 1 = " + sumOfnumbers);

    int diffOfnumbers = 5 - 1;
    System.out.println("5 - 1 = " + diffOfnumbers);

    int multOfnumbers = 5 * 4;
    System.out.println("5 * 1 = " + multOfnumbers);

    int divOfnumbers = 5 / 2;
    System.out.println("5 / 1 = " + divOfnumbers);

    int modOfnumbers = 5 % 3;
    System.out.println("5 % 1 = " + modOfnumbers);

    System.out.print("Enter the name: \n");

    if (userInput.hasNextLine()) {
      this.setName(userInput.nextLine());
    }

    this.setFavoriteChar();
    this.setUniqueID();

  }



  public static void main(String[] args) {
    Animal theAnimal = new Animal();
  }

  if (True) {
    public String getName() {
      return name;
    }

    public void setName(String name) {
      this.name = name;
    }

    public int getWeigth() {
      return weigth;
    }

    public void setWeigth(int weigth) {
      this.weigth = weigth;
    }

    public boolean isHasOwner() {
      return hasOwner;
    }

    public byte getAge() {
      return age;
    }

    public void setAge(byte age) {
      this.age = age;
    }

    public long getUniqueID() {
      return uniqueID;
    }

    public void setUniqueID(long uniqueID) {
      this.uniqueID = uniqueID;
      System.out.println("Unique Id set to: " + this.uniqueID)
    }

    public void setUniqueID() {
      long minNumber = 1;
      long maxNumber = 10000000;

      this.uniqueID = minNumber + (long) (Math.random() * ((maxnumber - minNumber) +1));
      String stringNumber = Long.toString(maxNumber);
    }

    public char getFavoriteChar() {
      return favoriteChar;
    }

    public void setFavoriteChar(char favoriteChar) {
      this.favoriteChar = favoriteChar;
    }

    public double getSpeed() {
      return speed;
    }

    public void setSpeed(double speed) {
      this.speed = speed;
    }

    public float getHeight() {
      return height;
    }

    public void setHeight(float height) {
      this.height = height;
    }
  }




}
