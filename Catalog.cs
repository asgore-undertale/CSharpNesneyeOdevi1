using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace ServiceCatalog.Domain
{
    /// <summary>
    /// Servisler listesini tutan, yöneten nesnedir
    /// </summary>
    public class Catalog
    {
        /*
            Mümkün mertebe null değer kullanımından kaçınmak lazım.
            Null check kod yönetimi ve okunurluğu açısından hatta iş kurallarının anlaşılırlığı açısından pek tercih edilmemelidir.

            Aşağıdaki özellikler yine read-only tanımlanmıştır. Ancak varsayılan değerleri de set edilmiştir.
            private set oldukları içinden nesne örneği üzerinden doğrudan değiştirilemezler ama buradaki gibi = operatörü ile ilk değerleri verilebilir.
         */
        /// <summary>
        /// Servis kataloğunun adı
        /// </summary>
        public string Name { get; private set; } = "Default Catalog";
        /// <summary>
        /// Servis kataloğu ile ilgili detaylı bilgi
        /// </summary>
        public string Description { get; private set; } = string.Empty;
        /// <summary>
        /// Servislerin listesi
        /// </summary>
        public List<Service> Services { get; private set; } = []; // Boş bir liste oluşturur

        /// <summary>
        /// Servisleri tutan Catalog nesnesini örnekler
        /// </summary>
        /// <param name="name">Katalog adı</param>
        /// <param name="description">Katalog ile ilgili genel bilgiler</param>
        public Catalog(string name, string description)
        {
            Name = name;
            Description = description;
        }

        //TODO@Everyone AddService metodu nasıl daha iyi yazılabilir?
        public void AddService(Service service)
        {
            if (service == null)
            {
                throw new Exception("Service cannot be null.");
            }

            if (Services.Contains(service))
            {
                return;
            }

            Services.Add(service);
        }
        //public void AddService(string alias,IPAddress address,short port)
        //{

        //}
        //public void AddService(string alias, IPAddress address)
        //{

        //}
    }
}
