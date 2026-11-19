from ptcgo.game.card_effects.attacks_common import damage_per, count_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="674560c8-db58-5bb9-8cf6-db0b0322f7e9",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunala.Name",
    display_name="Lunala ◇",
    searchable_by=["Lunala \u25c7", "Basic", "Prism Star", "Lunala"],
    subtypes=["Basic", "Prism Star"],
    collector_number=62,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=792,
    abilities=[
        Attack(
            title="Full Moon Star",
            game_text="For each of your opponent's Pok\u00e9mon in play, attach a Psychic Energy card from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Psystorm",
            game_text="This attack does 20 damage times the amount of Energy attached to all Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 4},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_energy("both"), 20),
        ),
    ],
)