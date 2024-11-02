import requests
import json
import os
from core.helper import get_headers, countdown_timer, extract_user_data, config
from colorama import *
import random
from datetime import datetime, timedelta
import time


class Fastmint:
    def __init__(self) -> None:
        self.session = requests.Session()


    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        banner = f"""{Fore.GREEN}
                                         ██████  ██    ██   ██████  ██    ██  ███    ███  ██████   ███████  ██████  
                                        ██       ██    ██  ██       ██    ██  ████  ████  ██   ██  ██       ██   ██ 
                                        ██       ██    ██  ██       ██    ██  ██ ████ ██  ██████   █████    ██████  
                                        ██       ██    ██  ██       ██    ██  ██  ██  ██  ██   ██  ██       ██   ██ 
                                         ██████   ██████    ██████   ██████   ██      ██  ██████   ███████  ██   ██     
                                            """
        print(Fore.GREEN + Style.BRIGHT + banner + Style.RESET_ALL)
        print(Fore.GREEN + f" Fastmint App")
        print(Fore.RED + f" FREE TO USE = Join us on {Fore.GREEN}t.me/cucumber_scripts")
        print(Fore.YELLOW + f" before start please '{Fore.GREEN}git pull{Fore.YELLOW}' to update bot")
        print(f"{Fore.WHITE}~" * 60)

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def login(self, query: str):
        url = 'https://api.chaingn.org/auth/login'
        data = json.dumps({'OAuth': query})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            return result['sessionToken']
        else:
            return None
    
    def user(self, token: str):
        url = 'https://api.chaingn.org/user'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def wallets(self, token: str):
        url = 'https://api.chaingn.org/wallets'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def daily_visits(self, token: str):
        url = 'https://api.chaingn.org/user/daily_visits'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def refferal_info(self, token: str):
        url = 'https://api.chaingn.org/referral/info'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def claim_refferal(self, token: str):
        url = 'https://api.chaingn.org/referral/claim'
        data = {}
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.post(url, headers=self.headers, json=data)
        if response.status_code == 200:
            return True
        else:
            return False
        
    def start_farm(self, token: str, id: str):
        url = 'https://api.chaingn.org/wallet/farm'
        data = json.dumps({'id': id})
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def claim_farm(self, token: str, id: str):
        url = 'https://api.chaingn.org/wallet/claim'
        data = json.dumps({'id': id})
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def upgarde_info(self, token: str):
        url = 'https://api.chaingn.org/wallets/info'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None
        
    def farming_upgarde(self, token: str, id: str):
        url = 'https://api.chaingn.org/wallet/upgrade'
        data = json.dumps({'id': id})
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None

    def sub_tasks(self, token: str):
        url = 'https://api.chaingn.org/sub_tasks'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result['tasks']
        else:
            return None

    def check_tasks(self, token: str, recource_id: str):
        url = 'https://api.chaingn.org/sub_task'
        data = json.dumps({'recourceId': recource_id})
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None

    def check_wallet(self, token: str):
        url = 'https://api.chaingn.org/wallets/external'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })
        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None


    def create_mnemonic(self, token: str):
        url = 'https://api.chaingn.org/wallet/external'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.post(url, headers=self.headers, data='{}')
        result = response.json()
        if response.status_code == 200:
            mnemonic = result.get('mnemonic', None)
            if mnemonic:
                return mnemonic
            else:
                return None
        else:
            return None


    def create_wallet(self, token: str, mnemonic: str):
        url = 'https://api.chaingn.org/wallet/external'
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })
        data = json.dumps({'mnemonic': mnemonic})
        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            mnemonic = result.get('mnemonic', None)
            if mnemonic:
                return mnemonic
            else:
                return None
        else:
            return None

    def claim_tasks(self, token: str, task_id: str):
        url = 'https://api.chaingn.org/sub_task/claim'
        data = json.dumps({'id': task_id})
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        })

        response = self.session.put(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            return result
        else:
            return None


    def set_proxy(self, proxy):
        self.session.proxies = {
            "http": proxy,
            "https": proxy,
        }
        if '@' in proxy:
            host_port = proxy.split('@')[-1]
        else:
            host_port = proxy.split('//')[-1]
        return host_port

    def question(self):
        while True:
            fu = config['farming_upgrade']
            if fu:
                farming_upgrade = "y"
            else:
                farming_upgrade = "n"
            if farming_upgrade in ["y", "n"]:
                farming_upgrade = farming_upgrade == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to upgrade or 'n' to skip.{Style.RESET_ALL}")

        return farming_upgrade

    def save_mnemonic(self, id, mnemonic):
        tokens = json.loads(open("mnemonic.json").read())
        tokens[str(id)] = mnemonic
        open("mnemonic.json", "w").write(json.dumps(tokens, indent=4))


    def process_query(self, query: str, farming_upgrade: bool, user_id:str):

        token = self.login(query)

        if not token:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} Token Is None {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )

        if token:
            user = self.user(token)
            if not user:
                return

            wallets = self.wallets(token)
            if not wallets:
                return

            for wallet in wallets:
                if wallet:
                    id = wallet['id']
                    current_level = wallet['level']

                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {user['firstName']} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {wallet['balance']} MT {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Farming{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} Level {current_level} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                    time.sleep(2)

                    visits = self.daily_visits(token)
                    if visits and 'visits' in visits:
                        visit = [visit for visit in visits['visits'] if visit['isCompleted']]
                        
                        if visit:
                            last_visit = max(visit, key=lambda x: x['day'])
                            if last_visit['isCompleted'] and last_visit:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Rewards{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {last_visit['rewardMnt']} MT {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Streak{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {last_visit['day']} Day {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Isn't Success {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Success {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Is None {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )

                    refferal = self.refferal_info(token)
                    if refferal and refferal['membersCount'] != 0:
                        reward = refferal['rewardMnt']
                        if reward > 0:
                            claim = self.claim_refferal(token)
                            if claim:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}" 
                                    f"{Fore.WHITE+Style.BRIGHT} {reward} MT {Style.RESET_ALL}" 
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} Isn't Reward to Claim {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Count Is None {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                        )

                    if config['create_wallet']:
                        wallet_exist = self.check_wallet(token)
                        if not wallet_exist:
                            mnemonic= self.create_mnemonic(token)
                            if mnemonic:
                                self.save_mnemonic(user_id, mnemonic)
                                create_wallet_res = self.create_wallet(token, mnemonic)
                                if create_wallet_res:
                                    self.log(Fore.GREEN+ f'Successfully Created Wallet{Style.RESET_ALL}')
                                else:
                                    self.log(Fore.RED + f'Failed Created Wallet{Style.RESET_ALL}')
                            else:
                                self.log(Fore.RED + f'Failed Created Wallet{Style.RESET_ALL}')
                        else:
                            self.log(Fore.RED + f'Wallet already exist{Style.RESET_ALL}')


                    farm_date = wallet['startFarmDate']
                    if farm_date is None:
                        start = self.start_farm(token, id)
                        if start:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                            )

                    if farm_date:
                        farm_date_utc = datetime.fromisoformat(farm_date.replace('Z', '+00:00'))
                        claim_time = (farm_date_utc + timedelta(hours=6)).strftime('%x %X %Z')

                        Claim = self.claim_farm(token, id)
                        if Claim:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}" 
                                f"{Fore.WHITE+Style.BRIGHT} {wallet['info']['reward']} MT {Style.RESET_ALL}" 
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                            )

                            start = self.start_farm(token, id)
                            if start:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} Not Time to Claim {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}" 
                                f"{Fore.WHITE+Style.BRIGHT} {claim_time} {Style.RESET_ALL}" 
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}" 
                            )

                    if farming_upgrade:
                        farming_account = self.upgarde_info(token)
                        if farming_account:
                            next_level = current_level + 1

                            if next_level <= len(farming_account):
                                item = farming_account[next_level - 1]

                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} Upgrade to Level {next_level} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Profit{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {item['reward']} MT/Claim {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Cost{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {item['cost']} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                time.sleep(1)

                                if wallet['balance'] >= item['cost']:
                                    upgrade_farm = self.farming_upgarde(token, id)
                                    if upgrade_farm:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                            f"{Fore.GREEN+Style.BRIGHT} Is Upgraded {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                            f"{Fore.RED+Style.BRIGHT} Isn't Upgraded {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT} Isn't Upgraded {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} Balance Not Enough {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                    f"{Fore.YELLOW+Style.BRIGHT} Upgarde Is Reached Max Level {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Is None {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Upgrade Is Skipped {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )

                    MAX_CHECKS = 1
                    tasks = self.sub_tasks(token)
                    while tasks:
                        for task in tasks:
                            recource_id = task.get('recourceId')
                            task_id = task.get('id')
                            title = task.get('title', 'Unknown')
                            done = task.get('done', False)
                            claimed = task.get('claimed', False)

                            checks_done = task.get('checks_done', 0)

                            if not claimed:
                                if not done:
                                    if checks_done < MAX_CHECKS:
                                        check = self.check_tasks(token, recource_id)
                                        task['checks_done'] = checks_done + 1

                                        if check:
                                            self.log(
                                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                                f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                                f"{Fore.GREEN+Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                            )
                                            
                                            tasks = self.sub_tasks(token)
                                            break
                                        else:
                                            self.log(
                                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                                f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                                f"{Fore.RED+Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                            )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                            f"{Fore.YELLOW+Style.BRIGHT}Skipped after {MAX_CHECKS} attempts{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                        )

                                if task.get('done', False) and task_id is not None:
                                    claim = self.claim_tasks(token, task_id)
                                    if claim:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                            f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {task.get('reward', 0)} MT {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                            f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                        )
                        else:
                            break
        return wallet['balance']

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]
            with open('proxies.txt', 'r') as file:
                proxies = [line.strip() for line in file if line.strip()]

            farming_upgrade = self.question()

            while True:

                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Proxy's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(proxies)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-----------------------------------------------------------------------{Style.RESET_ALL}")

                for i, query in enumerate(queries):
                    query = query.strip()
                    if query:
                        self.log(
                            f"{Fore.GREEN + Style.BRIGHT}Account: {Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT}{i + 1} / {len(queries)}{Style.RESET_ALL}"
                        )
                        if len(proxies) >= len(queries):
                            proxy = self.set_proxy(proxies[i])  # Set proxy for each account
                            self.log(
                                f"{Fore.GREEN + Style.BRIGHT}Use proxy: {Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT}{proxy}{Style.RESET_ALL}"
                            )

                        else:
                            self.log(
                                Fore.RED + "Number of proxies is less than the number of accounts. Proxies are not used!")

                        user_info = extract_user_data(query)
                        user_name = str(user_info.get('username'))
                        user_id = str(user_info.get('id'))
                        self.headers = get_headers(user_id)

                        try:
                            balance = self.process_query(query, farming_upgrade, user_name)
                        except Exception as e:
                            self.log(f"{Fore.RED + Style.BRIGHT}An error process_query: {e}{Style.RESET_ALL}")
                            balance = 0

                        now = datetime.now().strftime("%Y-%m-%d %H:%M")
                        open("balance.txt", "a", encoding="utf-8").write(
                            f"{now}/{i+1}/{user_name}/{balance} \n")

                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}" * 75)
                        account_delay = config['account_delay']
                        countdown_timer(random.randint(min(account_delay), max(account_delay)))

                cycle_delay = config['cycle_delay']
                countdown_timer(random.randint(min(cycle_delay), max(cycle_delay)))

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Fastmint - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    fastmint = Fastmint()
    fastmint.clear_terminal()
    fastmint.welcome()
    fastmint.main()