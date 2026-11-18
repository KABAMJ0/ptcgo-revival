from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4ea52fbd-d7fa-568f-81c1-c609d018ba22",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    display_name="Munna",
    searchable_by=["Munna", "Basic", "Munna"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=517,
    abilities=[
        Attack(
            title="Rest",
            game_text="This Pok\u00e9mon is now Asleep. Heal 30 damage from it.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Mumble",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)