import json
import logging


class recprec(object):
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    def __init__(self):
        self._stream = None
        self._recid = None
        self._weight = 0
        self._mapping = self.load_json("mapping.json")
        logging.basicConfig(
            filename = "main.log",
            level = logging.DEBUG,
            format = recprec.LOG_FORMAT
        )
        self.logger = logging.getLogger()

    def load_json(self, infile):
        """
        Read json file and return the data.
        """
        with open(infile) as data_file:
            data = json.load(data_file)
        return data

    def write_db(self):
        data = self.load_json("data.json")
        data[self._recid]["weight"] = self._weight
        data[self._recid]["mapping"] = "|".join(self._stream)
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

        self.logger.info(
            "Updated weight for [{} : {}] to {}".format(
            self._recid,
            data[self._recid]["name"],
            self._weight
            )
        )

    def calc_weight(self):
        """
        Read each character of stream and calculate the weight based on mapping.
        """
        self.logger.info("Calculating weight for id {}".format(self._recid))
        for idx, flag in enumerate(self._stream):
            if flag == "Y":
                self._weight += self._mapping["mapping"][idx]["weight"]
        self.write_db()
        print self._weight

    @property
    def stream(self):
        return self._stream

    @stream.setter
    def stream(self, value):
        self._stream = value.split("|")[0:-1]
        self._recid = value.split("|")[-1]
        print self._recid

#c = recprec()
#c.stream = 'Y|Y|Y|Y|Y|Y|Y|1'  # setter called
#c.calc_weight()
