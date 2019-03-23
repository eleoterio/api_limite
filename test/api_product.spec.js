var should = require("should");
var request = require("request");
var chai = require("chai");
var expect = chai.expect;
var urlBase = "http://localhost:5000/v1";

describe("Teste API produtos",function(){
    it("Deve inserir um json",function(done){
      request.post(
        {
          url : urlBase + "/products",
          json : [{"id": "123", "name": "mesa"}]
        },
        function(error, response, body){
          var _body = {};
          try{
            _body = JSON.parse(body);
          }
          catch(e){
            _body = {};
          }

          expect(response.statusCode).to.equal(200);
  
          done();
        }
      );
    });
    it("Não deixa inserir um json Igual",function(done){
        request.post(
          {
            url : urlBase + "/products",
            json : [{"id": "123", "name": "mesa"}]
          },
          function(error, response, body){
            var _body = {};
            try{
              _body = JSON.parse(body);
            }
            catch(e){
              _body = {};
            }
  
            expect(response.statusCode).to.equal(403);
    
            done();
          }
        );
      });
});