import json
import logging
import inflect
import math


class recprec(object):
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    def __init__(self):
        self._stream = None
        self._recid = None
        self._weight = 100
        self._mapping = self.load_json("mapping.json")
        self._inf = inflect.engine()
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

    def html_load_json(self, infile):
        data = self.load_json(infile)
        table = ""
        for line in reversed(sorted(data.keys())):
            table += '<tr><td>{}</td><td>{}</td><td>{}</td><td><div ' \
                     'class="mid-graph"><div class="{} ' \
                     'mid-graph-bar-status">{}</div></div></td></tr>'.format(
                line,
                data[line]['name'],
                data[line]['skill'],
                self._inf.number_to_words(int(math.ceil(data[line]['weight']) / 10)),
                data[line]['weight']
            )
        return table

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
#c.html_load_json("data.json")