using ServiceCatalog.Domain;
using System.Net;

namespace ServiceCatalog
{
    /*
        Main metodu olan sınıf aslında bir Executable çıktının çalışma zamanında giriş noktasıdır (EntryPoint)
        internal erişim belirleyicisi sadece bu Assembly(Executable) içerisinde kullanılabilir anlamına gelir.
        internal dışında public, private, protected gibi farklı Access Modifier'lar da vardır.

        Main genelde bir değer döndürmez ama bazı durumlarda int gibi dönüşleri olabilir.

        Varsayılan durumda(Default) tüm türler bir namespace içerisinde yer alır.

        Senaryomuzda servisleri tanımlayan bir sınıfımız(nesne tasarımı) olacak.
        Bunların listesini tutan da bir container yapısı kullanacağız.
    */
    internal class Program
    {
        static void Main(string[] args)
        {
            // Servis nesnesini aşağıdaki gibi default constructor veya parametreli private yapılmış versiyonu ile çalıştıramayız.
            // Service redisService = new Service()

            //TODO@Everyone Create fonksiyonundan geriye null değer dönsün istemiyorum. Kodu okurken daha anlaşılır olmasını da istiyorum. Ne yaparsınız?
            var redisService = Service.Create("Redis Service", new IPAddress([0, 0, 0, 0]), 6379);
            if (redisService == null)
            {
                throw new Exception("Service Error: Service was not created successfully.");
            }
        }
    }
}
