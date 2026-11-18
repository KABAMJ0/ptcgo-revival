from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8b1daaec-3ccf-5aab-947a-6517ff767c2a",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=442,
    abilities=[
        Ability(
            title="Fettered in Misfortune",
            game_text="Basic Pok\u00e9mon V in play\u00a0(both yours and your opponent's)\u00a0have no Abilities.",
            effect=unimplemented,
        ),
        Attack(
            title="Fade Out",
            game_text="Put this Pok\u00e9mon and all attached cards into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)