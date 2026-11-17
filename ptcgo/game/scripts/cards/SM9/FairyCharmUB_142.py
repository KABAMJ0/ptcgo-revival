from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import attacker_has_subtypes, pokemon_of, prevents_all_from

card = PokemonToolCardDef(
    guid="69cc2e46-9d61-5ccf-8927-f5264056f8c5",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmUB.Name",
    display_name="Fairy Charm UB",
    searchable_by=["Fairy Charm UB", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=142,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    passive=prevents_all_from(pokemon_of("fairy"), attacker_has_subtypes("Ultra Beast", "gx"))
)
