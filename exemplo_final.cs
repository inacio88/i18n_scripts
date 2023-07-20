using System;

namespace HelloWorld
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("TT".i18n());
      var oi = "{0:n2}";
      var o2i = "n{_percentDesc}";
      var ois = "{0:n3}";    
      var oifes = "dd/MM/yyyy HH:mm";    
      var oei = "MM/yyyy";    
      var ogi = "dd/MM/yyyy";    
      var obi = "T0";    
      var oie = "Faturar/Cancelar".i18n();    
      var oie = "Selecione os itens que deseja liberar.".i18n();    
      var oie = "Deseja cancelar os registros selecionados?".i18n();    
      var oie = "Deseja realizar o cancelamento na data do documento?".i18n();    
      var oie = "Não foi possível realizar 7a liberação de alguns registros:\n".i18n();

      var oie2 = "Não foi possível realizar 7a liberação de alguns registros:\n".i18n().i18n();


    oioi("Primeiro texto".i18n(), "Segundo texto".i18n());

    }

    public void oioi(String texto, String maisTesto){

    }
  }
}