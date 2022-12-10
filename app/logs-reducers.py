def _reduce_logs_to_single_type_planet(type:str):
    counter = 0
    entitymass=0
    with open('xg-samples.log') as logs_document:
            lines = logs_document.readlines()
            for line in lines:
                if (line.split(",")[1] == type):
                    with open(f'xg-raw-data-{type}.log', 'a') as the_file:
                        the_file.write(line)


def _reduce_logs_to_avg_for_second(type):
    count = 0
    entitymass = 0
    with open(f'xg-dev-new-{type}.log') as logs_document:
            lines = logs_document.readlines()
            for line in lines:
                count += 1
                entitymass += float(line.split(",")[2])
                if (count==10):
                    count=0
                    with open(f'xg-dev-{type}-1second.log', 'a') as the_file:
                        line.split(",")[2] =entitymass 
                        the_file.write(line)
                    entitymass=0


def _avg_logs_1_min(type):
    count = 0
    entitymass = 0
    with open(f'xg-{type}-1second-avg.log') as logs_document:
            lines = logs_document.readlines()
            for line in lines:
                count += 1
                entitymass += float(line.split(",")[2])
                if (count==60):
                    count=0
                    entitymass=0
                    with open(f'xg-{type}-1min-avg.log', 'a') as logs_file:
                        line.split(",")[2] =entitymass 
                        logs_file.write(line)

