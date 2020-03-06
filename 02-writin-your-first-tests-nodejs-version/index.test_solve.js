const expect = require('chai').expect;
const app = require('./index');

describe('Special numbers', function(){
    describe('isSpecialNumber', function(){
        it('should return true for numbers that contain Pi or are divisible by 7 or a prime or are happy', function(){
            expect( app.isSpecialNumber(7) ).to.equal(true);
            expect( app.isSpecialNumber(68) ).to.equal(true);
            expect(app.isSpecialNumber(179) ).to.equal(true);
            expect(app.isSpecialNumber(563) ).to.equal(true);
            expect(app.isSpecialNumber(827) ).to.equal(true);

            expect( app.isSpecialNumber(4) ).to.equal(false);
            expect( app.isSpecialNumber(12) ).to.equal(false);
        })
    });
});

describe('Special numbers', function(){
    describe('isDivisibleBy7', function(){
        it('should return true for numbers divisible by 7', function(){
            const resultOf14 = app.isDivisibleBy7(14);
            const resultOf21 = app.isDivisibleBy7(21);
            const resultOf70 = app.isDivisibleBy7(70);

            expect(resultOf14).to.equal(true);
            expect(resultOf21).to.equal(true);
            expect(resultOf70).to.equal(true);
        });

        it('should return false for numbers not divisible by 7', function(){

            const resultOf10 = app.isDivisibleBy7(10);
            const resultOf22 = app.isDivisibleBy7(22);
            const resultOf61 = app.isDivisibleBy7(61);

            expect(resultOf10).to.equal(false);
            expect(resultOf22).to.equal(false);
            expect(resultOf61).to.equal(false);
        });
    });

    describe('contains Pi', function(){
        it('should return true for numbers that contain 314', function(){

            const resultOf17 = app.hasPi(17);
            const resultOf70 = app.hasPi(70);
            const resultOf314 = app.hasPi(314);
            const resultOf1314 = app.hasPi(1314);
            const resultOf13147 = app.hasPi(13147);

            expect(resultOf17).to.equal(false);
            expect(resultOf70).to.equal(false);
            expect(resultOf314).to.equal(true);
            expect(resultOf1314).to.equal(true);
            expect(resultOf13147).to.equal(true);
        });

        it('should return false for numbers that dont contain Pi', function(){
            const resultOf17 = app.hasPi(4);
            const resultOf70 = app.hasPi(21);
            const resultOf13147 = app.hasPi(13147);

            expect(resultOf17).to.equal(false);
            expect(resultOf70).to.equal(false);
            expect(resultOf13147).to.equal(true);
        });
    });

    describe('is prime', function(){
        it('should return true for numbers are divisible only by themselves and one', function(){

            const resultOf29 = app.isPrime(29);
            const resultOf37 = app.isPrime(37);
            const resultOf71 = app.isPrime(71);
            const resultOf89 = app.isPrime(89);

            expect(resultOf29).to.equal(true);
            expect(resultOf37).to.equal(true);
            expect(resultOf71).to.equal(true);
            expect(resultOf89).to.equal(true);
        });
        
        it('should return false for numbers that are not prime', function(){
            const resultOf93 = app.isPrime(92);
            const resultOf96 = app.isPrime(96);
            
            expect(resultOf93).to.equal(false);
            expect(resultOf96).to.equal(false);
            
        });
    });

    describe('Happy numbers', function(){
        it('should return true for numbers that are happy', function(){

            const resultOf1 = app.isHappy(1);
            const resultOf2111 = app.isHappy(2111);
            const resultOf1997 = app.isHappy(1997);
            const resultOf89 = app.isHappy(89);

            expect(resultOf1).to.equal(true);
            expect(resultOf2111).to.equal(true);
            expect(resultOf1997).to.equal(false);
            expect(resultOf89).to.equal(false);
        });
        
        it('nextHappyNumber should return the next valid happy number', function(){
            const resultOf1 = app.nextHappyNumber(1);
            const resultOf97 = app.nextHappyNumber(97);
            const resultOf2111 = app.nextHappyNumber(2111);
            
            expect(resultOf1).to.equal(7);
            expect(resultOf97).to.equal(100);
            expect(resultOf97).to.not.equal(97);
            expect(resultOf2111).to.equal(2112);
            
        });
    });
});
