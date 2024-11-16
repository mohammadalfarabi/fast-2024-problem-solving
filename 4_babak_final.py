class Warehouse:
    __item_storage = []
    __max_capacity = 250

    def get_total_item(self):
        result = 0

        for item in self.__item_storage:
            result += item["stocks"]
        
        return result

    def is_overload(self, stocks):
        new_total = stocks + self.get_total_item()

        if new_total > self.__max_capacity:
            return True
        
        return False
    
    def add_item(self, item_name, item_stocks):
        new_item = {"name": item_name, "stocks": item_stocks}

        if self.is_overload(item_stocks):
            return False

        for item in self.__item_storage:
            if new_item["name"] == item["name"]:
                item["stocks"] += new_item["stocks"]

                return new_item

        self.__item_storage = self.__item_storage + [new_item]
        return new_item
    
    def get_items(self):
        item_list = []

        for item in self.__item_storage:
            if not item["stocks"]:
                continue

            item_list = item_list + [item]
        
        return item_list

    def get_item_minmax_stocks(self):
        smallest = {"name": "", "stocks": 0}
        biggest = {"name": "", "stocks": 0}

        if not self.__item_storage:
            return False

        for item in self.__item_storage:
            if not item["stocks"]:
                continue

            elif (not biggest["stocks"]) and (not smallest["stocks"]):
                biggest, smallest = item, item

            elif item["stocks"] > biggest["stocks"]:
                biggest = item

            elif item["stocks"] < smallest["stocks"]:
                smallest = item
                
        return [smallest, biggest]
    
    def get_sort_items_name(self):
        item_list = []
        counter = 0

        for item in self.__item_storage:
            if not item_list:
                item_list = [item]

            elif item["name"] > item_list[-1]["name"]:
                item_list = item_list + [item]

            elif item["name"] < item_list[counter]["name"]:
                item_list = item_list[:counter] + [item] + item_list[counter:]

            counter += 1

        return item_list

    def get_sort_items_stocks(self):
        item_list = []
        counter = 0

        for item in self.__item_storage:
            if not item_list:
                item_list = [item]

            elif item["stocks"] > item_list[-1]["stocks"]:
                item_list = item_list + [item]

            elif item["stocks"] < item_list[counter]["stocks"]:
                item_list = item_list[:counter] + [item] + item_list[counter:]

            counter += 1
        
        return item_list
    
    def delete_item(self, item_name):
        edited_list = []

        for item in self.__item_storage:
            if item_name == item["name"] and item["stocks"]:
                item["stocks"] = 0
            
            elif item_name == item["name"] and not item["stocks"]:
                continue
            
            edited_list = edited_list + [item]
        
        self.__item_storage = edited_list
        return True

    def get_search_item(self, item_name):
        for item in self.__item_storage:
            if item_name == item["name"]:
                return item
        
        return
            
    def distribute_item(self, item_name, total_distribute):
        counter = 0

        for item in self.__item_storage:
            if item_name == item["name"]:
                if total_distribute > item["stocks"]:
                    return False
                
                item["stocks"] = item["stocks"] - total_distribute

                self.__item_storage = self.__item_storage[:counter] + [item] + self.__item_storage[counter + 1:]
                return item
            
            counter += 1
        
        return
            
            
        

def main():
    warehouse = Warehouse()
    condition = True

    while condition:
        print("Pilih fitur:")
        print("1. Tambah barang\n2. Menampilkan barang\n3. Pencarian barang\n4. Distribusi barang\n0. Keluar")
        
        menu = input("Masukkan pilihan menu anda: ")
        print()

        match menu:
            case "1":
                item_name = input("Masukkan nama barang: ")
                item_stocks = int(input("Masukkan jumlah stok barang: "))
                print()
                
                result = warehouse.add_item(item_name, item_stocks)

                if not result:
                    print("Barang gagal ditambahkan, kapasitas maksimum!")
                else:
                    print(f"Barang berhasil ditambahkan\n{result}")

                print()
            
            case "2":
                print("Pilih fitur:")
                print("1. Tampilkan semua barang\n2. Tampilkan stok paling sedikit\n3. Tampilkan stok paling banyak")

                menu = input("Masukkan pilihan anda: ")

                if menu == "1":
                    result = warehouse.get_items()
                    result = result if result else "Barang kosong"

                    print(f"Hasil:\n{result}\n")
                    continue

                result = warehouse.get_item_minmax_stocks()

                if not result:
                    print("Barang kosong\n")
                    continue

                match menu:
                    case "2":
                        print(f"Barang stok paling dikit:\n{result[0]}")
                    case "3":
                        print(f"Barang stok paling banyak:\n{result[1]}")
                
                print()
            
            case "3":
                item_name = input("Masukkan nama barang: ")
                result = warehouse.get_search_item(item_name)
                
                if not result:
                    print("Barang tidak ditemukan")
                    print()
                    continue
                    
                else:
                    print(f"Hasil:\n{result}")
                
                is_delete = input("Apakah anda ingin menghapus data ini? (y/n): ")
                print()

                if is_delete == "y":
                    result = warehouse.delete_item(result["name"])
                    
                    if not result:
                        print("Barang gagal dihapus!")
                    
                    else:
                        print("Barang berhasil dihapus")
                    
                print()

            case "4":
                item_name = input("Masukkan nama barang: ")
                total_distribution = int(input("Masukkan total distribusi: "))

                result = warehouse.distribute_item(item_name, total_distribution)

                if result == None:
                    print("Barang tidak ditemukan")

                elif result == False:
                    print("Stok barang tidak mencukupi")
                
                else:
                    print(f"Barang berhasil didistribusikan:\n{result}")
                
                print()
            
            case "0":
                print("Program dihentikan")
                condition = False
            
            case _:
                print("Maaf, menu yang anda pilih tidak terdapat pada menu!")

main()
