from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import abilities_off_for, all_of, any_of, pokemon_of, is_evolution_pokemon

card = StadiumCardDef(
    guid="863670df-0f40-501c-b9ec-f262b7db8a19",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleFrontier.Name",
    display_name="Battle Frontier",
    searchable_by=["Battle Frontier", "Stadium"],
    subtypes=["Stadium"],
    collector_number=75,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    passive=abilities_off_for(all_of(is_evolution_pokemon, any_of(pokemon_of("colorless"), pokemon_of("darkness"), pokemon_of("metal"))))
)
