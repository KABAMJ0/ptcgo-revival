from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_attack_discount_typed

card = PokemonToolCardDef(
    guid="06cf15ae-a698-5e9a-aca6-5cbeda20e770",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KarateBelt.Name",
    display_name="Karate Belt",
    searchable_by=["Karate Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=201,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    passive=holder_attack_discount_typed("fighting", prize_behind=True)
)
