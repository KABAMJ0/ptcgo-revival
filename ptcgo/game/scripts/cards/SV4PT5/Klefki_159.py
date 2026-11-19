from ptcgo.game.card_effects.attacks_common import discard_defender_tools_then_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="483b35b7-bfe5-5b21-bdfe-03cbe0856a86",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name",
    display_name="Klefki",
    searchable_by=["Klefki", "Basic", "Klefki"],
    subtypes=["Basic"],
    collector_number=159,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=707,
    abilities=[
        Ability(
            title="Mischievous Lock",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, Basic Pok\u00e9mon in play (both yours and your opponent's) have no Abilities, except for Mischievous Lock.",
            effect=discard_defender_tools_then_damage(),
        ),
        Attack(
            title="Joust",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)