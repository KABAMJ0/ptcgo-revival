from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_prize_shift

card = PokemonToolCardDef(
    guid="691f6d4b-5916-5149-a203-625437431d99",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeDew.Name",
    display_name="Life Dew",
    searchable_by=["Life Dew", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=107,
    set_code="BW9",
    rarity=Rarities.Rare,
    passive=holder_prize_shift(-1, None, attack_only=False)
)
